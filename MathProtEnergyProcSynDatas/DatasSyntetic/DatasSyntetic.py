from MathProtEnergyProcSynDatas.File import ReadProjectFileForModeling

from MathProtEnergyProcSynDatas.SystemStructure import SystemStructure

from MathProtEnergyProc import CountDynamics

from .GetModelingParameters import GetModelingParameters
from .Save import SavedFinction, GetDynamicToCSVFileName

from pandas import DataFrame, concat


# Моделирование динамик системы (термодинамический подход)
def SystemDynamicsModelingBase(modeAttributes,  # Аттрибуты режима
                               dynamicParameters,  # Начальное состояние
                               attributes,  # Аттрибуты
                               dynamicParametersNDyblicates,  # Число дубликаций динамик с разными параметрами

                               # Интегрирование
                               integDynamic,  # Интегратор динамики
                               integrateAttributes,  # Аттрибуты интегрирования

                               # Функция класса системы
                               structureFunction,  # Функция структуры системы
                               constParametersFunction,  # Функция постоянных параметров системы
                               characteristicsFunction,  # Функция характеристик системы
                               conditionsFunction,  # Функция условий протекания процессов

                               # Функции обработки
                               inputArrayCreate,  # Функция предобработки входных данных
                               outputArrayCreate,  # Функция постобработки выходных данных

                               # Графики
                               indexesGraphics,  # Индексы графиков

                               # Имя функции сохранения динамики
                               saveDynamicFun  # Функтор сохранения динамики
                               ):
    # Получаем параметры моделировния
    (Pars,  # Параметры

     # Параметры интегрирования
     integrateAttributes,  # Аттрибуты интегрирования

     # Построение графиков
     indexesGraphics,  # Индексы графиков, которые нужно построить
     buildingGraphics  # Необходимость построения графиков
     ) = GetModelingParameters(modeAttributes,  # Аттрибуты режима
                               dynamicParameters,  # Начальное состояние
                               attributes,  # Аттрибуты
                               dynamicParametersNDyblicates,  # Число дубликаций динамик с разными параметрами

                               integrateAttributes,  # Прочие аттрибуты интегрирования

                               indexesGraphics  # Индексы графиков
                               )

    # Исходные данные моделирования системы
    (Tints,
     stateCoordinates0s,
     systemParameters,
     ts) = inputArrayCreate(Pars,  # Параметры

                            integrateAttributes  # Аттрибуты интегрирования
                            )

    # Функция сохранения в файл
    def savedFinction(dyn, index):
        # Сохраняем в файл и возвращаем индекс
        return SavedFinction(dyn, index,

                             saveDynamicFun,  # Функтор сохранения динамики
                             buildingGraphics,  # Нужно ли строить график
                             indexesGraphics,  # Индексы графиков

                             outputArrayCreate  # Функция создания выходного массива
                             )

    # Динамика системы
    sysDyn = SystemStructure(structureFunction,  # Функция структуры системы
                             constParametersFunction,  # Функция постоянных параметров системы
                             characteristicsFunction,  # Функция характеристик системы
                             conditionsFunction,  # Функция условий протекания процессов

                             integDynamic  # Метод интегрирования динамики
                             )
    sysDyns = CountDynamics(sysDyn, savedFinction)  # Класс динамик системы

    # Моделируем динамики
    indexes = sysDyns.ComputingExperiment(Tints,
                                          stateCoordinates0s,
                                          systemParameters,
                                          t_evals=ts)  # Индекс динамики начинается с единицы

    # Выводим результат
    return concat([Pars,
                   DataFrame({"dynamicIndex": indexes.reshape(-1,)})],
                  axis=1)


# Моделирование динамик системы (термодинамический подход)
def SystemDynamicsModeling(ProjectFileName,  # Имя файла проекта

                           # Функция класса системы
                           structureFunction,  # Функция структуры системы
                           constParametersFunction,  # Функция постоянных параметров системы
                           characteristicsFunction,  # Функция характеристик системы
                           conditionsFunction,  # Функция условий протекания процессов
                           integDynamic,  # Интегратор динамики

                           # Функции обработки
                           inputArrayCreate,  # Функция предобработки входных данных
                           outputArrayCreate  # Функция постобработки выходных данных
                           ):
    # Считываем файл проекта
    (integrateAttributes,  # Аттрибуты интегрирования

     # Построение графиков
     indexesGraphics,  # Индексы графиков, которые нужно построить

     # Моделирование системы
     modeAttributes,  # Аттрибуты режима
     dynamicParameters,  # Начальное состояние
     attributes,  # Аттрибуты
     dynamicParametersNDyblicates,  # Число дубликаций динамик с разными параметрами

     # Имя файла динамики
     DynamicFileNameBase,  # Файл csv

     # Имя файла параметров
     ParametersFileName,

     sep,  # Разделитель csv
     dec  # Десятичный разделитель
     ) = ReadProjectFileForModeling(ProjectFileName)

    # Получаем динамики системы
    getDynamicToCSVFileName = GetDynamicToCSVFileName(DynamicFileNameBase,  # Файл csv

                                                      sep,  # Разделитель csv
                                                      dec  # Десятичный разделитель
                                                      )
    allPars = SystemDynamicsModelingBase(modeAttributes,  # Аттрибуты режима
                                         dynamicParameters,  # Начальное состояние
                                         attributes,  # Аттрибуты
                                         dynamicParametersNDyblicates,  # Число дубликаций динамик с разными параметрами

                                         # Интегрирование
                                         integDynamic,  # Интегратор динамики
                                         integrateAttributes,  # Прочие аттрибуты интегрирования

                                         # Функция класса системы
                                         structureFunction,  # Функция структуры системы
                                         constParametersFunction,  # Функция постоянных параметров системы
                                         characteristicsFunction,  # Функция характеристик системы
                                         conditionsFunction,  # Функция условий протекания процессов

                                         # Функции обработки
                                         inputArrayCreate,  # Функция предобработки входных данных
                                         outputArrayCreate,  # Функция постобработки выходных данных

                                         # Графики
                                         indexesGraphics,  # Индексы графиков

                                         # Имя файла динамики
                                         getDynamicToCSVFileName  # Функтор сохранения динамики
                                         )

    # Сохраняем параметры
    allPars.to_csv(ParametersFileName,
                   sep=sep, decimal=dec,
                   index=False)
