import numpy as np
import pandas as pd

from MathProtEnergyProc.IndexedNames import IndexedNamesFromIndexes

from MathProtEnergyProcSynDatas.File.ReadProjectFileBase import ReadDynamicFileName, ReadIndexesGraphics
from MathProtEnergyProcSynDatas.DatasIndexes import IndexesGraphics

from .GetModelingParameters import GetAttribuesIndexesNames


# Функцтор сохранения динамики в .csv
class DynamicToCSVBase(object):
    # Инициализация класса
    def __init__(self,

                 # Файл CSV
                 DynamicFileNameBase,  # Начало имени
                 sep,  # Сепаратор CSV
                 dec  # Десятичный разделитель
                 ):
        # Заполняем поля
        self.__DynamicFileNameBase = DynamicFileNameBase  # Начало имени
        self.__sep = sep  # Сепаратор CSV
        self.__dec = dec  # Десятичный разделитель

    # Аттррибуты класса
    def GetSep(self):  # Разделитель CSV
        return self.__sep

    def GetDec(self):  # Десятичный разделитель
        return self.__dec

    # Получение имени файла динамики по индексу
    def GetDynFileName(self,

                       index  # Индекс сохраняемой динамики
                       ):
        # Формируем и выводим имя файла
        return IndexedNamesFromIndexes([index],  # Индексы
                                       self.__DynamicFileNameBase,  # Начало имени
                                       endName=".csv",  # Конец имени
                                       sepName="_"  # Разделитель имени
                                       )[0]

    # Получение динамики по индексу
    def GetDynamic(self,

                   index  # Индекс сохраняемой динамики
                   ):
        # Формируем имя файла
        dynamicsFileName = self.GetDynFileName(index)

        # Считываем и возвращаем динамику
        return pd.read_csv(dynamicsFileName,
                           sep=self.__sep,
                           decimal=self.__dec)

    # Функция вызова
    def SaveDynamic(self,

                    dyn,  # Сохраняемая динамика
                    index  # Индекс сохраняемой динамики
                    ):
        # Формируем имя файла
        dynamicsFileName = self.GetDynFileName(index)

        # Формируем фрейм данных
        DynamicDatas = pd.DataFrame(dyn)

        # Сохраняем в csv файл
        DynamicDatas.to_csv(dynamicsFileName,
                            sep=self.__sep,
                            decimal=self.__dec,
                            index=False)

        # Выводим имя файла динамики
        return dynamicsFileName


# Функцтор сохранения динамики в .csv
class DynamicToCSV(DynamicToCSVBase):
    # Инициализация класса
    def __init__(self,

                 ProjectsAttributes,  # Аттрибуты проекта

                 sep,  # Сепаратор CSV
                 dec  # Десятичный разделитель
                 ):
        # Получаем начало имени файла динамики
        DynamicFileNameBase = ReadDynamicFileName(ProjectsAttributes)

        # Инициализируем базовый класс
        super().__init__(DynamicFileNameBase,  # Начало имени

                         sep,  # Сепаратор CSV
                         dec  # Десятичный разделитель
                         )


# Функцтор сохранения динамики в .csv (базовый функтор)
class DynamicToCSVAndPlotBase(DynamicToCSVBase):
    # Инициализация класса
    def __init__(self,

                 nMode,  # Число аттрибутов режима
                 dynamicParametersNDyblicates,  # Число дубликаций динамик с разными параметрами
                 nAttrs,  # Число аттрибутов

                 indexesGraphics,  # Индексы графиков

                 # Файл CSV
                 DynamicFileNameBase,  # Начало имени
                 sep,  # Сепаратор CSV
                 dec  # Десятичный разделитель
                 ):
        # Выполняем базовую инициализацию класса
        super().__init__(DynamicFileNameBase, sep, dec)

        # Получаем индексы графиков
        self.SetIndexesGraphics(nMode,  # Число аттрибутов режима
                                dynamicParametersNDyblicates,  # Число дубликаций динамик с разными параметрами
                                nAttrs,  # Число аттрибутов

                                indexesGraphics  # Индексы графиков
                                )

    # Задание индексов графиков
    def SetIndexesGraphics(self,

                           nMode,  # Число аттрибутов режима
                           dynamicParametersNDyblicates,  # Число дубликаций динамик с разными параметрами
                           nAttrs,  # Число аттрибутов

                           indexesGraphics  # Индексы графиков
                           ):
        # Получаем информацию по индексам аттрибутов
        (arrNamesAllAttrsIndexes,  # Массив заголовков индексов аттрибутов
         arrNAllAttrs  # Массив чисел аттрибутов
         ) = GetAttribuesIndexesNames(nMode,  # Число аттрибутов режима
                                      dynamicParametersNDyblicates,  # Число дубликаций динамик с разными параметрами
                                      nAttrs  # Число аттрибутов
                                      )

        # Формируем индексы динамик, графики которых мы будем строить
        (self.__indexesGraphics,
         self.__buildingGraphics) = IndexesGraphics(indexesGraphics,
                                                    arrNamesAllAttrsIndexes,
                                                    arrNAllAttrs)

    # Проверка возможности построения графиков
    def IsAllowPlot(self, index):
        return (self.__buildingGraphics and np.any(index == self.__indexesGraphics))


# Функцтор сохранения динамики в .csv
class DynamicToCSVAndPlot(DynamicToCSVAndPlotBase):
    # Инициализация класса
    def __init__(self,

                 nMode,  # Число аттрибутов режима
                 dynamicParametersNDyblicates,  # Число дубликаций динамик с разными параметрами
                 nAttrs,  # Число аттрибутов

                 ProjectsAttributes,  # Аттрибуты проекта

                 # Файл CSV
                 sep,  # Сепаратор CSV
                 dec  # Десятичный разделитель
                 ):
        # Получаем начало имени файла динамики
        DynamicFileNameBase = ReadDynamicFileName(ProjectsAttributes)

        # Получаем индексы графиков
        indexesGraphics = ReadIndexesGraphics(ProjectsAttributes, sep, dec)

        # Выполняем базовую инициализацию класса
        super().__init__(nMode,  # Число аттрибутов режима
                         dynamicParametersNDyblicates,  # Число дубликаций динамик с разными параметрами
                         nAttrs,  # Число аттрибутов

                         indexesGraphics,  # Индексы графиков

                         # Файл CSV
                         DynamicFileNameBase,  # Начало имени
                         sep,  # Сепаратор CSV
                         dec  # Десятичный разделитель
                         )
