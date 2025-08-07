import numpy as np


# Функция линейных моментов времени
def LinearTimesMoments(Tints,  # Времена интегрирования
                       NPoints,  # Числа точек интегрирования

                       tBegins=None  # Начальные моменты времени
                       ):
    # Начальные моменты времени интегрирования
    if tBegins is None:
        tBegins = np.zeros_like(Tints)

    # Конечные моменты времени интегрирования
    tEnds = tBegins + Tints

    # Векторизуемая функция временных диапазонов
    def FunTs(ind):
        return np.linspace(tBegins[ind], tEnds[ind], NPoints[ind])

    # Формируем список массивов времен интегрирования
    nListIntegrateTimes = len(Tints)  # Число элементов списка времен интегрирования
    inds = np.arange(nListIntegrateTimes, dtype=np.int64)  # Массив индексов
    vecFunTs = np.vectorize(FunTs, otypes=[np.ndarray])  # Векторизованная функция временных сеток
    ts = vecFunTs(inds)  # Получаем список сеток

    # Выводим список массивов времен интегрирования
    return ts
