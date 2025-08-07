# Базовый индикатор
def BaseIndicate(msg,  # Сообщение
                 index  # Индекс
                 ):
    # Выводим сообщение
    print(msg + str(index))


# Отсутствие сообщения
def NoIndicate(index  # Индекс
               ):
    pass


# Сообщение о сохранении динамики в файл
def SaveDynamicToFileIndicate(index  # Индекс
                              ):
    # Выводим сообщение о сохранении динамики в файл
    BaseIndicate("Writting dynamic: ",  # Сообщение
                 index  # Индекс
                 )


# Сообщение о выводе графика
def PlotGraphicIndicate(index  # Индекс
                        ):
    # Выводим сообщение об отображении графика
    BaseIndicate("Graphic dynamic index: ",  # Сообщение
                 index  # Индекс
                 )
