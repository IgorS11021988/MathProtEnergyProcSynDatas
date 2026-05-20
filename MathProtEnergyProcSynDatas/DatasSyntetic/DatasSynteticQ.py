from MathProtEnergyProcSynDatas.File import ReadProjectFileForModeling, ReadProjectFileForOptimizeModeling

from .SystemStructure import SystemStructureQ
from .GetModelingParameters import GetModelingParameters
from .Save import DynamicToCSV, DynamicToCSVAndPlot

from pandas import DataFrame, concat


# Моделирование динамик системы (термодинамический подход)
def SystemModelingBaseQ(modeAttributes,  # Аттрибуты режима
                        dynamicParameters,  # Начальное состояние
                        attributes,  # Аттрибуты

                        nMode,  # Число аттрибутов режима
                        dynamicParametersNDyblicates,  # Число дубликаций динамик с разными параметрами
                        nAttrs,  # Число аттрибутов

                        # Интегрирование
                        integrateAttributes,  # Аттрибуты интегрирования

                        # Функции обработки
                        inputArrayCreateQ,  # Функция предобработки входных данных

                        # Класс системы и ее динамик
                        sysDyns
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
def SystemDynamicsModelingBaseQ(modeAttributes,  # Аттрибуты режима
                                dynamicParameters,  # Начальное состояние
                                attributes,  # Аттрибуты

                                nMode,  # Число аттрибутов режима
                                dynamicParametersNDyblicates,  # Число дубликаций динамик с разными параметрами
                                nAttrs,  # Число аттрибутов

                                # Интегрирование
                                integrateAttributes,  # Аттрибуты интегрирования

                                # Функция класса системы
                                structureFunctionQ,  # Функция структуры системы
                                constParametersFunctionQ,  # Функция постоянных параметров системы
                                characteristicsFunction,  # Функция характеристик системы
                                conditionsFunction,  # Функция условий протекания процессов
                                integDynamic,  # Интегратор динамики

                                # Сохранение проинтегрированных динамик
                                saveDynamicFun,  # Функтор сохранения динамики
                                PathResult,  # Путь к результатам

                                # Функции обработки
                                inputArrayCreateQ,  # Функция предобработки входных данных
                                outputArrayCreate,  # Функция постобработки выходных данных
                                PostModeling  # Функция обработки рзультатов моделирования
                                ):
    # Получаем динамики системы
    sysDyns = SystemStructureQ(structureFunctionQ,  # Функция структуры системы
                               constParametersFunctionQ,  # Функция постоянных параметров системы
                               characteristicsFunction,  # Функция характеристик системы
                               conditionsFunction,  # Функция условий протекания процессов
                               integDynamic,  # Метод интегрирования динамики

                               # Функции обработки
                               outputArrayCreate,  # Функция постобработки выходных данных

                               # Имя функции сохранения динамики
                               saveDynamicFun  # Функтор сохранения динамики
                               )  # Класс динамик системы
    allPars = SystemModelingBaseQ(modeAttributes,  # Аттрибуты режима
                                  dynamicParameters,  # Начальное состояние
                                  attributes,  # Аттрибуты

                                  nMode,  # Число аттрибутов режима
                                  dynamicParametersNDyblicates,  # Число дубликаций динамик с разными параметрами
                                  nAttrs,  # Число аттрибутов

                                  # Интегрирование
                                  integrateAttributes,  # Аттрибуты интегрирования

                                  # Функции обработки
                                  inputArrayCreateQ,  # Функция предобработки входных данных

                                  # Класс системы и ее динамик
                                  sysDyns
                                  )

    # Обрабатываем результаты моделирования и возвращаем результат
    return PostModeling(allPars,  # Параметры моделирования с индексами
                        saveDynamicFun,  # Функтор сохранения динамики
                        PathResult  # Путь к результатам
                        )


# Моделирование динамик системы (термодинамический подход)
def SystemOptimizeModelingBaseQ(optimizeModeAttributes,  # Аттрибуты режима
                                attributesBorder,  # Границы аттрибутов
                                dynamicParametersBorder,  # Границы начального состояния

                                nOptimizeModes,  # Число аттрибутов режима
                                attributesNPoints,  # Число точек аттрибутов
                                dynamicParametersNDyblicates,  # Число состояний, определяющих конкретную динамику

                                # Сохранение проинтегрированных динамик
                                saveDynamicFun,  # Функтор сохранения динамики
                                PathResultOptimize,  # Путь к результатам

                                # Интегрирование
                                integrateAttributesOptimize,  # Аттрибуты интегрирования

                                # Функция класса системы
                                structureFunctionQ,  # Функция структуры системы
                                constParametersFunctionQ,  # Функция постоянных параметров системы
                                characteristicsFunction,  # Функция характеристик системы
                                conditionsFunction,  # Функция условий протекания процессов
                                integDynamicOptimize,  # Интегратор динамики

                                # Функции обработки
                                inputArrayCreateQ,  # Функция предобработки входных данных
                                outputArrayCreate,  # Функция постобработки выходных данных
                                OptimizeModeling  # Функция оптимизации параметров путем моделирования
                                ):
    # Создаем структуру системы
    sysDyns = SystemStructureQ(structureFunctionQ,  # Функция структуры системы
                               constParametersFunctionQ,  # Функция постоянных параметров системы
                               characteristicsFunction,  # Функция характеристик системы
                               conditionsFunction,  # Функция условий протекания процессов
                               integDynamicOptimize,  # Метод интегрирования динамики

                               # Функции обработки
                               outputArrayCreate,  # Функция постобработки выходных данных

                               # Имя функции сохранения динамики
                               saveDynamicFun  # Функтор сохранения динамики
                               )  # Класс динамик системы

    # Функция моделирования динамик системы
    def modelDynamicsFun(dynamicParameters,  # Начальное состояние
                         attributes  # Аттрибуты
                         ):
        # Получаем числа аттрибутов
        curNAttrs = len(attributes)  # Текущее число аттрибутов

        # Можделируем и выводим результат моделирования динамик
        return SystemModelingBaseQ(optimizeModeAttributes,  # Аттрибуты режима
                                   dynamicParameters,  # Начальное состояние
                                   attributes,  # Аттрибуты

                                   nOptimizeModes,  # Число аттрибутов режима
                                   dynamicParametersNDyblicates,  # Число дубликаций динамик с разными параметрами
                                   curNAttrs,  # Число аттрибутов

                                   # Интегрирование
                                   integrateAttributesOptimize,  # Аттрибуты интегрирования

                                   # Функции обработки
                                   inputArrayCreateQ,  # Функция предобработки входных данных

                                   # Класс системы и ее динамик
                                   sysDyns
                                   )

    # Обратный вызов функции оптимизации
    return OptimizeModeling(attributesBorder,  # Границы аттрибутов
                            dynamicParametersBorder,  # Границы начального состояния

                            nOptimizeModes,  # Число аттрибутов режима
                            attributesNPoints,  # Число точек аттрибутов
                            dynamicParametersNDyblicates,  # Число состояний, определяющих конкретную динамику

                            PathResultOptimize,  # Путь к результату

                            modelDynamicsFun  # Функция моделирования динамик
                            )


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
                            outputArrayCreate,  # Функция постобработки выходных данных
                            PostModeling  # Функция обработки рзультатов моделирования
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

     # Путь к результату
     PathResult,

     sep,  # Разделитель csv
     dec  # Десятичный разделитель
     ) = ReadProjectFileForModeling(ProjectFileName)

    # Создаем структуру системы, оптимизируем параметры путем моделирования динамик и выводим результат
    dynamicToCSV = DynamicToCSVAndPlot(nMode,  # Число аттрибутов режима
                                       dynamicParametersNDyblicates,  # Число дубликаций динамик с разными параметрами
                                       nAttrs,  # Число аттрибутов

                                       ProjectsAttributes,  # Аттрибуты проекта

                                       # Файл CSV
                                       sep,  # Сепаратор CSV
                                       dec  # Десятичный разделитель
                                       )
    return SystemDynamicsModelingBaseQ(modeAttributes,  # Аттрибуты режима
                                       dynamicParameters,  # Начальное состояние
                                       attributes,  # Аттрибуты

                                       nMode,  # Число аттрибутов режима
                                       dynamicParametersNDyblicates,  # Число дубликаций динамик с разными параметрами
                                       nAttrs,  # Число аттрибутов

                                       # Интегрирование
                                       integrateAttributes,  # Аттрибуты интегрирования

                                       # Функция класса системы
                                       structureFunctionQ,  # Функция структуры системы
                                       constParametersFunctionQ,  # Функция постоянных параметров системы
                                       characteristicsFunction,  # Функция характеристик системы
                                       conditionsFunction,  # Функция условий протекания процессов
                                       integDynamic,  # Интегратор динамики

                                       # Сохранение проинтегрированных динамик
                                       dynamicToCSV,  # Функтор сохранения динамики
                                       PathResult,  # Путь к результатам

                                       # Функции обработки
                                       inputArrayCreateQ,  # Функция предобработки входных данных
                                       outputArrayCreate,  # Функция постобработки выходных данных
                                       PostModeling  # Функция обработки рзультатов моделирования
                                       )


# Моделирование динамик системы (термодинамический подход)
def SystemOptimizeModelingQ(ProjectFileName,  # Имя файла проекта

                            # Функция класса системы
                            structureFunctionQ,  # Функция структуры системы
                            constParametersFunctionQ,  # Функция постоянных параметров системы
                            characteristicsFunction,  # Функция характеристик системы
                            conditionsFunction,  # Функция условий протекания процессов
                            integDynamicOptimize,  # Интегратор динамики

                            # Функции обработки
                            inputArrayCreateQ,  # Функция предобработки входных данных
                            outputArrayCreate,  # Функция постобработки выходных данных
                            OptimizeModeling  # Функция оптимизации параметров путем моделирования
                            ):
    # Считываем файл проекта
    (ProjectsAttributes,

     # Интегрирование
     integrateAttributesOptimize,  # Аттрибуты интегрирования

     # Аттрибуты
     optimizeModeAttributes,  # Аттрибуты оптимизационных режимов

     attributesBorder,  # Границы аттрибутов
     dynamicParametersBorder,  # Границы начального состояния

     attributesNPoints,  # Число точек аттрибутов
     nOptimizeModes,  # Число режимов работы
     dynamicParametersNDyblicates,  # Число состояний, определяющих конкретную динамику

     # Путь к результату
     PathResultOptimize,

     sep,  # Разделитель csv
     dec  # Десятичный разделитель
     ) = ReadProjectFileForOptimizeModeling(ProjectFileName)

    # Создаем структуру системы
    dynamicToCSV = DynamicToCSV(ProjectsAttributes,  # Аттрибуты проекта

                                # Файл CSV
                                sep,  # Сепаратор CSV
                                dec  # Десятичный разделитель
                                )
    return SystemOptimizeModelingBaseQ(optimizeModeAttributes,  # Аттрибуты режима
                                       attributesBorder,  # Границы аттрибутов
                                       dynamicParametersBorder,  # Границы начального состояния

                                       nOptimizeModes,  # Число аттрибутов режима
                                       attributesNPoints,  # Число точек аттрибутов
                                       dynamicParametersNDyblicates,  # Число состояний, определяющих конкретную динамику

                                       # Сохранение проинтегрированных динамик
                                       dynamicToCSV,  # Функтор сохранения динамики
                                       PathResultOptimize,  # Путь к результатам

                                       # Интегрирование
                                       integrateAttributesOptimize,  # Аттрибуты интегрирования

                                       # Функция класса системы
                                       structureFunctionQ,  # Функция структуры системы
                                       constParametersFunctionQ,  # Функция постоянных параметров системы
                                       characteristicsFunction,  # Функция характеристик системы
                                       conditionsFunction,  # Функция условий протекания процессов
                                       integDynamicOptimize,  # Интегратор динамики

                                       # Функции обработки
                                       inputArrayCreateQ,  # Функция предобработки входных данных
                                       outputArrayCreate,  # Функция постобработки выходных данных
                                       OptimizeModeling  # Функция оптимизации параметров путем моделирования
                                       )
