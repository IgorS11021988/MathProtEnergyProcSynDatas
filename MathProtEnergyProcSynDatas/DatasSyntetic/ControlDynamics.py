from MathProtEnergyProcSynDatas.File import ReadProjectFileForSelectControlDynamics

from pandas import DataFrame, concat

import numpy as np


# Выделяем контрольные динамики
def SelectControlDynamics(controlDynamicIndexes,  # Индексы контрольных динамик
                          controlDynamicNames,  # Имена контрольных динамик
                          nModes,  # Число режимов
                          parameters,  # Параметры, полученные в результате эксперимента

                          needRepeat=False  # Нужно ли повторять контрольные динамики
                          ):
    # Получаем индексы динамик
    dynamicIndexes = parameters["dynamicIndex"].to_numpy()

    # Приводим динамики к матрице и выделяем контрольные динамики
    dynamicIndexes.shape = (-1, nModes)  # Приводим к матрице, столбцами которой являются разные режимы работы системы
    aControlDynamicIndexes = np.array(controlDynamicIndexes) - 1  # Приводим индексы контрольных динамик к индексации numpy
    controlDynamicIndexesMatrix = dynamicIndexes[:, aControlDynamicIndexes]  # Получаем индексы контрольных динамик
    if needRepeat:
        controlDynamicIndexesMatrix = np.repeat(controlDynamicIndexesMatrix, nModes, axis=0)  # Повторяем элементы массива индексов контрольных динамик

    # Упаковываем в pandas
    return DataFrame(controlDynamicIndexesMatrix,
                     columns=controlDynamicNames)


# Конкатенуем контрольные динамики
def ConcatControlDynamics(controlDynamicIndexes,  # Индексы контрольных динамик
                          controlDynamicNames,  # Имена контрольных динамик
                          modeAttributes,  # Аттрибуты режимов
                          parameters,  # Параметры, полученные в результате эксперимента

                          deletingParameters=False  # Удаляем параметры
                          ):
    # Число аттрибутов режима
    nModes = len(modeAttributes)

    # Получаем контрольные динамики
    pControlDynamicIndexesMatrix = SelectControlDynamics(controlDynamicIndexes,  # Индексы контрольных динамик
                                                         controlDynamicNames,  # Имена контрольных динамик
                                                         nModes,  # Число режимов
                                                         parameters,  # Параметры, полученные в результате эксперимента

                                                         needRepeat=True  # Нужно ли повторять контрольные динамики
                                                         )

    # Конкатенуем данные
    parametersExt = concat([parameters, pControlDynamicIndexesMatrix], axis=1)  # Конкатенованные параметры
    if deletingParameters:  # Удаляем при необходимости лишнее
        modeAttributesNames = list(modeAttributes)  # Заголовки аттрибутов режима

        return parametersExt[["dynamicIndex"] + controlDynamicNames + modeAttributesNames]
    else:
        return parametersExt


# Функция конкатенации контрольных динамик в файл результатов
def ConcatenateControlDynamics(ProjectFileName,  # Имя файла проекта

                               controlDynamicIndexes,  # Индексы контрольных динамик
                               controlDynamicNames,  # Имена контрольных динамик

                               deletingParameters=False  # Удаляем параметры
                               ):
    # Считываем файл проекта
    (modeAttributes,  # Аттрибуты режима
     parameters,  # Параметры
     sep,  # Разделитель csv
     dec,  # Десятичный разделитель

     ControlDynamicsFileName  # Имя файла csv параметров с контролтными динамиками
     ) = ReadProjectFileForSelectControlDynamics(ProjectFileName  # Имя файла проекта
                                                 )

    # Получаем конкатенованные параметры
    parametersExt = ConcatControlDynamics(controlDynamicIndexes,  # Индексы контрольных динамик
                                          controlDynamicNames,  # Имена контрольных динамик
                                          modeAttributes,  # Аттрибуты режимов
                                          parameters,  # Параметры, полученные в результате эксперимента

                                          deletingParameters=deletingParameters  # Удаляем параметры
                                          )

    # Сохраняем в файл
    parametersExt.to_csv(ControlDynamicsFileName,
                         sep=sep, decimal=dec,
                         index=False)
