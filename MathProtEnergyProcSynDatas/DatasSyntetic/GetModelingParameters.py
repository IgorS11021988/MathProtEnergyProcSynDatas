from MathProtEnergyProcSynDatas.DatasIntegrate import ConcatModelingParameters, IntegrateAttributes


# Определяем полное число динамик
def GetNDynamics(attributesNPoints,  # Число точек аттрибутов
                 nModes,  # Число режимов работы
                 dynamicParametersNDyblicates,  # Число состояний, определяющих конкретную динамику
                 ):
    # Получаем и выводим результат
    return nModes * dynamicParametersNDyblicates * attributesNPoints


# Функция индксов аттрибутов
def GetAttribuesIndexesNames(nMode,  # Число аттрибутов режима
                             dynamicParametersNDyblicates,  # Число дубликаций динамик с разными параметрами
                             nAttrs  # Число аттрибутов
                             ):
    # Массив заголовков индексов аттрибутов
    arrNamesAllAttrsIndexes = ["indexMode", "indexDynamicParameters", "indexParameters"]

    # Массив чисел аттрибутов
    arrNAllAttrs = [nMode, dynamicParametersNDyblicates, nAttrs]

    # Выводим массивы
    return (arrNamesAllAttrsIndexes,  # Массив заголовков индексов аттрибутов
            arrNAllAttrs  # Массив чисел аттрибутов
            )


# Считывание файла проекта для моделирования
def GetModelingParameters(modeAttributes,  # Аттрибуты режима
                          dynamicParameters,  # Начальное состояние
                          attributes,  # Аттрибуты

                          nMode,  # Число аттрибутов режима
                          dynamicParametersNDyblicates,  # Число дубликаций динамик с разными параметрами
                          nAttrs,  # Число аттрибутов

                          integrateAttributes  # Аттрибуты интегрирования
                          ):
    # Размножаем параметры
    Pars = ConcatModelingParameters(modeAttributes,  # Аттрибуты режима
                                    dynamicParameters,  # Начальное состояние
                                    attributes,  # Аттрибуты
                                    dynamicParametersNDyblicates  # Число дубликаций динамик с разными параметрами
                                    )

    # Получаем числа аттрибутов
    nDyns = len(Pars)  # Число динамик

    # Получаем информацию по индексам аттрибутов
    (arrNamesAllAttrsIndexes,  # Массив заголовков индексов аттрибутов
     arrNAllAttrs  # Массив чисел аттрибутов
     ) = GetAttribuesIndexesNames(nMode,  # Число аттрибутов режима
                                  dynamicParametersNDyblicates,  # Число дубликаций динамик с разными параметрами
                                  nAttrs  # Число аттрибутов
                                  )

    # Вычисляем аттрибуты интегрирования
    integrateAttributes = IntegrateAttributes(integrateAttributes,
                                              arrNamesAllAttrsIndexes,
                                              arrNAllAttrs,
                                              nDyns)  # Приравниваем базовые аттрибуты интегрирования

    # Вцыводим результат
    return (Pars,  # Параметры

            # Параметры интегрирования
            integrateAttributes  # Аттрибуты интегрирования
            )
