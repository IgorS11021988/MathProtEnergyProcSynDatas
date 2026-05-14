import numpy as np

from MathProtEnergyProc.IndexedNames import IndexedNamesFromIndexes

from MathProtEnergyProcSynDatas.File.Save import DynamicSave


# Функцтор сохранения динамики в .csv
class GetDynamicToCSVFileName(object):
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

    # Функция вызова
    def __call__(self,

                 dyn,  # Сохраняемая динамика
                 index  # Индекс сохраняемой динамики
                 ):
        # Формируем имя файла
        dynamicsFileName = IndexedNamesFromIndexes([index],  # Индексы
                                                   self.__DynamicFileNameBase,  # Начало имени
                                                   endName=".csv",  # Конец имени
                                                   sepName="_"  # Разделитель имени
                                                   )[0]

        # Сохраняем динамику в файл
        DynamicSave(dyn,  # Словарь динамик с заголовками
                    dynamicsFileName,  # Имя файла динамик

                    self.__sep,    # Разделитель .csv
                    self.__dec  # Десятичный разделитель
                    )

        # Выводим имя файла динамики
        return dynamicsFileName


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
