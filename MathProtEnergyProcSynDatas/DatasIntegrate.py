import numpy as np
from pandas import DataFrame

from MathProtEnergyProc.DatasIntegration import HStackMatrixRepeat

from .DatasIndexes import GenIndex, SelectNonZeroIndexes


# Получаем фрейм параметров
def ConcatModelingParameters(modeAttributes,  # Аттрибуты режима
                             dynamicParameters,  # Параметры динамики
                             attributes,  # Аттрибуты
                             dynamicParametersNDyblicates  # Число дубликаций динамик с разными параметрами
                             ):
    # Заголовки данных
    attributesName = list(attributes)  # Имена аттрибутов
    dynamicParametersName = list(dynamicParameters)  # Имена начального состояния
    modeAttributesName = list(modeAttributes)  # Имена аттрибутов тока

    # Размножаем параметры
    Pars = HStackMatrixRepeat([attributes.to_numpy(), dynamicParameters.loc[0:(dynamicParametersNDyblicates - 1)].to_numpy(), modeAttributes.to_numpy()],
                              True)
    Pars = DataFrame(Pars, columns=attributesName + dynamicParametersName + modeAttributesName)
    Pars[dynamicParametersName] = dynamicParameters.to_numpy()

    # Выводим параметры
    return Pars


# Аттрибуты интегрирования
def IntegrateAttributes(integrateAttributes,  # Аттрибуты интегрирования
                        arrNamesAllAttrsIndexes,  # Массив имен всех аттрибутов
                        arrNAllAttrs,  # Массив чисел всех аттрибутов
                        nDyns  # Число динамик
                        ):
    # Выделяем прочие аттрибуты
    (bIntegrateAttributesOther,
     isIntegrateAttributesOther,
     integrateAttributesOther) = SelectNonZeroIndexes(integrateAttributes,
                                                      arrNamesAllAttrsIndexes
                                                      )

    # Выделяем базовые аттрибуты интегрирования
    integrateAttributesBase = integrateAttributes.loc[np.logical_not(bIntegrateAttributesOther)].loc[0]

    # Формируем аттрибуты интегрирования
    integrateAttributes = DataFrame(np.full((nDyns, len(list(integrateAttributes))), integrateAttributesBase.to_numpy()),
                                    columns=list(integrateAttributes))  # Приравниваем базовые аттрибуты интегрирования
    if isIntegrateAttributesOther:
        indIntegrateAttributesOther = GenIndex(integrateAttributesOther,
                                               arrNamesAllAttrsIndexes,
                                               arrNAllAttrs)  # Инденсы прочих аттрибутов интегрирования
        integrateAttributes.loc[indIntegrateAttributesOther] = integrateAttributesOther.to_numpy()  # Приравниваем прочие аттрибуты интегрирования

    # Возвращаем аттрибуты интегрирования
    return integrateAttributes
