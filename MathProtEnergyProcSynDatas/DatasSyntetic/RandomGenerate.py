from MathProtEnergyProcSynDatas.File import ReadProjectFileForGenerateModelParameters
from MathProtEnergyProcSynDatas.File import ReadProjectFileForGenerateAttributes
from MathProtEnergyProcSynDatas.File import ReadProjectFileForGenerateDynamicParameters

from MathProtEnergyProcSynDatas.DatasGenerate import GenerateRandomDatasInDiapasonsFrame

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


# Генерация аттрибутов и начального состояния
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
