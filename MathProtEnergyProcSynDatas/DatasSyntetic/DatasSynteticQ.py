from MathProtEnergyProcSynDatas.File import ParametersSave, ReadProjectFileForModeling

from MathProtEnergyProcSynDatas.SystemStructure import SystemStructureQ

from MathProtEnergyProc import CountDynamicsQ

from .Save import SavedFinction

from pandas import DataFrame


# Функция расчета динамик (термодинамический подход)
def SystemDynamicsFunctionQ(Pars,  # Параметры

                            # Параметры интегрирования
                            integrateAttributes,  # Аттрибуты интегрирования

                            # Класс системы
                            sysDyn,  # Динамики системы

                            # Функции обработки
                            inputArrayCreateQ,  # Функция предобработки входных данных
                            outputArrayCreate,  # Функция постобработки выходных данных

                            # Построение графиков
                            indexesGraphics,  # Индексы графиков, которые нужно построить
                            buildingGraphics,  # Необходимость построения графиков

                            # Имя файла
                            DynamicFileNameBase,  # Базовое имя файла csv
                            sep,  # Разделитель csv
                            dec  # Десятичный разделитель
                            ):
    # Исходные данные моделирования системы
    (Tints,
     stateCoordinates0s,
     reducedTemp0s,
     systemParameters,
     ts) = inputArrayCreateQ(Pars,  # Параметры

                             integrateAttributes  # Аттрибуты интегрирования
                             )

    # Функция сохранения в файл
    def savedFinction(dyn, index):
        # Сохраняем в файл и возвращаем индекс
        return SavedFinction(dyn, index,
                             DynamicFileNameBase,  # основа имени файла динамики
                             buildingGraphics,  # Нужно ли строить график
                             indexesGraphics,  # Индексы графиков

                             outputArrayCreate,  # Функция создания выходного массива

                             sep, dec  # Разделители
                             )

    # Задаем класс динамик системы
    sysDyns = CountDynamicsQ(sysDyn, savedFinction)

    # Моделируем динамики
    indexes = sysDyns.ComputingExperimentQ(Tints,
                                           stateCoordinates0s,
                                           reducedTemp0s,
                                           systemParameters,
                                           t_evals=ts)  # Индекс динамики начинается с единицы

    # Выводим результат
    return DataFrame({"dynamicIndex": indexes.reshape(-1,)})


# Моделирование динамик системы (термодинамический подход)
def SystemDynamicsModelingQ(ProjectFileName,  # Имя файла проекта

                            # Функция класса системы
                            structureFunctionQ,  # Функция структуры системы
                            constParametersFunctionQ,  # Функция постоянных параметров системы
                            characteristicsFunction,  # Функция характеристик системы
                            conditionsFunction,  # Функция условий протекания процессов
                            integDynamicClass,  # Метод интегрирования динамики

                            # Функции обработки
                            inputArrayCreateQ,  # Функция предобработки входных данных
                            outputArrayCreate  # Функция постобработки выходных данных
                            ):
    # Считываем файл проекта
    (Pars,  # Параметры

     # Параметры интегрирования
     integrateAttributes,  # Аттрибуты интегрирования
     integrateMethod,  # Метод интегрирования дифференциальных уравнений

     # Построение графиков
     indexesGraphics,  # Индексы графиков, которые нужно построить
     buildingGraphics,  # Необходимость построения графиков

     # Имя файла динамики
     DynamicFileName,  # Файл csv

     # Имя файла параметров
     ParametersFileName,

     sep,  # Разделитель csv
     dec  # Десятичный разделитель
     ) = ReadProjectFileForModeling(ProjectFileName)

    # Динамика системы
    integDynamic = integDynamicClass(method=integrateMethod)  # Интегратор динамики
    sysDyn = SystemStructureQ(structureFunctionQ,  # Функция структуры системы
                              constParametersFunctionQ,  # Функция постоянных параметров системы
                              characteristicsFunction,  # Функция характеристик системы
                              conditionsFunction,  # Функция условий протекания процессов

                              integDynamic  # Метод интегрирования динамики
                              )

    # Выполняем моделирование динамики системы
    dynamicIndex = SystemDynamicsFunctionQ(Pars,  # Параметры

                                           # Параметры интегрирования
                                           integrateAttributes,  # Аттрибуты интегрирования

                                           # Динамика системы
                                           sysDyn,

                                           # Функции обработки
                                           inputArrayCreateQ,  # Функция предобработки входных данных
                                           outputArrayCreate,  # Функция постобработки выходных данных

                                           # Построение графиков
                                           indexesGraphics,  # Индексы графиков, которые нужно построить
                                           buildingGraphics,  # Необходимость построения графиков

                                           # Имя файла динамики
                                           DynamicFileName,  # Файл csv
                                           sep,  # Разделитель csv
                                           dec  # Десятичный разделитель
                                           )

    # Сохраняем параметры
    ParametersSave(dynamicIndex,  # Индексы динамик
                   Pars,  # Параметры
                   ParametersFileName,  # Имя файла параметров
                   sep,  # CSV разделитель
                   dec  # Десятичный разделитель
                   )
