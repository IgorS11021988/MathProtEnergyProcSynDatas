import numpy as np
import pandas as pd
import json as js

from .DatasIndexes import IndexesGraphics
from .DatasIntegrate import ConcatModelingParameters, IntegrateAttributes


# Функция сохранения параметров
def ParametersSave(dynamicCharacteristics,  # Индексы динамик
                   Pars,  # Параметры
                   ParametersFileName,  # Имя файла параметров

                   sep,  # CSV разделитель
                   dec  # Десятичный разделитель
                   ):  # Сохранение параметров в файл
    # Конкатенуем характеристики динамик к параметрам динамик
    allDynamicDatas = pd.concat([Pars, dynamicCharacteristics], axis=1)  # Параметры для

    # Сохраняем параметры в файл
    allDynamicDatas.to_csv(ParametersFileName, sep=sep, decimal=dec, index=False)  # Сохраняем в csv файл


# Считывание файла проекта для моделирования
def ReadProjectFileForModeling(ProjectFileName  # Имя файла проекта
                               ):
    # Открываем файл проекта
    with open(ProjectFileName, 'r') as ProjFileName:
        ProjectsAttributes = js.load(ProjFileName)

    # Метод интегрирования дифференциальных уравнений
    integrateMethod = ProjectsAttributes["integrateMethod"]

    # Имя файла
    ParametersFileName = ProjectsAttributes["ParametersFileName"]  # Файл csv параметров
    ModeAttributesFileName = ProjectsAttributes["ModeAttributesFileName"]  # Файл csv аттрибутов режима
    DynamicParametersFileName = ProjectsAttributes["DynamicParametersFileName"]  # Файл csv начального состояния аккумулятора
    AttributesFileName = ProjectsAttributes["AttributesFileName"]  # Файл csv аттрибутов аккумулятора
    IntegrateAttributesFileName = ProjectsAttributes["IntegrateAttributesFileName"]  # Файл csv аттрибутов интегрирования
    IndexesGraphicsFileName = ProjectsAttributes["IndexesGraphicsFileName"]  # Файл csv индексов графиков, которые нужно построить
    DynamicFileName = ProjectsAttributes["DynamicFileName"]  # Файл csv динамики
    dynamicParametersNDyblicates = ProjectsAttributes["DynamicParametersNDyblicates"]  # Число дубликаций начального состояния аккумулятора на каждый режим работы

    # Разделители csv
    sep = ProjectsAttributes["sep"]  # Разделитель csv
    dec = ProjectsAttributes["dec"]  # Десятичный разделитель

    # Считываем файл аттрибутов режима
    modeAttributes = pd.read_csv(ModeAttributesFileName, sep=sep, decimal=dec)

    # Считываем файл начального состояния аккумулятора
    dynamicParameters = pd.read_csv(DynamicParametersFileName, sep=sep, decimal=dec)

    # Считываем файл аттрибутов аккумулятора
    attributes = pd.read_csv(AttributesFileName, sep=sep, decimal=dec)

    # Размножаем параметры
    Pars = ConcatModelingParameters(modeAttributes,  # Аттрибуты режима
                                    dynamicParameters,  # Начальное состояние
                                    attributes,  # Аттрибуты
                                    dynamicParametersNDyblicates  # Число дубликаций динамик с разными параметрами
                                    )

    # Считываем файл аттрибутов интегрирования
    integrateAttributes = pd.read_csv(IntegrateAttributesFileName, sep=sep, decimal=dec)

    # Получаем числа аттрибутов
    nDyns = len(Pars)  # Число динамик
    nAttrs = len(attributes)  # Число аттрибутов аккумулятора
    nMode = len(modeAttributes)  # Число аттрибутов режима

    # Массив заголовков индексов аттрибутов
    arrNamesAllAttrsIndexes = ["indexMode", "indexDynamicParameters", "indexParameters"]

    # Массив чисел аттрибутов
    arrNAllAttrs = [nMode, dynamicParametersNDyblicates, nAttrs]

    # Вычисляем аттрибуты интегрирования
    integrateAttributes = IntegrateAttributes(integrateAttributes,
                                              arrNamesAllAttrsIndexes,
                                              arrNAllAttrs,
                                              nDyns)  # Приравниваем базовые аттрибуты интегрирования

    # Считываем файл индексов графиков
    indexesGraphics = pd.read_csv(IndexesGraphicsFileName, sep=sep, decimal=dec)

    # Формируем индексы динамик, графики которых мы будем строить
    (indexesGraphics, buildingGraphics) = IndexesGraphics(indexesGraphics,
                                                          arrNamesAllAttrsIndexes,
                                                          arrNAllAttrs)

    # Вцыводим результат
    return (Pars,  # Параметры

            # Параметры интегрирования
            integrateAttributes,  # Аттрибуты интегрирования
            integrateMethod,  # Метод интегрирования дифференциальных уравнений

            # Построение графиков
            indexesGraphics,  # Индексы графиков, которые нужно построить
            buildingGraphics,  # Необходимость построения графиков

            # Имя файла динамики
            DynamicFileName,  # Файл csv

            # Имя файла параметров
            ParametersFileName,

            sep,  # Разделитель csv
            dec  # Десятичный разделитель
            )


# Считывание файла проекта для генерации значений параметров модели
def ReadProjectFileForGenerateModelParameters(ProjectFileName  # Имя файла проекта
                                              ):
    # Открываем файл проекта
    with open(ProjectFileName, 'r') as ProjFileName:
        ProjectsAttributes = js.load(ProjFileName)

    # Исходные данные
    ModeAttributesFileName = ProjectsAttributes["ModeAttributesFileName"]  # Файл csv аттрибутов тока
    DynamicParametersFileName = ProjectsAttributes["DynamicParametersFileName"]  # Файл csv начального состояния
    AttributesFileName = ProjectsAttributes["AttributesFileName"]  # Файл csv аттрибутов
    DynamicParametersBorderFileName = ProjectsAttributes["DynamicParametersBorderFileName"]  # Файл csv границ начального состояния
    AttributesBorderFileName = ProjectsAttributes["AttributesBorderFileName"]  # Файл csv границ аттрибутов
    dynamicParametersNDyblicates = np.array(ProjectsAttributes["DynamicParametersNDyblicates"])  # Число точек начального состояния
    attributesNPoints = ProjectsAttributes["AttributesNPoints"]  # Число точек аттрибутов
    sep = ProjectsAttributes["sep"]  # Разделитель csv
    dec = ProjectsAttributes["dec"]  # Десятичный разделитель

    # Считываем файл аттрибутов тока
    modeAttributes = pd.read_csv(ModeAttributesFileName, sep=sep, decimal=dec)

    # Считываем файлы границ
    dynamicParametersBorder = pd.read_csv(DynamicParametersBorderFileName, sep=sep, decimal=dec)  # Границы начального состояния
    attributesBorder = pd.read_csv(AttributesBorderFileName, sep=sep, decimal=dec)  # Границы аттрибутов

    # Получаем числа аттрибутов
    nModes = len(modeAttributes)  # Число режимов работы

    # Получаем число характеристик каждой динамики (число динамик)
    dynamicParametersNPoints = nModes * dynamicParametersNDyblicates * attributesNPoints

    # Выводим результат
    return (attributesBorder,  # Границы аттрибутов
            attributesNPoints,  # Число точек аттрибутов
            AttributesFileName,  # Файл csv аттрибутов аккумулятора
            dynamicParametersBorder,  # Границы начального состояния
            dynamicParametersNPoints,  # Число характеристик каждой динамики (число динамик)
            DynamicParametersFileName,  # Файл csv начального состояния аккумулятора
            sep,  # Разделитель csv
            dec  # Десятичный разделитель
            )


def ReadProjectFileForGenerateDynamicParameters(ProjectFileName  # Имя файла проекта
                                                ):
    # Открываем файл проекта
    with open(ProjectFileName, 'r') as ProjFileName:
        ProjectsAttributes = js.load(ProjFileName)

    # Исходные данные
    ModeAttributesFileName = ProjectsAttributes["ModeAttributesFileName"]  # Файл csv аттрибутов тока
    DynamicParametersFileName = ProjectsAttributes["DynamicParametersFileName"]  # Файл csv начального состояния
    DynamicParametersBorderFileName = ProjectsAttributes["DynamicParametersBorderFileName"]  # Файл csv границ начального состояния
    dynamicParametersNDyblicates = np.array(ProjectsAttributes["DynamicParametersNDyblicates"])  # Число точек начального состояния
    attributesNPoints = ProjectsAttributes["AttributesNPoints"]  # Число точек аттрибутов
    sep = ProjectsAttributes["sep"]  # Разделитель csv
    dec = ProjectsAttributes["dec"]  # Десятичный разделитель

    # Считываем файл аттрибутов тока
    modeAttributes = pd.read_csv(ModeAttributesFileName, sep=sep, decimal=dec)

    # Считываем файлы границ
    dynamicParametersBorder = pd.read_csv(DynamicParametersBorderFileName, sep=sep, decimal=dec)  # Границы начального состояния

    # Получаем числа аттрибутов
    nModes = len(modeAttributes)  # Число режимов работы

    # Получаем число характеристик каждой динамики (число динамик)
    dynamicParametersNPoints = nModes * dynamicParametersNDyblicates * attributesNPoints

    # Выводим результат
    return (dynamicParametersBorder,  # Границы начального состояния
            dynamicParametersNPoints,  # Число характеристик каждой динамики (число динамик)
            DynamicParametersFileName,  # Файл csv начального состояния аккумулятора
            sep,  # Разделитель csv
            dec  # Десятичный разделитель
            )


def ReadProjectFileForGenerateAttributes(ProjectFileName  # Имя файла проекта
                                         ):
    # Открываем файл проекта
    with open(ProjectFileName, 'r') as ProjFileName:
        ProjectsAttributes = js.load(ProjFileName)

    # Исходные данные
    AttributesFileName = ProjectsAttributes["AttributesFileName"]  # Файл csv аттрибутов
    AttributesBorderFileName = ProjectsAttributes["AttributesBorderFileName"]  # Файл csv границ аттрибутов
    attributesNPoints = ProjectsAttributes["AttributesNPoints"]  # Число точек аттрибутов
    sep = ProjectsAttributes["sep"]  # Разделитель csv
    dec = ProjectsAttributes["dec"]  # Десятичный разделитель

    # Считываем файлы границ
    attributesBorder = pd.read_csv(AttributesBorderFileName, sep=sep, decimal=dec)  # Границы аттрибутов

    # Выводим результат
    return (attributesBorder,  # Границы аттрибутов
            attributesNPoints,  # Число точек аттрибутов
            AttributesFileName,  # Файл csv аттрибутов аккумулятора
            sep,  # Разделитель csv
            dec  # Десятичный разделитель
            )


# Считывание файла пргоекта для выделения контрльных динамик
def ReadProjectFileForSelectControlDynamics(ProjectFileName  # Имя файла проекта
                                            ):
    # Считываем файл проекта
    with open(ProjectFileName, 'r') as ProjFileName:
        ProjectsAttributes = js.load(ProjFileName)

    # Считываем имена файлов
    ParametersFileName = ProjectsAttributes["ParametersFileName"]  # Файл csv параметров
    ModeAttributesFileName = ProjectsAttributes["ModeAttributesFileName"]  # Файл csv аттрибутов режима
    ControlDynamicsFileName = ProjectsAttributes["ControlDynamicsFileName"]  # Файл csv параметров с контролтными динамиками

    # Разделители csv
    sep = ProjectsAttributes["sep"]  # Разделитель csv
    dec = ProjectsAttributes["dec"]  # Десятичный разделитель

    # Считываем файл аттрибутов режима
    modeAttributes = pd.read_csv(ModeAttributesFileName, sep=sep, decimal=dec)

    # Считываем файл параметров
    parameters = pd.read_csv(ParametersFileName, sep=sep, decimal=dec)

    # Выводим результат
    return (modeAttributes,  # Аттрибуты режима
            parameters,  # Параметры
            sep,  # Разделитель csv
            dec,  # Десятичный разделитель

            ControlDynamicsFileName  # Имя файла csv параметров с контролтными динамиками
            )
