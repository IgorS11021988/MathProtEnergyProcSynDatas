from MathProtEnergyProcSynDatas.DatasIndexes import IndexesGraphics
from MathProtEnergyProcSynDatas.DatasIntegrate import ConcatModelingParameters, IntegrateAttributes


# Определяем полное число динамик
def GetNDynamics(attributesNPoints,  # Число точек аттрибутов
                 nModes,  # Число режимов работы
                 dynamicParametersNDyblicates,  # Число состояний, определяющих конкретную динамику
                 ):
    # Получаем и выводим результат
    return nModes * dynamicParametersNDyblicates * attributesNPoints


# Считывание файла проекта для моделирования
def GetModelingParameters(modeAttributes,  # Аттрибуты режима
                          dynamicParameters,  # Начальное состояние
                          attributes,  # Аттрибуты
                          dynamicParametersNDyblicates,  # Число дубликаций динамик с разными параметрами

                          integrateAttributes,  # Аттрибуты интегрирования

                          indexesGraphics  # Индексы графиков
                          ):
    # Размножаем параметры
    Pars = ConcatModelingParameters(modeAttributes,  # Аттрибуты режима
                                    dynamicParameters,  # Начальное состояние
                                    attributes,  # Аттрибуты
                                    dynamicParametersNDyblicates  # Число дубликаций динамик с разными параметрами
                                    )

    # Получаем числа аттрибутов
    nDyns = len(Pars)  # Число динамик
    nAttrs = len(attributes)  # Число аттрибутов аккумулятора
    nMode = len(modeAttributes)  # Число аттрибутов режима

    # Массив заголовков индексов аттрибутов
    arrNamesAllAttrsIndexes = ["indexMode", "indexDynamicParameters", "indexParameters"]

    # Массив чисел аттрибутов
    arrNAllAttrs = [nMode, dynamicParametersNDyblicates, nAttrs]

    # Вычисляем аттрибуты интегрирования
    integrateAttributes = IntegrateAttributes(integrateAttributes,
                                              arrNamesAllAttrsIndexes,
                                              arrNAllAttrs,
                                              nDyns)  # Приравниваем базовые аттрибуты интегрирования

    # Формируем индексы динамик, графики которых мы будем строить
    (indexesGraphics, buildingGraphics) = IndexesGraphics(indexesGraphics,
                                                          arrNamesAllAttrsIndexes,
                                                          arrNAllAttrs)

    # Вцыводим результат
    return (Pars,  # Параметры

            # Параметры интегрирования
            integrateAttributes,  # Аттрибуты интегрирования

            # Построение графиков
            indexesGraphics,  # Индексы графиков, которые нужно построить
            buildingGraphics  # Необходимость построения графиков
            )
