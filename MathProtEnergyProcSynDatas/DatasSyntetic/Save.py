from MathProtEnergyProc.IndexedNames import IndexedNamesFromIndexes

import numpy as np


# Функция сохранения в файл
def SavedFinction(dyn, index,
                  DynamicFileNameBase,  # основа имени файла динамики
                  buildingGraphics,  # Нужно ли строить график
                  indexesGraphics,  # Индексы графиков

                  outputArrayCreate,  # Функция создания выходного массива

                  sep, dec  # Разделители
                  ):
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

    # Возвращаем индекс
    return index
