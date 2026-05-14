from MathProtEnergyProcSynDatas.File import ReadProjectFileForGenerateModelParameters
from MathProtEnergyProcSynDatas.File import ReadProjectFileForGenerateAttributes
from MathProtEnergyProcSynDatas.File import ReadProjectFileForGenerateDynamicParameters
from MathProtEnergyProcSynDatas.DatasGenerate import GenerateRandomDatasInDiapasonsFrame

from .GetModelingParameters import GetNDynamics

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


def RandomGenerateDynamicParametersBase(attributesNPoints,  # Число точек аттрибутов
                                        nModes,  # Число режимов работы
                                        dynamicParametersNDyblicates,  # Число состояний, определяющих конкретную динамику

                                        dynamicParametersBorder  # Границы динамических параметров
                                        ):
    # Получаем число характеристик каждой динамики (число динамик)
    dynamicParametersNPoints = GetNDynamics(attributesNPoints,  # Число точек аттрибутов
                                            nModes,  # Число режимов работы
                                            dynamicParametersNDyblicates  # Число состояний, определяющих конкретную динамику
                                            )

    # Генерируем и выводим значения параметров динамики
    return RandomGenerateDynamicParametersFunction(dynamicParametersBorder,  # Границы динамических параметров
                                                   dynamicParametersNPoints  # Числа динамических параметров в соответствующих границах
                                                   )


# Генерация аттрибутов и начального состояния
def RandomGenerateAttributesAndDynamicParametersBase(attributesNPoints,  # Число точек аттрибутов
                                                     nModes,  # Число режимов работы
                                                     dynamicParametersNDyblicates,  # Число состояний, определяющих конкретную динамику

                                                     attributesBorder,  # Границы аттрибутов
                                                     dynamicParametersBorder  # Границы динамических параметров
                                                     ):
    # Генерируем значения аттрибутов аккумулятора
    attributes = GenerateRandomDatasInDiapasonsFrame(attributesBorder,
                                                     attributesNPoints)

    # Генерируем значения параметров динамики
    dynamicParameters = RandomGenerateDynamicParametersBase(attributesNPoints,  # Число точек аттрибутов
                                                            nModes,  # Число режимов работы
                                                            dynamicParametersNDyblicates,  # Число состояний, определяющих конкретную динамику

                                                            dynamicParametersBorder  # Границы динамических параметров
                                                            )

    # Выводим результат
    return (attributes, dynamicParameters)


def RandomGenerateDynamicParameters(ProjectFileName  # Имя файла проекта
                                    ):
    # Считываем файл проекта
    (dynamicParametersBorder,  # Границы начального состояния

     attributesNPoints,  # Число точек аттрибутов
     nModes,  # Число режимов работы
     dynamicParametersNDyblicates,  # Число состояний, определяющих конкретную динамику

     DynamicParametersFileName,  # Файл csv начального состояния аккумулятора

     sep,  # Разделитель csv
     dec  # Десятичный разделитель
     ) = ReadProjectFileForGenerateDynamicParameters(ProjectFileName)

    # Генерируем значения параметров динамики
    dynamicParameters = RandomGenerateDynamicParametersBase(attributesNPoints,  # Число точек аттрибутов
                                                            nModes,  # Число режимов работы
                                                            dynamicParametersNDyblicates,  # Число состояний, определяющих конкретную динамику

                                                            dynamicParametersBorder  # Границы динамических параметров
                                                            )

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


# Генерация аттрибутов и начального состояния
def RandomGenerateAttributesAndDynamicParameters(ProjectFileName  # Имя файла проекта
                                                 ):
    # Считываем файл проекта
    (attributesBorder,  # Границы аттрибутов
     dynamicParametersBorder,  # Границы начального состояния

     attributesNPoints,  # Число точек аттрибутов
     nModes,  # Число режимов работы
     dynamicParametersNDyblicates,  # Число состояний, определяющих конкретную динамику

     AttributesFileName,  # Файл csv аттрибутов аккумулятора
     DynamicParametersFileName,  # Файл csv начального состояния аккумулятора

     sep,  # Разделитель csv
     dec  # Десятичный разделитель
     ) = ReadProjectFileForGenerateModelParameters(ProjectFileName)

    # Генерируем значения аттрибутов и параметров аккумулятора
    (attributes, dynamicParameters) = RandomGenerateAttributesAndDynamicParametersBase(attributesNPoints,  # Число точек аттрибутов
                                                                                       nModes,  # Число режимов работы
                                                                                       dynamicParametersNDyblicates,  # Число состояний, определяющих конкретную динамику

                                                                                       attributesBorder,  # Границы аттрибутов
                                                                                       dynamicParametersBorder  # Границы динамических параметров
                                                                                       )

    # Сохраняем значения аттрибутов аккумулятора в файл
    attributes.to_csv(AttributesFileName,
                      sep=sep, decimal=dec,
                      index=False)

    # Сохраняем значения начальных состояний аккумулятора в файл
    dynamicParameters.to_csv(DynamicParametersFileName,
                             sep=sep, decimal=dec,
                             index=False)
