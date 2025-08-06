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

    # Формируем список массивов времен интегрирования
    nListIntegrateTimes = len(Tints)  # Число элементов списка времен интегрирования
    ts = []
    for ind in range(nListIntegrateTimes):
        ts.append(np.linspace(tBegins[ind], tEnds[ind], NPoints[ind]))

    # Выводим список массивов времен интегрирования
    return ts
