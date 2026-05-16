import pandas as pd

from .ReadProjectFileBase import ReadProjectStructure, ReadModesAttributes, ReadAttributesBorders, ReadDynamicParametersBorder, ReadIntegrateAttributes


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
    dynamicParametersNDyblicates = ProjectsAttributes["DynamicParametersNDyblicates"]  # Число дубликаций начального состояния аккумулятора на каждый режим работы

    # Считываем файл аттрибутов режима
    (modeAttributes,
     nModes) = ReadModesAttributes(ProjectsAttributes, sep, dec)

    # Считываем файл начального состояния аккумулятора
    dynamicParameters = pd.read_csv(DynamicParametersFileName, sep=sep, decimal=dec)

    # Считываем файл аттрибутов аккумулятора
    attributes = pd.read_csv(AttributesFileName, sep=sep, decimal=dec)
    nAttrs = len(attributes)  # Число аттрибутов

    # Считываем файл аттрибутов интегрирования динамики
    integrateAttributes = ReadIntegrateAttributes(ProjectsAttributes, sep, dec)

    # Вцыводим результат
    return (ProjectsAttributes,

            # Интегрирование
            integrateAttributes,  # Аттрибуты интегрирования

            # Моделирование системы
            modeAttributes,  # Аттрибуты режима
            dynamicParameters,  # Начальное состояние
            attributes,  # Аттрибуты

            nModes,  # Число аттрибутов режима
            dynamicParametersNDyblicates,  # Число дубликаций динамик с разными параметрами
            nAttrs,  # Число аттрибутов

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

    # Считываем файл аттрибутов
    (_, nModes) = ReadModesAttributes(ProjectsAttributes, sep, dec)

    # Считываем файлы границ
    (dynamicParametersBorder,
     dynamicParametersNDyblicates) = ReadDynamicParametersBorder(ProjectsAttributes, sep, dec)  # Границы начального состояния
    (attributesBorder,
     attributesNPoints) = ReadAttributesBorders(ProjectsAttributes, sep, dec)  # Границы аттрибутов

    # Исходные данные
    DynamicParametersFileName = ProjectsAttributes["DynamicParametersFileName"]  # Файл csv начального состояния
    AttributesFileName = ProjectsAttributes["AttributesFileName"]  # Файл csv аттрибутов

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

    # Считываем файлы границ
    (dynamicParametersBorder,
     dynamicParametersNDyblicates) = ReadDynamicParametersBorder(ProjectsAttributes, sep, dec)  # Границы начального состояния

    # Считываем файл аттрибутов режима
    (_, nModes) = ReadModesAttributes(ProjectsAttributes, sep, dec)

    # Исходные данные
    DynamicParametersFileName = ProjectsAttributes["DynamicParametersFileName"]  # Файл csv начального состояния
    attributesNPoints = ProjectsAttributes["AttributesNPoints"]  # Число точек аттрибутов

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
    (attributesBorder,
     attributesNPoints) = ReadAttributesBorders(ProjectsAttributes, sep, dec)  # Границы аттрибутов

    # Выводим результат
    return (attributesBorder,  # Границы аттрибутов
            attributesNPoints,  # Число точек аттрибутов

            AttributesFileName,  # Файл csv аттрибутов аккумулятора

            sep,  # Разделитель csv
            dec  # Десятичный разделитель
            )
