import numpy as np
import pandas as pd
import json as js


# Считывание файлас труктуры проекта
def ReadProjectStructure(ProjectFileName  # Имя файла проекта
                         ):
    # Открываем файл проекта
    with open(ProjectFileName, 'r') as ProjFileName:
        ProjectsAttributes = js.load(ProjFileName)

    # Считываем разделители
    sep = ProjectsAttributes["sep"]  # Разделитель csv
    dec = ProjectsAttributes["dec"]  # Десятичный разделитель

    # Выводим структуру проекта
    return (ProjectsAttributes,
            sep, dec)


# Считывание файла аттрибутов режима
def ReadModesAttributes(ProjectsAttributes,  # Аттрибуты проекта

                        # Десятичные разделители
                        sep,  # Разделитель csv
                        dec  # Десятичный разделитель
                        ):
    # Имена файлов
    ModeAttributesFileName = ProjectsAttributes["ModeAttributesFileName"]  # Файл csv аттрибутов режима

    # Считываем файл аттрибутов режима
    modeAttributes = pd.read_csv(ModeAttributesFileName, sep=sep, decimal=dec)

    # Выводим эти аттрибуты и их число
    return (modeAttributes,
            len(modeAttributes))


# Считывание файла аттрибутов оптимизационных режима
def ReadOptimizeModesAttributes(ProjectsAttributes,  # Аттрибуты проекта

                                # Десятичные разделители
                                sep,  # Разделитель csv
                                dec  # Десятичный разделитель
                                ):
    # Имена файлов
    OptimizeModeAttributesFileName = ProjectsAttributes["OptimizeModeAttributesFileName"]  # Файл csv аттрибутов режима

    # Считываем файл аттрибутов режима
    optimizeModeAttributes = pd.read_csv(OptimizeModeAttributesFileName, sep=sep, decimal=dec)

    # Выводим эти аттрибуты и их число
    return (optimizeModeAttributes,
            len(optimizeModeAttributes))


# Считываем файл границ аттрибутов
def ReadAttributesBorders(ProjectsAttributes,  # Аттрибуты проекта

                          # Десятичные разделители
                          sep,  # Разделитель csv
                          dec  # Десятичный разделитель
                          ):
    # Получаем аттрбуты
    AttributesBorderFileName = ProjectsAttributes["AttributesBorderFileName"]  # Файл csv границ аттрибутов
    attributesNPoints = np.array(ProjectsAttributes["AttributesNPoints"], dtype=np.int_)  # Число точек аттрибутов

    # Считываем файлы границ
    attributesBorder = pd.read_csv(AttributesBorderFileName, sep=sep, decimal=dec)  # Границы аттрибутов

    # Выводим результат
    return (attributesBorder,  # Границы аттрибутов

            attributesNPoints  # Число генерируемых точек аттрибутов
            )


# Считываем файл границ параметров динамики
def ReadDynamicParametersBorder(ProjectsAttributes,  # Аттрибуты проекта

                                # Десятичные разделители
                                sep,  # Разделитель csv
                                dec  # Десятичный разделитель
                                ):
    # Получаем аттрбуты
    DynamicParametersBorderFileName = ProjectsAttributes["DynamicParametersBorderFileName"]  # Файл csv границ начального состояния
    dynamicParametersNDyblicates = np.array(ProjectsAttributes["DynamicParametersNDyblicates"], dtype=np.int_)  # Число состояний, определяющих конкретную динамику

    # Считываем файлы границ
    dynamicParametersBorder = pd.read_csv(DynamicParametersBorderFileName, sep=sep, decimal=dec)  # Границы начального состояния

    # Выводим результат
    return (dynamicParametersBorder,  # Границы аттрибутов

            dynamicParametersNDyblicates  # Число генерируемых точек аттрибутов
            )


# Считываем аттрибуты интегрирования
def ReadIntegrateAttributes(ProjectsAttributes,  # Аттрибуты проекта

                            # Десятичные разделители
                            sep,  # Разделитель csv
                            dec  # Десятичный разделитель
                            ):
    # Получаем аттрбуты
    IntegrateAttributesFileName = ProjectsAttributes["IntegrateAttributesFileName"]  # Файл csv аттрибутов интегрирования

    # Считываем файлы аттрибутов
    integrateAttributes = pd.read_csv(IntegrateAttributesFileName, sep=sep, decimal=dec)  # Аттрибуты интегирования

    # Вывыдим считанные аттрибуты
    return integrateAttributes


# Считываем аттрибуты интегрирования для оптимизации
def ReadOptimizeIntegrateAttributes(ProjectsAttributes,  # Аттрибуты проекта

                                    # Десятичные разделители
                                    sep,  # Разделитель csv
                                    dec  # Десятичный разделитель
                                    ):
    # Получаем аттрбуты
    OptimizeIntegrateAttributesFileName = ProjectsAttributes["OptimizeIntegrateAttributesFileName"]  # Файл csv аттрибутов интегрирования

    # Считываем файлы аттрибутов
    integrateAttributesOptimize = pd.read_csv(OptimizeIntegrateAttributesFileName,
                                              sep=sep, decimal=dec)  # Аттрибуты интегирования

    # Вывыдим считанные аттрибуты
    return integrateAttributesOptimize


# Считываем аттрибуты интегрирования
def ReadIndexesGraphics(ProjectsAttributes,  # Аттрибуты проекта

                        # Десятичные разделители
                        sep,  # Разделитель csv
                        dec  # Десятичный разделитель
                        ):
    # Получаем аттрбуты
    IndexesGraphicsFileName = ProjectsAttributes["IndexesGraphicsFileName"]  # Файл csv индексов графиков, которые нужно построить

    # Считываем файлы аттрибутов
    indexesGraphics = pd.read_csv(IndexesGraphicsFileName, sep=sep, decimal=dec)  # Индексы графиков

    # Вывыдим считанные аттрибуты
    return indexesGraphics


# Считываем имя файла динамики
def ReadDynamicFileName(ProjectsAttributes  # Аттрибуты проекта
                        ):
    # Получаем и выводим имя файла динамики
    return ProjectsAttributes["DynamicFileName"]  # Файл csv динамики
