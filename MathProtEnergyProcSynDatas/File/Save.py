import os

from pandas import concat, DataFrame

from MathProtEnergyProcSynDatas.Indicate import NoIndicate
from MathProtEnergyProcSynDatas.ValuesGraphics import PlotGraphics, SaveGraphics


# Функция сохранения параметров
def ParametersSave(dynamicCharacteristics,  # Индексы динамик
                   Pars,  # Параметры
                   ParametersFileName,  # Имя файла параметров

                   sep,  # CSV разделитель
                   dec  # Десятичный разделитель
                   ):  # Сохранение параметров в файл
    # Конкатенуем характеристики динамик к параметрам динамик
    allDynamicDatas = concat([Pars, dynamicCharacteristics], axis=1)  # Параметры для

    # Сохраняем параметры в файл
    allDynamicDatas.to_csv(ParametersFileName, sep=sep, decimal=dec, index=False)  # Сохраняем в csv файл


# Функция сохранения данных в .csv файл
def DynamicSave(dynamicsHeaders,  # Словарь динамик с заголовками
                dynamicsFileName,  # Имя файла динамик

                sep, dec  # Разделители (csv и десятичный соответственно)
                ):
    # Формируем фрейм данных
    DynamicDatas = DataFrame(dynamicsHeaders)

    # Сохраняем в csv файл
    DynamicDatas.to_csv(dynamicsFileName,
                        sep=sep, decimal=dec,
                        index=False)


# Функция сохранения данных в .csv файл и отображения графиков
def DynamicSaveAndPlotGraphics(dynamicsHeaders,  # Словарь динамик с заголовками
                               dynamicsFileName,  # Имя файла динамик

                               t,  # Моменты времени
                               oneTimeValueGraphicsDict,  # Один график на одном полотне
                               timesValuesGraphicsDict,  # Несколько графиков на одном полотне

                               plotGraphics,  # Необходимость построения графиков

                               sep, dec,   # Разделители (csv и десятичный соответственно)

                               saveDynamicIndicator=NoIndicate,  # Индикатор сохранения динамики
                               plotGraphicIndicator=NoIndicate,  # Индикатор отображения графиков
                               index=0  # Индекс динамики
                               ):
    # Выводим сообщение о сохранении динамики в файл
    saveDynamicIndicator(index)

    # Сохраняем динамику в .csv файл
    DynamicSave(dynamicsHeaders,  # Словарь динамик с заголовками
                dynamicsFileName,  # Имя файла динамик

                sep, dec  # Разделители (csv и десятичный соответственно)
                )

    # Рисуем при необходимости график
    if plotGraphics:
        # Выводим сообщение о сохранении графика
        plotGraphicIndicator(index)

        # Отображаем графики
        PlotGraphics(t,  # Моменты времени
                     oneTimeValueGraphicsDict,  # Один график на одном полотне
                     timesValuesGraphicsDict  # Несколько графиков на одном полотне
                     )


# Функция сохранения данных в .csv файл и отображения графиков
def DynamicSaveAndSaveGraphics(dynamicsHeaders,  # Словарь динамик с заголовками
                               dynamicsFileName,  # Имя файла динамик

                               t,  # Моменты времени
                               oneTimeValueGraphicsDict,  # Один график на одном полотне
                               timesValuesGraphicsDict,  # Несколько графиков на одном полотне

                               plotGraphics,  # Необходимость построения графиков

                               sep, dec,   # Разделители (csv и десятичный соответственно)

                               saveDynamicIndicator=NoIndicate,  # Индикатор сохранения динамики
                               saveGraphicIndicator=NoIndicate,  # Индикатор отображения графиков
                               index=0  # Индекс динамики
                               ):
    # Выводим сообщение о сохранении динамики в файл
    saveDynamicIndicator(index)

    # Сохраняем динамику в .csv файл
    DynamicSave(dynamicsHeaders,  # Словарь динамик с заголовками
                dynamicsFileName,  # Имя файла динамик

                sep, dec  # Разделители (csv и десятичный соответственно)
                )

    # Рисуем при необходимости график
    if plotGraphics:
        # Получаем имена директории и динамики
        dynDirName = os.path.dirname(dynamicsFileName)  # Имя директории
        dynName = os.path.basename(dynamicsFileName)  # Имя файла динамики с расширением
        dynName = os.path.splitext(dynName)[0]  # Имя файла динамики без расширения

        # Выводим сообщение о сохранении графика
        saveGraphicIndicator(index)

        # Отображаем графики
        SaveGraphics(t,  # Моменты времени
                     oneTimeValueGraphicsDict,  # Один график на одном полотне
                     timesValuesGraphicsDict,  # Несколько графиков на одном полотне

                     dynDirName,  # Имя директории динамики
                     dynName  # Имя динамики
                     )
