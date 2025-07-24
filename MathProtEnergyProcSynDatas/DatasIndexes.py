import numpy as np


# Формирование индекса из мультииндекса
def GenIndex(MulIndex,  # Множественный индекс
             selNames,  # Выбираемые имена
             nIndexes  # Количества индексов
             ):
    # Выделяем мультииндексы
    rMulIndex = MulIndex[selNames].to_numpy()

    # Приводим количества индексов
    aNIndexes = np.array(np.hstack([[1], nIndexes]), dtype=np.int32)  # Приводим к массиву
    NIndexes = np.cumprod(aNIndexes[0:-1], dtype=np.int32).reshape(-1, 1)  # Получаем массив произведений

    # Удаляем индексы, большие соответсвующих чисел индексов
    bMoreRMulIndex = np.all((rMulIndex <= aNIndexes[1::]), axis=1)
    rMulIndex = rMulIndex[bMoreRMulIndex]

    # Вычисляем индекс
    return np.dot((rMulIndex - 1), NIndexes).reshape(-1,)


# Выделение ненулевых индексов
def SelectNonZeroIndexes(MulIndex,  # Множественный индекс
                         selNames  # Выбираемые имена
                         ):
    # Выделяем мультииндексы
    rMulIndex = MulIndex[selNames].to_numpy()

    # Логические индексы ненулевых мультииндексов
    bNonZeroMultiIndex = (np.prod(rMulIndex, axis=1) > 0)

    # Факт наличия ненулевого мультииндекса
    isNonZeroMultiIndex = np.any(bNonZeroMultiIndex)

    # Выделяем ненулевые мультииндексы
    NonZeroMultiIndexes = MulIndex.loc[bNonZeroMultiIndex]

    # Выводим результат
    return (bNonZeroMultiIndex, isNonZeroMultiIndex, NonZeroMultiIndexes)


# Индексы для построения графиков
def IndexesGraphics(indexesGraphics,  # Составные индексы рафиков, которые нужно отобразить
                    arrNamesAllAttrsIndexes,  # Массив имен всех аттрибутов
                    arrNAllAttrs  # Массив чисел всех аттрибутов
                    ):
    # Выделяем индексы для построения графиков
    (bBuildGraphicsIndexes,
     isBuildGraphicsIndexes,
     buildGraphicsIndexes) = SelectNonZeroIndexes(indexesGraphics,
                                                  arrNamesAllAttrsIndexes
                                                  )
    if isBuildGraphicsIndexes:
        # Формируем индексы графиков для построения
        buildGraphicsIndexes = GenIndex(buildGraphicsIndexes,
                                        arrNamesAllAttrsIndexes,
                                        arrNAllAttrs) + 1  # Индексы графиков для построения

    # Выводим результат
    return (buildGraphicsIndexes, isBuildGraphicsIndexes)
