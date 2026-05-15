import numpy as np


# Гененрируем локально-равномерно распределенные величины
def GenerateRandomDatasInDiapasons(minValues,  # Минимальные значения величин
                                   maxValues,  # Максимальные значения величин
                                   nPoints=1  # Числа точек в соответствующих диапазонах
                                   ):  # Конкатенация с размножением двух матриц
    # Матрицы максимальных и минимальных величин приводим к массиву numpy
    aMinValues = np.array(minValues)  # Минимальные значения величин
    aMaxValues = np.array(maxValues)  # Максимальные значения величин

    # Получаем матрицу приращений
    deltaValues = aMaxValues - aMinValues

    # Приодим минимальные величины и матрицу приращений в соответсвие с индексами
    aMinValues = np.repeat(aMinValues, nPoints, axis=0)  # Минимальные величины
    deltaValues = np.repeat(deltaValues, nPoints, axis=0)  # Приращения величин

    # Получаем случайные величины
    (nRows, nColumns) = aMinValues.shape  # Число рядов и колонок
    return aMinValues + deltaValues * np.random.rand(nRows, nColumns)  # Случайные числа
