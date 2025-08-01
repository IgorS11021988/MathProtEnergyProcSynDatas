import os

from matplotlib import pyplot as plt


# Функция построения графика одной величины
def OneTimeValueGraphic(times,  # Моменты времени
                        values,  # Величины в моменты времени
                        graphicsName,  # Имя полотна
                        axeName,  # Имя оси
                        needGrid=True  # Нужна ли сетка
                        ):  # Построение графика одной величины во времени
    # Строим полотно
    plt.figure()

    # Строим график
    plt.plot(times, values)

    # Добавляем надписи
    plt.title(graphicsName)  # Имя полотна
    plt.xlabel("Время, с")  # Имя оси времени
    plt.ylabel(axeName)  # Имя оси величины

    # Добавляем сетку
    plt.grid(needGrid)


def TimesValuesGraphics(times,  # Моменты времени
                        listValues,  # Список величин в моменты времени
                        listValuesNames,  # Список имен величин
                        graphicsName,  # Имя полотна
                        axeName,  # Имя оси
                        needGrid=True  # Нужна ли сетка
                        ):  # Построение графиков нескольких величин во времени
    # Строим полотно
    plt.figure()

    # Строим графики
    nValues = len(listValuesNames)  # Число величин
    inds = range(nValues)
    for ind in inds:
        plt.plot(times, listValues[ind], label=listValuesNames[ind])

    # Добавляем надписи
    plt.title(graphicsName)  # Имя полотна
    plt.xlabel("Время, с")  # Имя оси времени
    plt.ylabel(axeName)  # Имя оси величины

    # Добавляем сетку
    plt.grid(needGrid)

    # Добавляем легенду
    plt.legend(loc="best")


# Формирование имени файла графиков
def SaveGraphicsImage(imageDir,  # Директория изображения
                      graphicName,  # Имя графика
                      dynamicName  # Имя динамики
                      ):
    # Формируем полное имя изображения
    fullImageName = os.path.join(imageDir, graphicName + dynamicName + ".jpg")
    
    # Сохраняем изображение
    plt.savefig(fullImageName)
