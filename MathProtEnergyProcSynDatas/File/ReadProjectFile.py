import numpy as np
import pandas as pd

from .ReadProjectFileBase import ReadProjectStructure, ReadModesAttributes, ReadAttributesBorders


# Считывание файла проекта для моделирования
def ReadProjectFileForModeling(ProjectFileName  # Имя файла проекта
                               ):
    # Открываем файл проекта
    (ProjectsAttributes,
     sep, dec) = ReadProjectStructure(ProjectFileName)

    # Имя файла
    ParametersFileName = ProjectsAttributes["ParametersFileName"]  # Файл csv параметров
    DynamicParametersFileName = ProjectsAttributes["DynamicParametersFileName"]  # Файл csv начального состояния аккумулятора
    AttributesFileName = ProjectsAttributes["AttributesFileName"]  # Файл csv аттрибутов аккумулятора
    IntegrateAttributesFileName = ProjectsAttributes["IntegrateAttributesFileName"]  # Файл csv аттрибутов интегрирования
    IndexesGraphicsFileName = ProjectsAttributes["IndexesGraphicsFileName"]  # Файл csv индексов графиков, которые нужно построить
    DynamicFileName = ProjectsAttributes["DynamicFileName"]  # Файл csv динамики
    dynamicParametersNDyblicates = ProjectsAttributes["DynamicParametersNDyblicates"]  # Число дубликаций начального состояния аккумулятора на каждый режим работы

    # Считываем файл аттрибутов режима
    modeAttributes = ReadModesAttributes(ProjectsAttributes, sep, dec)

    # Считываем файл начального состояния аккумулятора
    dynamicParameters = pd.read_csv(DynamicParametersFileName, sep=sep, decimal=dec)

    # Считываем файл аттрибутов аккумулятора
    attributes = pd.read_csv(AttributesFileName, sep=sep, decimal=dec)

    # Считываем файл аттрибутов интегрирования
    integrateAttributes = pd.read_csv(IntegrateAttributesFileName, sep=sep, decimal=dec)

    # Считываем файл индексов графиков
    indexesGraphics = pd.read_csv(IndexesGraphicsFileName, sep=sep, decimal=dec)

    # Вцыводим результат
    return (integrateAttributes,  # Аттрибуты интегрирования

            # Построение графиков
            indexesGraphics,  # Индексы графиков, которые нужно построить

            # Моделирование системы
            modeAttributes,  # Аттрибуты режима
            dynamicParameters,  # Начальное состояние
            attributes,  # Аттрибуты
            dynamicParametersNDyblicates,  # Число дубликаций динамик с разными параметрами

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
    (ProjectsAttributes,
     sep, dec) = ReadProjectStructure(ProjectFileName)

    # Исходные данные
    DynamicParametersFileName = ProjectsAttributes["DynamicParametersFileName"]  # Файл csv начального состояния
    AttributesFileName = ProjectsAttributes["AttributesFileName"]  # Файл csv аттрибутов
    DynamicParametersBorderFileName = ProjectsAttributes["DynamicParametersBorderFileName"]  # Файл csv границ начального состояния
    dynamicParametersNDyblicates = np.array(ProjectsAttributes["DynamicParametersNDyblicates"])  # Число состояний, определяющих конкретную динамику

    # Считываем файл аттрибутов
    modeAttributes = ReadModesAttributes(ProjectsAttributes, sep, dec)

    # Считываем файлы границ
    dynamicParametersBorder = pd.read_csv(DynamicParametersBorderFileName, sep=sep, decimal=dec)  # Границы начального состояния
    (attributesBorder, attributesNPoints) = ReadAttributesBorders(ProjectsAttributes, sep, dec)  # Границы аттрибутов

    # Получаем числа аттрибутов
    nModes = len(modeAttributes)  # Число режимов работы

    # Выводим результат
    return (attributesBorder,  # Границы аттрибутов
            dynamicParametersBorder,  # Границы начального состояния

            attributesNPoints,  # Число точек аттрибутов
            nModes,  # Число режимов работы
            dynamicParametersNDyblicates,  # Число состояний, определяющих конкретную динамику

            AttributesFileName,  # Файл csv аттрибутов аккумулятора
            DynamicParametersFileName,  # Файл csv начального состояния аккумулятора

            sep,  # Разделитель csv
            dec  # Десятичный разделитель
            )


def ReadProjectFileForGenerateDynamicParameters(ProjectFileName  # Имя файла проекта
                                                ):
    # Открываем файл проекта
    (ProjectsAttributes,
     sep, dec) = ReadProjectStructure(ProjectFileName)

    # Исходные данные
    DynamicParametersFileName = ProjectsAttributes["DynamicParametersFileName"]  # Файл csv начального состояния
    DynamicParametersBorderFileName = ProjectsAttributes["DynamicParametersBorderFileName"]  # Файл csv границ начального состояния
    dynamicParametersNDyblicates = np.array(ProjectsAttributes["DynamicParametersNDyblicates"])  # Число точек начального состояния
    attributesNPoints = ProjectsAttributes["AttributesNPoints"]  # Число точек аттрибутов

    # Считываем файлы границ
    dynamicParametersBorder = pd.read_csv(DynamicParametersBorderFileName, sep=sep, decimal=dec)  # Границы начального состояния

    # Считываем файл аттрибутов режима
    modeAttributes = ReadModesAttributes(ProjectsAttributes, sep, dec)

    # Получаем числа аттрибутов
    nModes = len(modeAttributes)  # Число режимов работы

    # Выводим результат
    return (dynamicParametersBorder,  # Границы начального состояния

            attributesNPoints,  # Число точек аттрибутов
            nModes,  # Число режимов работы
            dynamicParametersNDyblicates,  # Число состояний, определяющих конкретную динамику

            DynamicParametersFileName,  # Файл csv начального состояния аккумулятора

            sep,  # Разделитель csv
            dec  # Десятичный разделитель
            )


def ReadProjectFileForGenerateAttributes(ProjectFileName  # Имя файла проекта
                                         ):
    # Открываем файл проекта
    (ProjectsAttributes,
     sep, dec) = ReadProjectStructure(ProjectFileName)

    # Исходные данные
    AttributesFileName = ProjectsAttributes["AttributesFileName"]  # Файл csv аттрибутов

    # Считываем файлы границ
    (attributesBorder, attributesNPoints) = ReadAttributesBorders(ProjectsAttributes, sep, dec)  # Границы аттрибутов

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
    (ProjectsAttributes,
     sep, dec) = ReadProjectStructure(ProjectFileName)

    # Считываем имена файлов
    ParametersFileName = ProjectsAttributes["ParametersFileName"]  # Файл csv параметров
    ControlDynamicsFileName = ProjectsAttributes["ControlDynamicsFileName"]  # Файл csv параметров с контролтными динамиками

    # Считываем файл аттрибутов режима
    modeAttributes = ReadModesAttributes(ProjectsAttributes, sep, dec)

    # Считываем файл параметров
    parameters = pd.read_csv(ParametersFileName, sep=sep, decimal=dec)

    # Выводим результат
    return (modeAttributes,  # Аттрибуты режима
            parameters,  # Параметры

            sep,  # Разделитель csv
            dec,  # Десятичный разделитель

            ControlDynamicsFileName  # Имя файла csv параметров с контролтными динамиками
            )
