from MathProtEnergyProc import NonEqSystemQ, NonEqSystem, NonEqSystemQDyn, NonEqSystemDyn


# Функция структуры системы для моделирования ее динамики (термодинамический подход)
def SystemStructureQ(structureFunctionQ,  # Функция структуры системы
                     constParametersFunctionQ,  # Функция постоянных параметров системы
                     characteristicsFunction,  # Функция характеристик системы
                     conditionsFunction,  # Функция условий протекания процессов

                     integDynamic  # Метод интегрирования динамики
                     ):  # Структура для расчета одной динамики
    # Описываем структуру литий-ионного элемента
    strSys = structureFunctionQ()

    # Класс системы
    sysStructureQ = NonEqSystemQ(*strSys)

    # Задаем постоянные параметры системы
    constParametersFunctionQ(sysStructureQ)

    # Задаем класс динамики системы
    return NonEqSystemQDyn(sysStructureQ,  # Система
                           conditionsFunction,  # Функция условий протекания процессов
                           characteristicsFunction,  # Функция внешних параметров
                           integDynamic  # Метод интегрирования дифференциальных уравнений
                           )


# Функция структуры системы для моделирования ее динамики (общеэнергетический подход)
def SystemStructure(structureFunction,  # Функция структуры системы
                    constParametersFunction,  # Функция постоянных параметров системы
                    characteristicsFunction,  # Функция характеристик системы
                    conditionsFunction,  # Функция условий протекания процессов

                    integDynamic  # Метод интегрирования динамики
                    ):  # Структура для расчета одной динамики
    # Описываем структуру литий-ионного элемента
    strSys = structureFunction()

    # Класс системы
    sysStructure = NonEqSystem(*strSys)

    # Задаем постоянные параметры системы
    constParametersFunction(sysStructure)

    # Задаем класс динамики системы
    return NonEqSystemDyn(sysStructure,  # Система
                          conditionsFunction,  # Функция условий протекания процессов
                          characteristicsFunction,  # Функция внешних параметров
                          integDynamic  # Метод интегрирования дифференциальных уравнений
                          )
