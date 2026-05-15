from MathProtEnergyProcSynDatas.File import ReadProjectFileForModeling

from MathProtEnergyProcSynDatas.SystemStructure import SystemStructureQ

from MathProtEnergyProc import CountDynamicsQ

from .GetModelingParameters import GetModelingParameters
from .Save import SavedFinction, DynamicToCSVAndPlot

from pandas import DataFrame, concat


# Моделирование динамик системы (термодинамический подход)
def SystemDynamicsModelingBaseQ(modeAttributes,  # Аттрибуты режима
                                dynamicParameters,  # Начальное состояние
                                attributes,  # Аттрибуты

                                nMode,  # Число аттрибутов режима
                                dynamicParametersNDyblicates,  # Число дубликаций динамик с разными параметрами
                                nAttrs,  # Число аттрибутов

                                # Интегрирование
                                integDynamic,  # Интегратор динамики
                                integrateAttributes,  # Аттрибуты интегрирования

                                # Функция класса системы
                                structureFunctionQ,  # Функция структуры системы
                                constParametersFunctionQ,  # Функция постоянных параметров системы
                                characteristicsFunction,  # Функция характеристик системы
                                conditionsFunction,  # Функция условий протекания процессов

                                # Функции обработки
                                inputArrayCreateQ,  # Функция предобработки входных данных
                                outputArrayCreate,  # Функция постобработки выходных данных

                                # Имя функции сохранения динамики
                                saveDynamicFun  # Функтор сохранения динамики
                                ):
    # Получаем параметры моделировния
    (Pars,  # Параметры

     # Параметры интегрирования
     integrateAttributes  # Аттрибуты интегрирования
     ) = GetModelingParameters(modeAttributes,  # Аттрибуты режима
                               dynamicParameters,  # Начальное состояние
                               attributes,  # Аттрибуты

                               nMode,  # Число аттрибутов режима
                               dynamicParametersNDyblicates,  # Число дубликаций динамик с разными параметрами
                               nAttrs,  # Число аттрибутов

                               integrateAttributes  # Аттрибуты интегрирования
                               )

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

                             saveDynamicFun,  # Функтор сохранения динамики

                             outputArrayCreate  # Функция создания выходного массива
                             )

    # Динамика системы
    sysDyn = SystemStructureQ(structureFunctionQ,  # Функция структуры системы
                              constParametersFunctionQ,  # Функция постоянных параметров системы
                              characteristicsFunction,  # Функция характеристик системы
                              conditionsFunction,  # Функция условий протекания процессов

                              integDynamic  # Метод интегрирования динамики
                              )
    sysDyns = CountDynamicsQ(sysDyn, savedFinction)  # Класс динамик системы

    # Моделируем динамики
    indexes = sysDyns.ComputingExperimentQ(Tints,
                                           stateCoordinates0s,
                                           reducedTemp0s,
                                           systemParameters,
                                           t_evals=ts)  # Индекс динамики начинается с единицы

    # Выводим результат
    return concat([Pars,
                   DataFrame({"dynamicIndex": indexes.reshape(-1,)})],
                  axis=1)


# Моделирование динамик системы (термодинамический подход)
def SystemDynamicsModelingQ(ProjectFileName,  # Имя файла проекта

                            # Функция класса системы
                            structureFunctionQ,  # Функция структуры системы
                            constParametersFunctionQ,  # Функция постоянных параметров системы
                            characteristicsFunction,  # Функция характеристик системы
                            conditionsFunction,  # Функция условий протекания процессов
                            integDynamic,  # Интегратор динамики

                            # Функции обработки
                            inputArrayCreateQ,  # Функция предобработки входных данных
                            outputArrayCreate  # Функция постобработки выходных данных
                            ):
    # Считываем файл проекта
    (ProjectsAttributes,

     # Интегрирование
     integrateAttributes,  # Аттрибуты интегрирования

     # Моделирование системы
     modeAttributes,  # Аттрибуты режима
     dynamicParameters,  # Начальное состояние
     attributes,  # Аттрибуты

     nMode,  # Число аттрибутов режима
     dynamicParametersNDyblicates,  # Число дубликаций динамик с разными параметрами
     nAttrs,  # Число аттрибутов

     # Имя файла параметров
     ParametersFileName,

     sep,  # Разделитель csv
     dec  # Десятичный разделитель
     ) = ReadProjectFileForModeling(ProjectFileName)

    # Получаем динамики системы
    dynamicToCSV = DynamicToCSVAndPlot(nMode,  # Число аттрибутов режима
                                       dynamicParametersNDyblicates,  # Число дубликаций динамик с разными параметрами
                                       nAttrs,  # Число аттрибутов

                                       ProjectsAttributes,  # Аттрибуты проекта

                                       # Файл CSV
                                       sep,  # Сепаратор CSV
                                       dec  # Десятичный разделитель
                                       )
    allPars = SystemDynamicsModelingBaseQ(modeAttributes,  # Аттрибуты режима
                                          dynamicParameters,  # Начальное состояние
                                          attributes,  # Аттрибуты

                                          nMode,  # Число аттрибутов режима
                                          dynamicParametersNDyblicates,  # Число дубликаций динамик с разными параметрами
                                          nAttrs,  # Число аттрибутов

                                          # Аттрибуты интегрирования
                                          integDynamic,  # Интегратор динамики
                                          integrateAttributes,  # Прочие аттрибуты интегрирования

                                          # Функция класса системы
                                          structureFunctionQ,  # Функция структуры системы
                                          constParametersFunctionQ,  # Функция постоянных параметров системы
                                          characteristicsFunction,  # Функция характеристик системы
                                          conditionsFunction,  # Функция условий протекания процессов

                                          # Функции обработки
                                          inputArrayCreateQ,  # Функция предобработки входных данных
                                          outputArrayCreate,  # Функция постобработки выходных данных

                                          # Имя файла динамики
                                          dynamicToCSV  # Функтор сохранения динамики
                                          )

    # Сохраняем параметры
    allPars.to_csv(ParametersFileName,
                   sep=sep, decimal=dec,
                   index=False)

    # Возвращаем полученные динамики и параметры
    return (allPars, dynamicToCSV)
