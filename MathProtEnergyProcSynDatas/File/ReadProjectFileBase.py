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
    # Имна файлов
    ModeAttributesFileName = ProjectsAttributes["ModeAttributesFileName"]  # Файл csv аттрибутов режима

    # Считываем файл аттрибутов режима и выводим эти аттрибуты
    return pd.read_csv(ModeAttributesFileName, sep=sep, decimal=dec)


# Считываем файл границ аттрибутов
def ReadAttributesBorders(ProjectsAttributes,  # Аттрибуты проекта

                          # Десятичные разделители
                          sep,  # Разделитель csv
                          dec  # Десятичный разделитель
                          ):
    # Получаем аттрбуты
    AttributesBorderFileName = ProjectsAttributes["AttributesBorderFileName"]  # Файл csv границ аттрибутов
    attributesNPoints = ProjectsAttributes["AttributesNPoints"]  # Число точек аттрибутов

    # Считываем файлы границ
    attributesBorder = pd.read_csv(AttributesBorderFileName, sep=sep, decimal=dec)  # Границы аттрибутов

    # Выводим результат
    return (attributesBorder,  # Границы аттрибутов

            attributesNPoints  # Число генерируемых точек аттрибутов
            )
