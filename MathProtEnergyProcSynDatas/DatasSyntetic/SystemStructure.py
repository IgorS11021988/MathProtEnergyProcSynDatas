from MathProtEnergyProc import (
    NonEqSystemQ,
    NonEqSystem,
    NonEqSystemQDyn,
    NonEqSystemDyn,
    CountDynamics,
    CountDynamicsQ
)


# Функция сохранения в файл
def _SavedFinction(dyn, index,

                   saveDynamicFun,  # Функтор сохранения динамики

                   outputArrayCreate  # Функция создания выходного массива
                   ):
    # Индекс
    index += 1

    # Сохраняем данные в файл
    outputArrayCreate(dyn, index, saveDynamicFun)

    # Возвращаем индекс
    return index


# Функция структуры системы для моделирования ее динамики (термодинамический подход)
def SystemStructureQ(structureFunctionQ,  # Функция структуры системы
                     constParametersFunctionQ,  # Функция постоянных параметров системы
                     characteristicsFunction,  # Функция характеристик системы
                     conditionsFunction,  # Функция условий протекания процессов

                     integDynamic,  # Метод интегрирования динамики

                     # Функции обработки
                     outputArrayCreate,  # Функция постобработки выходных данных

                     # Имя функции сохранения динамики
                     saveDynamicFun  # Функтор сохранения динамики
                     ):  # Структура для расчета одной динамики
    # Описываем структуру литий-ионного элемента
    strSys = structureFunctionQ()

    # Класс системы
    sysStructureQ = NonEqSystemQ(*strSys)

    # Задаем постоянные параметры системы
    constParametersFunctionQ(sysStructureQ)

    # Функция сохранения выходных параметров
    def savedFinction(dyn, index):
        # Сохраняем в файл и возвращаем индекс
        return _SavedFinction(dyn, index,

                              saveDynamicFun,  # Функтор сохранения динамики

                              outputArrayCreate  # Функция создания выходного массива
                              )

    # Задаем и возвращаем класс динамики системы
    sysDyn = NonEqSystemQDyn(sysStructureQ,  # Система
                             conditionsFunction,  # Функция условий протекания процессов
                             characteristicsFunction,  # Функция внешних параметров
                             integDynamic  # Метод интегрирования дифференциальных уравнений
                             )
    return CountDynamicsQ(sysDyn, savedFinction)


# Функция структуры системы для моделирования ее динамики (общеэнергетический подход)
def SystemStructure(structureFunction,  # Функция структуры системы
                    constParametersFunction,  # Функция постоянных параметров системы
                    characteristicsFunction,  # Функция характеристик системы
                    conditionsFunction,  # Функция условий протекания процессов

                    integDynamic,  # Метод интегрирования динамики

                    # Функции обработки
                    outputArrayCreate,  # Функция постобработки выходных данных

                    # Имя функции сохранения динамики
                    saveDynamicFun  # Функтор сохранения динамики
                    ):  # Структура для расчета одной динамики
    # Описываем структуру литий-ионного элемента
    strSys = structureFunction()

    # Класс системы
    sysStructure = NonEqSystem(*strSys)

    # Задаем постоянные параметры системы
    constParametersFunction(sysStructure)

    # Функция сохранения выходных параметров
    def savedFinction(dyn, index):
        # Сохраняем в файл и возвращаем индекс
        return _SavedFinction(dyn, index,

                              saveDynamicFun,  # Функтор сохранения динамики

                              outputArrayCreate  # Функция создания выходного массива
                              )

    # Задаем и возвращаем класс динамики системы
    sysDyn = NonEqSystemDyn(sysStructure,  # Система
                            conditionsFunction,  # Функция условий протекания процессов
                            characteristicsFunction,  # Функция внешних параметров
                            integDynamic  # Метод интегрирования дифференциальных уравнений
                            )
    return CountDynamics(sysDyn, savedFinction)
