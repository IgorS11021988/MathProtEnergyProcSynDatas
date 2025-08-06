from MathProtEnergyProc import NonEqSystemQ, NonEqSystem, NonEqSystemQDyn, NonEqSystemDyn


# Функция структуры системы для моделирования ее динамики (термодинамический подход)
def SystemStructureQ(structureFunctionQ,  # Функция структуры системы
                     constParametersFunctionQ,  # Функция постоянных параметров системы
                     characteristicsFunction,  # Функция характеристик системы
                     conditionsFunction,  # Функция условий протекания процессов

                     integDynamic  # Метод интегрирования динамики
                     ):  # Структура для расчета одной динамики
    # Описываем структуру литий-ионного элемента
    (stateCoordinatesNames,  # Имена координат состояния
     processCoordinatesNames,  # Имена координат процессов
     energyPowersNames,  # Имена энергетических степеней свободы
     reducedTemperaturesEnergyPowersNames,  # Имена приведенных температур энергетических степеней свободы
     energyPowersBetNames,  # Имена взаимодействий между энергетическими степенями свободы
     heatTransfersNames,  # Имена потоков переноса теплоты
     heatTransfersOutputEnergyPowersNames,  # Имена энергетических степеней свободы, с которых уходит теплота
     heatTransfersInputEnergyPowersNames,  # Имена энергетических степеней свободы, на которые приходит теплота
     stateCoordinatesStreamsNames,  # Имена координат состояния, изменяемых в результате внешних потоков
     heatEnergyPowersStreamsNames,  # Имена потоков теплоты на энергетические степени свободы
     stateFunction,  # Функция состояния
     stateCoordinatesVarBalanceNames,  # Имена переменных коэффициентов матрицы баланса по координатам состояния
     processCoordinatesVarBalanceNames,  # Имена переменных коэффициентов матрицы баланса по координатам процессов
     energyPowersVarTemperatureNames,  # Имена переменных температур энергетических степеней свободы
     stateCoordinatesVarPotentialsInterNames,  # Имена переменных потенциалов взаимодействия по координатам состояния
     energyPowersVarPotentialsInterNames,  # Имена переменных потенциалов взаимодействия по энергетическим степеням свободы
     stateCoordinatesVarPotentialsInterBetNames,  # Имена переменных потенциалов взаимодействия для взаимодействий между энергетическими степенями свободы по координатам состояния
     energyPowersVarPotentialsInterBetNames,  # Имена переменных потенциалов взаимодействия для взаимодействий между энергетическими степенями свободы по энергетическим степеням свободы
     energyPowersVarBetaNames,  # Имена переменных долей распределения некомпенсированной теплоты энергетических степеней свободы
     processCoordinatesVarBetaNames,  # Имена переменных долей распределения некомпенсированной теплоты координат процессов
     reducedTemperaturesEnergyPowersVarInvHeatCapacityNames,  # Имена переменных коэффициентов обратных теплоемкостей по отношению к приведенным температурам
     energyPowersVarInvHeatCapacityNames,  # Имена переменных коэффициентов обратных теплоемкостей по отношению к энергетическим степеням свободы
     reducedTemperaturesEnergyPowersVarHeatEffectNames,  # Имена переменных коэффициентов обратных теплоемкостей по отношению к приведенным температурам
     stateCoordinatesVarHeatEffectNames,  # Имена переменных коэффициентов обратных теплоемкостей по отношению к координатам состояния
     varKineticPCPCNames,  # Имена сопряженностей между собой координат процессов
     varKineticPCPCAffNames,  # Имена сопряженностей между собой термодинамических сил
     varKineticPCHeatNames,  # Имена сопряженностей координат процессов с теплопереносами
     varKineticPCHeatAffNames,  # Имена сопряженностей термодинамических сил с теплопереносами
     varKineticHeatPCNames,  # Имена сопряженностей теплопереносов с координатами процессов
     varKineticHeatPCAffNames,  # Имена сопряженностей теплопереносов с термодинамическими силами
     varKineticHeatHeatNames,  # Имена сопряженностей между собой перенесенных теплот
     varKineticHeatHeatAffNames,  # Имена сопряженностей между собой термодинамических сил по переносу теплот
     stateCoordinatesVarStreamsNames,  # Имена переменных внешних потоков
     heatEnergyPowersVarStreamsNames  # Имена переменных внешних потоков теплоты
     ) = structureFunctionQ()

    # Класс системы
    sysStructureQ = NonEqSystemQ(stateCoordinatesNames,  # Имена координат состояния
                                 processCoordinatesNames,  # Имена координат процессов
                                 energyPowersNames,  # Имена энергетических степеней свободы
                                 reducedTemperaturesEnergyPowersNames,  # Имена приведенных температур энергетических степеней свободы
                                 energyPowersBetNames,  # Имена взаимодействий между энергетическими степенями свободы
                                 heatTransfersNames,  # Имена потоков переноса теплоты
                                 heatTransfersOutputEnergyPowersNames,  # Имена энергетических степеней свободы, с которых уходит теплота
                                 heatTransfersInputEnergyPowersNames,  # Имена энергетических степеней свободы, на которые приходит теплота

                                 stateCoordinatesStreamsNames,  # Имена координат состояния, изменяемых в результате внешних потоков
                                 heatEnergyPowersStreamsNames,  # Имена потоков теплоты на энергетические степени свободы

                                 stateFunction,  # Функция состояния

                                 stateCoordinatesVarBalanceNames,  # Имена переменных коэффициентов матрицы баланса по координатам состояния
                                 processCoordinatesVarBalanceNames,  # Имена переменных коэффициентов матрицы баланса по координатам процессов
                                 energyPowersVarTemperatureNames,  # Имена переменных температур энергетических степеней свободы
                                 stateCoordinatesVarPotentialsInterNames,  # Имена переменных потенциалов взаимодействия по координатам состояния
                                 energyPowersVarPotentialsInterNames,  # Имена переменных потенциалов взаимодействия по энергетическим степеням свободы
                                 stateCoordinatesVarPotentialsInterBetNames,  # Имена переменных потенциалов взаимодействия для взаимодействий между энергетическими степенями свободы по координатам состояния
                                 energyPowersVarPotentialsInterBetNames,  # Имена переменных потенциалов взаимодействия для взаимодействий между энергетическими степенями свободы по энергетическим степеням свободы
                                 energyPowersVarBetaNames,  # Имена переменных долей распределения некомпенсированной теплоты энергетических степеней свободы
                                 processCoordinatesVarBetaNames,  # Имена переменных долей распределения некомпенсированной теплоты координат процессов
                                 reducedTemperaturesEnergyPowersVarInvHeatCapacityNames,  # Имена переменных коэффициентов обратных теплоемкостей по отношению к приведенным температурам
                                 energyPowersVarInvHeatCapacityNames,  # Имена переменных коэффициентов обратных теплоемкостей по отношению к энергетическим степеням свободы
                                 reducedTemperaturesEnergyPowersVarHeatEffectNames,  # Имена переменных коэффициентов обратных теплоемкостей по отношению к приведенным температурам
                                 stateCoordinatesVarHeatEffectNames,  # Имена переменных коэффициентов обратных теплоемкостей по отношению к координатам состояния

                                 varKineticPCPCNames,  # Имена сопряженностей между собой координат процессов
                                 varKineticPCPCAffNames,  # Имена сопряженностей между собой термодинамических сил
                                 varKineticPCHeatNames,  # Имена сопряженностей координат процессов с теплопереносами
                                 varKineticPCHeatAffNames,  # Имена сопряженностей термодинамических сил с теплопереносами
                                 varKineticHeatPCNames,  # Имена сопряженностей теплопереносов с координатами процессов
                                 varKineticHeatPCAffNames,  # Имена сопряженностей теплопереносов с термодинамическими силами
                                 varKineticHeatHeatNames,  # Имена сопряженностей между собой перенесенных теплот
                                 varKineticHeatHeatAffNames,  # Имена сопряженностей между собой термодинамических сил по переносу теплот

                                 stateCoordinatesVarStreamsNames,  # Имена переменных внешних потоков
                                 heatEnergyPowersVarStreamsNames  # Имена переменных внешних потоков теплоты
                                 )

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
    (stateCoordinatesNames,  # Имена координат состояния
     processCoordinatesNames,  # Имена координат процессов
     stateCoordinatesStreamsNames,  # Имена координат состояния, изменяемых в результате внешних потоков
     stateFunction,  # Функция состояния
     stateCoordinatesVarBalanceNames,  # Имена переменных коэффициентов матрицы баланса по координатам состояния
     processCoordinatesVarBalanceNames,  # Имена переменных коэффициентов матрицы баланса по координатам процессов
     stateCoordinatesVarPotentialsInterNames,  # Имена переменных потенциалов взаимодействия по координатам состояния
     varKineticNames,  # Имена сопряженностей между собой координат процессов
     varKineticAffNames,  # Имена сопряженностей между собой термодинамических сил
     stateCoordinatesVarStreamsNames  # Имена переменных внешних потоков
     ) = structureFunction()

    # Класс системы
    sysStructure = NonEqSystem(stateCoordinatesNames,  # Имена координат состояния
                               processCoordinatesNames,  # Имена координат процессов
                               stateCoordinatesStreamsNames,  # Имена координат состояния, изменяемых в результате внешних потоков
                               stateFunction,  # Функция состояния
                               stateCoordinatesVarBalanceNames,  # Имена переменных коэффициентов матрицы баланса по координатам состояния
                               processCoordinatesVarBalanceNames,  # Имена переменных коэффициентов матрицы баланса по координатам процессов
                               stateCoordinatesVarPotentialsInterNames,  # Имена переменных потенциалов взаимодействия по координатам состояния
                               varKineticNames,  # Имена сопряженностей между собой координат процессов
                               varKineticAffNames,  # Имена сопряженностей между собой термодинамических сил
                               stateCoordinatesVarStreamsNames  # Имена переменных внешних потоков
                               )

    # Задаем постоянные параметры системы
    constParametersFunction(sysStructure)

    # Задаем класс динамики системы
    return NonEqSystemDyn(sysStructure,  # Система
                          conditionsFunction,  # Функция условий протекания процессов
                          characteristicsFunction,  # Функция внешних параметров
                          integDynamic  # Метод интегрирования дифференциальных уравнений
                          )
