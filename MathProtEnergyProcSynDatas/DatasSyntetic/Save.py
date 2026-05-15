import numpy as np
import pandas as pd

from MathProtEnergyProc.IndexedNames import IndexedNamesFromIndexes

from MathProtEnergyProcSynDatas.File.ReadProjectFileBase import ReadDynamicFileName


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


# Функция сохранения в файл
def SavedFinction(dyn, index,

                  saveDynamicFun,  # Функтор сохранения динамики
                  buildingGraphics,  # Нужно ли строить график
                  indexesGraphics,  # Индексы графиков

                  outputArrayCreate  # Функция создания выходного массива
                  ):
    # Индекс
    index += 1

    # Сохраняем данные в файл
    BuildGraphic = (buildingGraphics and np.any(index == indexesGraphics))  # Необходимость построения графика
    outputArrayCreate(dyn, index, saveDynamicFun, plotGraphics=BuildGraphic)

    # Возвращаем индекс
    return index
