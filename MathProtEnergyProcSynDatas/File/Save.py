import os

from MathProtEnergyProcSynDatas.Indicate import NoIndicate
from MathProtEnergyProcSynDatas.ValuesGraphics import PlotGraphics, SaveGraphics


# Функция сохранения данных в .csv файл и отображения графиков
def DynamicSaveAndPlotGraphics(dynamicsHeaders,  # Словарь динамик с заголовками
                               saveDynamicFun,  # Функция сохранения динамик

                               t,  # Моменты времени
                               oneTimeValueGraphicsDict,  # Один график на одном полотне
                               timesValuesGraphicsDict,  # Несколько графиков на одном полотне

                               plotGraphics,  # Необходимость построения графиков

                               saveDynamicIndicator=NoIndicate,  # Индикатор сохранения динамики
                               plotGraphicIndicator=NoIndicate,  # Индикатор отображения графиков
                               index=0  # Индекс динамики
                               ):
    # Выводим сообщение о сохранении динамики в файл
    saveDynamicIndicator(index)

    # Сохраняем динамику
    saveDynamicFun.SaveDynamic(dynamicsHeaders, index)

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
                               saveDynamicFun,  # Функция сохранения динамик

                               t,  # Моменты времени
                               oneTimeValueGraphicsDict,  # Один график на одном полотне
                               timesValuesGraphicsDict,  # Несколько графиков на одном полотне

                               plotGraphics,  # Необходимость построения графиков
                               showGraphics=False,  # Необходимость отображения графиков

                               saveDynamicIndicator=NoIndicate,  # Индикатор сохранения динамики
                               saveGraphicIndicator=NoIndicate,  # Индикатор отображения графиков
                               index=0  # Индекс динамики
                               ):
    # Выводим сообщение о сохранении динамики в файл
    saveDynamicIndicator(index)

    # Сохраняем динамику
    dynamicsFileName = saveDynamicFun.SaveDynamic(dynamicsHeaders, index)

    # Рисуем при необходимости график
    if plotGraphics:
        # Получаем имена директории и динамики
        dynDirName = os.path.dirname(dynamicsFileName)  # Имя директории
        dynName = os.path.basename(dynamicsFileName)  # Имя файла динамики с расширением
        dynName = os.path.splitext(dynName)[0]  # Имя файла динамики без расширения

        # Выводим сообщение о сохранении графика
        saveGraphicIndicator(index)

        # Сохраняем графики
        SaveGraphics(t,  # Моменты времени
                     oneTimeValueGraphicsDict,  # Один график на одном полотне
                     timesValuesGraphicsDict,  # Несколько графиков на одном полотне

                     dynDirName,  # Имя директории динамики
                     dynName,  # Имя динамики

                     showGraphics=showGraphics  # Необходимость отображения графиков
                     )
