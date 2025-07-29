from .File import ReadProjectFileForGenerateModelParameters
from .File import ReadProjectFileForGenerateAttributes
from .File import ReadProjectFileForGenerateDynamicParameters
from .DatasGenerate import GenerateRandomDatasInDiapasonsFrame
from .File import ParametersSave, ReadProjectFileForModeling
from .File import ReadProjectFileForSelectControlDynamics

from MathProtEnergyProc.IndexedNames import IndexedNamesFromIndexes
from MathProtEnergyProc import CountDynamicsQ

from pandas import DataFrame, concat

import numpy as np


# Генерируем начальные состояния
def RandomGenerateDynamicParametersFunction(dynamicParametersBorder,  # Границы динамических параметров
                                            dynamicParametersNPoints  # Числа динамических параметров в соответствующих границах
                                            ):
    # Генерируем значения параметров динамики
    dynamicParameters = GenerateRandomDatasInDiapasonsFrame(dynamicParametersBorder,
                                                            dynamicParametersNPoints)

    # Перемешиваем случайно строки
    dynamicParametersValues = dynamicParameters.to_numpy()
    np.random.shuffle(dynamicParametersValues)
    dynamicParameters[:] = dynamicParametersValues

    # Выводим результат
    return dynamicParameters


# Геенрация аттрибутов и начального состояния
def RandomGenerateAttributesAndDynamicParameters(ProjectFileName  # Имя файла проекта
                                                 ):
    # Считываем файл проекта
    (attributesBorder,  # Границы аттрибутов
     attributesNPoints,  # Число точек аттрибутов
     AttributesFileName,  # Файл csv аттрибутов аккумулятора
     dynamicParametersBorder,  # Границы начального состояния
     dynamicParametersNPoints,  # Число динамик
     DynamicParametersFileName,  # Файл csv начального состояния аккумулятора
     sep,  # Разделитель csv
     dec  # Десятичный разделитель
     ) = ReadProjectFileForGenerateModelParameters(ProjectFileName)

    # Генерируем значения аттрибутов аккумулятора
    attributes = GenerateRandomDatasInDiapasonsFrame(attributesBorder,
                                                     attributesNPoints)

    # Генерируем значения параметров динамики
    dynamicParameters = RandomGenerateDynamicParametersFunction(dynamicParametersBorder,  # Границы динамических параметров
                                                                dynamicParametersNPoints  # Числа динамических параметров в соответствующих границах
                                                                )

    # Сохраняем значения аттрибутов аккумулятора в файл
    attributes.to_csv(AttributesFileName,
                      sep=sep, decimal=dec,
                      index=False)

    # Сохраняем значения начальных состояний аккумулятора в файл
    dynamicParameters.to_csv(DynamicParametersFileName,
                             sep=sep, decimal=dec,
                             index=False)


def RandomGenerateAttributes(ProjectFileName  # Имя файла проекта
                             ):
    # Считываем файл проекта
    (attributesBorder,  # Границы аттрибутов
     attributesNPoints,  # Число точек аттрибутов
     AttributesFileName,  # Файл csv аттрибутов аккумулятора
     sep,  # Разделитель csv
     dec  # Десятичный разделитель
     ) = ReadProjectFileForGenerateAttributes(ProjectFileName)

    # Генерируем значения аттрибутов аккумулятора
    attributes = GenerateRandomDatasInDiapasonsFrame(attributesBorder,
                                                     attributesNPoints)

    # Сохраняем значения аттрибутов аккумулятора в файл
    attributes.to_csv(AttributesFileName,
                      sep=sep, decimal=dec,
                      index=False)


def RandomGenerateDynamicParameters(ProjectFileName  # Имя файла проекта
                                    ):
    # Считываем файл проекта
    (dynamicParametersBorder,  # Границы начального состояния
     dynamicParametersNPoints,  # Число динамик
     DynamicParametersFileName,  # Файл csv начального состояния аккумулятора
     sep,  # Разделитель csv
     dec  # Десятичный разделитель
     ) = ReadProjectFileForGenerateDynamicParameters(ProjectFileName)

    # Генерируем значения параметров динамики
    dynamicParameters = RandomGenerateDynamicParametersFunction(dynamicParametersBorder,  # Границы динамических параметров
                                                                dynamicParametersNPoints  # Числа динамических параметров в соответствующих границах
                                                                )

    # Сохраняем значения начальных состояний аккумулятора в файл
    dynamicParameters.to_csv(DynamicParametersFileName,
                             sep=sep, decimal=dec,
                             index=False)


# Функция расчета динамик
def SystemDynamicsFunction(Pars,  # Параметры

                           # Параметры интегрирования
                           integrateAttributes,  # Аттрибуты интегрирования

                           # Класс системы
                           sysDyn,  # Динамики системы

                           # Функции обработки
                           inputArrayCreate,  # Функция предобработки входных данных
                           outputArrayCreate,  # Функция постобработки выходных данных

                           # Построение графиков
                           indexesGraphics,  # Индексы графиков, которые нужно построить
                           buildingGraphics,  # Необходимость построения графиков

                           # Имя файла
                           DynamicFileNameBase,  # Базовое имя файла csv
                           sep,  # Разделитель csv
                           dec  # Десятичный разделитель
                           ):
    # Исходные данные моделирования системы
    (Tints,
     stateCoordinates0s,
     reducedTemp0s,
     systemParameters,
     ts) = inputArrayCreate(Pars,  # Параметры

                            integrateAttributes  # Аттрибуты интегрирования
                            )

    # Функция сохранения в файл
    def SavedFinction(dyn, index):
        # Индекс
        index += 1

        # Формируем имя файла
        fileName = IndexedNamesFromIndexes([index],  # Индексы
                                           DynamicFileNameBase,  # Начало имени
                                           endName=".csv",  # Конец имени
                                           sepName="_"  # Раздлитель имени
                                           )[0]

        # Сохраняем данные в файл
        BuildGraphic = (buildingGraphics and np.any(index == indexesGraphics))  # Необходимость построения графика
        if BuildGraphic:
            print("Graphic dynamic index: ", index)
        outputArrayCreate(dyn, fileName, sep, dec, plotGraphics=BuildGraphic)

        # Возвращаем имя файла
        return index

    # Задаем класс динамик системы
    sysDyns = CountDynamicsQ(sysDyn, SavedFinction)

    # Моделируем динамики
    indexes = sysDyns.ComputingExperimentQ(Tints,
                                           stateCoordinates0s,
                                           reducedTemp0s,
                                           systemParameters,
                                           t_evals=ts)  # Индекс динамики начинается с единицы

    # Выводим результат
    return DataFrame({"dynamicIndex": indexes.reshape(-1,)})


# Моделирование динамик системы
def SystemDynamicsModeling(ProjectFileName,  # Имя файла проекта

                           # Функция класса системы
                           sysCreate,  # Функция создания системы

                           # Функции обработки
                           inputArrayCreate,  # Функция предобработки входных данных
                           outputArrayCreate  # Функция постобработки выходных данных
                           ):
    # Считываем файл проекта
    (Pars,  # Параметры

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
     ) = ReadProjectFileForModeling(ProjectFileName)

    # Динамика системы
    sysDyn = sysCreate(integrateMethod  # Метод интегрирования дифференциальных уравнений
                       )

    # Выполняем моделирование динамики системы
    dynamicIndex = SystemDynamicsFunction(Pars,  # Параметры

                                          # Параметры интегрирования
                                          integrateAttributes,  # Аттрибуты интегрирования

                                          # Динамика системы
                                          sysDyn,

                                          # Функции обработки
                                          inputArrayCreate,  # Функция предобработки входных данных
                                          outputArrayCreate,  # Функция постобработки выходных данных

                                          # Построение графиков
                                          indexesGraphics,  # Индексы графиков, которые нужно построить
                                          buildingGraphics,  # Необходимость построения графиков

                                          # Имя файла динамики
                                          DynamicFileName,  # Файл csv
                                          sep,  # Разделитель csv
                                          dec  # Десятичный разделитель
                                          )

    # Сохраняем параметры
    ParametersSave(dynamicIndex,  # Индексы динамик
                   Pars,  # Параметры
                   ParametersFileName,  # Имя файла параметров
                   sep,  # CSV разделитель
                   dec  # Десятичный разделитель
                   )


# Выделяем контрольные динамики
def SelectControlDynamics(controlDynamicIndexes,  # Индексы контрольных динамик
                          controlDynamicNames,  # Имена контрольных динамик
                          nModes,  # Число режимов
                          parameters,  # Параметры, полученные в результате эксперимента

                          needRepeat=False  # Нужно ли повторять контрольные динамики
                          ):
    # Получаем индексы динамик
    dynamicIndexes = parameters["dynamicIndex"].to_numpy()

    # Приводим динамики к матрице и выделяем контрольные динамики
    dynamicIndexes.shape = (-1, nModes)  # Приводим к матрице, столбцами которой являются разные режимы работы системы
    aControlDynamicIndexes = np.array(controlDynamicIndexes) - 1  # Приводим индексы контрольных динамик к индексации numpy
    controlDynamicIndexesMatrix = dynamicIndexes[:, aControlDynamicIndexes]  # Получаем индексы контрольных динамик
    if needRepeat:
        controlDynamicIndexesMatrix = np.repeat(controlDynamicIndexesMatrix, nModes, axis=0)  # Повторяем элементы массива индексов контрольных динамик

    # Упаковываем в pandas
    return DataFrame(controlDynamicIndexesMatrix,
                     columns=controlDynamicNames)


# Конкатенуем контрольные динамики
def ConcatControlDynamics(controlDynamicIndexes,  # Индексы контрольных динамик
                          controlDynamicNames,  # Имена контрольных динамик
                          modeAttributes,  # Аттрибуты режимов
                          parameters,  # Параметры, полученные в результате эксперимента

                          deletingParameters=False  # Удаляем параметры
                          ):
    # Число аттрибутов режима
    nModes = len(modeAttributes)

    # Получаем контрольные динамики
    pControlDynamicIndexesMatrix = SelectControlDynamics(controlDynamicIndexes,  # Индексы контрольных динамик
                                                         controlDynamicNames,  # Имена контрольных динамик
                                                         nModes,  # Число режимов
                                                         parameters,  # Параметры, полученные в результате эксперимента

                                                         needRepeat=True  # Нужно ли повторять контрольные динамики
                                                         )

    # Конкатенуем данные
    parametersExt = concat([parameters, pControlDynamicIndexesMatrix], axis=1)  # Конкатенованные параметры
    if deletingParameters:  # Удаляем при необходимости лишнее
        modeAttributesNames = list(modeAttributes)  # Заголовки аттрибутов режима

        return parametersExt[["dynamicIndex"] + controlDynamicNames + modeAttributesNames]
    else:
        return parametersExt


# Функция конкатенации контрольных динамик в файл результатов
def ConcatenateControlDynamics(ProjectFileName,  # Имя файла проекта

                               controlDynamicIndexes,  # Индексы контрольных динамик
                               controlDynamicNames,  # Имена контрольных динамик

                               deletingParameters=False  # Удаляем параметры
                               ):
    # Считываем файл проекта
    (modeAttributes,  # Аттрибуты режима
     parameters,  # Параметры
     sep,  # Разделитель csv
     dec,  # Десятичный разделитель

     ControlDynamicsFileName  # Имя файла csv параметров с контролтными динамиками
     ) = ReadProjectFileForSelectControlDynamics(ProjectFileName  # Имя файла проекта
                                                 )

    # Получаем конкатенованные параметры
    parametersExt = ConcatControlDynamics(controlDynamicIndexes,  # Индексы контрольных динамик
                                          controlDynamicNames,  # Имена контрольных динамик
                                          modeAttributes,  # Аттрибуты режимов
                                          parameters,  # Параметры, полученные в результате эксперимента

                                          deletingParameters=deletingParameters  # Удаляем параметры
                                          )

    # Сохраняем в файл
    parametersExt.to_csv(ControlDynamicsFileName,
                         sep=sep, decimal=dec,
                         index=False)
