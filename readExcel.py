import pandas as pd

# all_discounts = сумма всех примененных скидок. (Складываем размер скидок)
# price_after_discounts = итоговая сумма с примененными скидками.  (final_summa_so_skidkoy_bez_rp - all_discounts)
# сумма_с_рп = без рп * (100 - %) пример 5% есть = 100 * 0.95 = 95 рублей
# summa_s_rp = final_summa_so_skidkoy_bez_rp * (100 - skidka_rp)


# если есть купон: сумма с купоном = (сумма с рп - Размер купона)
# если использованы бонусы: (сумма с купоном - Размер бонуса)
# если есть бонусы, зачисленные на карту: (сумма после всех вычетов + количество конвертируемых бонусов на карту)
# Делаем проверки значения сверху и Сумма списанную с карты покупателя.
# Если списало с карты больше, чем мы насчитали - ошибка. Выдаём разницу в сумме.
# Вторая проверка, проверяем сумма списсаную по карте и сумму по чеку покупателя. Если что вызываем Предупреждение!
# Проверяем повторяющиеся товары в списке, кроме пакета-майки. Если > 1 Выдаём Предупреждение.

def make_results(file, a, b, c, d):
    file = file
    skidka_rp = a.value()
    kupon = b.value()
    bonuses = c.value()
    convertable_bonuses = d.value()

    all_discounts = 0


    print("####")
    print(type(file))
    print(type(a.value()))
    print(file, a.value(), b.value(), c.value(), d.value())
    print("####")
    #print(float(input('Введите сумму, списанную с карты покупателя: ')))

    dd = pd.read_excel(open(f'{file}', 'rb'))
    # skidka_rp = print(int(input('Введите значение скидки РП: ')))
    # kupon = print(float(input('Введите размер купона, если есть (или введите 0) : ')))
    # bonuses = (float(input('Введите размер использованных бонусов при оплате \nесли есть (или введите) 0: ')))
    # convertable_bonuses = print(float(input('Введите размер скидок, которые прошли бонусами\nна карту лояльности (или введите 0): ')))
    # print(float(input('Введите сумму, списанную с карты покупателя: ')))


    skidka = {"Любимый Продукт":"0.2", # 20 % скидка
             "Вторая Цена Колво":"введи размер",
             "Вторая Цена Карта":"введи размер скидки",
             "Любимый продукт на 1 день": "0.2",  # скидка 20 %
             "Зеленый Ценник": "0.4",  # 40% скидка
             "Абонемент 6 (Я в Магазине)": "0.2"}  # 20 % скидка


    final_summa_so_skidkoy_bez_rp = 0.0   #  Здесь будет посчитана итоговая Сумма с учетом скидки без РП
    final_summa_pokupatelya = 0.0   # Здесь будет посчитана итоговая Сумма, которую заплатил покупатель

    for i in range((len(dd['Товар']))):
        #print(dd['Типскидки'][i])
        final_summa_pokupatelya += dd['Сумма'][i]
        if dd['Типскидки'][i] in skidka:
            #print(dd['Рознцена'][i])
            summa_skidki = dd['Рознцена'][i]*float(skidka[dd['Типскидки'][i]])
            print(f'Сумма скидки = {summa_skidki}')
            moya_cena = dd['Рознцена'][i] - summa_skidki
            #moya_summa = int((moya_cena * dd['Колво'][i])*100) / 100
            moya_summa = round(moya_cena * dd['Колво'][i], 2)
            print(f'Моя цена {moya_cena}')

            #print(f'moya cena =  {moya_cena}')
            #print(f'moya summa =  {moya_summa}')

            final_summa_so_skidkoy_bez_rp += moya_summa
        else:
            #final_summa_so_skidkoy_bez_rp += (int(dd['Рознцена'][i] * dd['Колво'][i])*100)/100
            final_summa_so_skidkoy_bez_rp += round(dd['Рознцена'][i] * dd['Колво'][i], 2)



    price_after_discounts = final_summa_so_skidkoy_bez_rp

    if skidka_rp:
        all_discounts += final_summa_so_skidkoy_bez_rp * (skidka_rp / 100)  # Добавляем значение к общей сумме скидок
        print(all_discounts)
        summa_s_rp = final_summa_so_skidkoy_bez_rp * ((100 - skidka_rp) / 100)
        print(summa_s_rp)
        price_after_discounts = summa_s_rp
    if kupon:
        all_discounts += kupon
        price_after_discounts -= kupon
    if bonuses:
        all_discounts += bonuses
        price_after_discounts -= bonuses

    print("ИТОГИ : ")
    print(f'Покупатель по чеку заплатил {final_summa_pokupatelya} ,а Сумма расчётная со скидкой без РП: {final_summa_so_skidkoy_bez_rp}')
    print(f's rp etc = {price_after_discounts}')

    #raznica = final_summa_so_skidkoy_bez_rp - final_summa_pokupatelya
    raznica = price_after_discounts - final_summa_pokupatelya
    if raznica >= 0:
        print('Всё ок, ПОКУПАТЕЛЬ ОСТАЛСЯ В ПЛЮСЕ или Суммы совпали')
        print(f"Разница = {raznica}")
    else:
        print('ПОКУПАТЕЛЬ ПЕРЕПЛАТИЛ !!! ')
        print(f"Разница = {raznica}")








# # Указываем к какому окну он принадлежит, какой у него фон и какая обводка
# frame_top = Frame(root, bg='#ffb700', bd=5)
# # Также указываем его расположение
# frame_top.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.25)
#
# # Все то-же самое, но для второго фрейма
# frame_bottom = Frame(root, bg='#ffb700', bd=5)
# frame_bottom.place(relx=0.15, rely=0.55, relwidth=0.7, relheight=0.1)
#
# # Создаем текстовое поле для получения данных от пользователя
# cityField = Entry(frame_top, bg='white', font=30)
# cityField.pack() # Размещение этого объекта, всегда нужно прописывать
#
# btn = Button(frame_top, text='Посмотреть погоду', command=make_results)
# btn.pack()













# сумма_с_рп = без рп * (100 - %) пример 5% есть = 100 * 0.95 = 95 рублей
# если есть купон: сумма с купоном = (сумма с рп - Размер купона)
# если использованы бонусы: (сумма с купоном - Размер купона)
# если есть бонусы, зачисленные на карту: (сумма после всех вычетов + количество конвертируемых бонусов на карту)
# Делаем проверки значения сверху и Сумма списанную с карты покупателя.
# Если списало с карты больше, чем мы насчитали - ошибка. Выдаём разницу в сумме.
# Вторая проверка, проверяем сумма списсаную по карте и сумму по чеку покупателя. Если что вызываем Предупреждение!
# Проверяем повторяющиеся товары в списке, кроме пакета-майки. Если > 1 Выдаём Предупреждение.

# def make_results(*args):
#     dd = pd.read_excel(open('ChekVkus.xlsx', 'rb'))
#     skidka_rp = print(int(input('Введите значение скидки РП: ')))
#     kupon = print(float(input('Введите размер купона, если есть (или введите 0) : ')))
#     bonuses = (float(input('Введите размер использованных бонусов при оплате \nесли есть (или введите) 0: ')))
#     convertable_bonuses = print(float(input('Введите размер скидок, которые прошли бонусами\nна карту лояльности (или введите 0): ')))
#     print(float(input('Введите сумму, списанную с карты покупателя: ')))
#
#
#     skidka = {"Любимый Продукт":"0.2", # 20 % скидка
#              "Вторая Цена Колво":"введи размер",
#              "Вторая Цена Карта":"введи размер скидки",
#              "Любимый продукт на 1 день": "0.2",  # скидка 20 %
#              "Зеленый Ценник": "0.4",  # 40% скидка
#              "Абонемент 6 (Я в Магазине)": "0.2"}  # 20 % скидка
#
#
#     final_summa_so_skidkoy_bez_rp = 0.0   #  Здесь будет посчитана итоговая Сумма с учетом скидки без РП
#     final_summa_pokupatelya = 0.0   # Здесь будет посчитана итоговая Сумма, которую заплатил покупатель
#
#     for i in range((len(dd['Товар']))):
#         #print(dd['Типскидки'][i])
#         final_summa_pokupatelya += dd['Сумма'][i]
#         if dd['Типскидки'][i] in skidka:
#             #print(dd['Рознцена'][i])
#             summa_skidki = dd['Рознцена'][i]*float(skidka[dd['Типскидки'][i]])
#             print(f'Сумма скидки = {summa_skidki}')
#             moya_cena = dd['Рознцена'][i] - summa_skidki
#             #moya_summa = int((moya_cena * dd['Колво'][i])*100) / 100
#             moya_summa = round(moya_cena * dd['Колво'][i], 2)
#             print(f'Моя цена {moya_cena}')
#
#             #print(f'moya cena =  {moya_cena}')
#             #print(f'moya summa =  {moya_summa}')
#
#             final_summa_so_skidkoy_bez_rp += moya_summa
#         else:
#             #final_summa_so_skidkoy_bez_rp += (int(dd['Рознцена'][i] * dd['Колво'][i])*100)/100
#             final_summa_so_skidkoy_bez_rp += round(dd['Рознцена'][i] * dd['Колво'][i], 2)
#
#     print("ИТОГИ : ")
#     print(f'Покупатель по чеку заплатил {final_summa_pokupatelya} ,а Сумма расчётная со скидкой без РП: {final_summa_so_skidkoy_bez_rp}')
#     raznica = final_summa_so_skidkoy_bez_rp - final_summa_pokupatelya
#     if raznica >= 0:
#         print('Всё ок, ПОКУПАТЕЛЬ ОСТАЛСЯ В ПЛЮСЕ или Суммы совпали')
#         print(f"Разница = {raznica}")
#     else:
#         print('ПОКУПАТЕЛЬ ПЕРЕПЛАТИЛ !!! ')
#         print(f"Разница = {raznica}")








# root['bg'] = '#008000'
# root.title = 'ВкусЧек'
# root.wm_attributes('-alpha', 0.95)
# root.geometry('700x500')
#
# # Указываем к какому окну он принадлежит, какой у него фон и какая обводка
# frame_top = Frame(root, bg='#ffb700', bd=5)
# # Также указываем его расположение
# frame_top.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.25)
#
# # Все то-же самое, но для второго фрейма
# frame_bottom = Frame(root, bg='#ffb700', bd=5)
# frame_bottom.place(relx=0.15, rely=0.55, relwidth=0.7, relheight=0.1)
#
# # Создаем текстовое поле для получения данных от пользователя
# cityField = Entry(frame_top, bg='white', font=30)
# cityField.pack() # Размещение этого объекта, всегда нужно прописывать
#
# btn = Button(frame_top, text='Посмотреть погоду', command=make_results)
# btn.pack()
#
# def func1():
#     input_file = root.filedialog.askopenfile()
#
# btn1 = Button(root, text="click", command=func1)
#
# btn1.pack()
# # Создаем текстовую надпись, в которую будет выводиться информация о погоде
# info = Label(frame_bottom, text='Погодная информация', bg='#ffb700', font=40)
# info.pack()
#
# root.mainloop()






