from functools import partial
from tkinter import *
from tkinter import filedialog
from classes import Discount
from readExcel import make_results
import pandas as pd

def browse_file():
    def delete():
        start_btn.grid_remove()
        del_btn.grid_remove()
        # dis_1.change(0)
        # dis_2.change(0)
        # dis_3.change(0)
        # dis_4.change(0)

    fname = filedialog.askopenfilename(filetypes = (("Template files", "*.xlsx"), ("All files", "*")))
    print(fname)
    if fname:
        start_btn = Button(w, text="Начать просчёт",
                           command=partial(make_results, fname, dis_1, dis_2, dis_3, dis_4))
        start_btn.grid(column=0)
        del_btn = Button(w, text="Clear", command=partial(delete))
        del_btn.grid(column=1)




def change_discount_rp():
    val = txt_1.get()
    print(type(val))
    print(val)
    if val and val != ".!entry":
        print(f'fff {val}')
        dis_1.change(val)
        disc_1_label.configure(text=f"Введенная скидка РП = {dis_1.value()}")


def change_discount_kupon():
    val = txt_2.get()
    print(type(val))
    print(val)
    if val and val != ".!entry":
        print(f'fff {val}')
        dis_2.change(val)
        disc_2_label.configure(text=f"Введенная скидка Купона = {dis_2.value()}")

def change_discount_bonuses():
    val = txt_3.get()
    print(type(val))
    print(val)
    if val and val != ".!entry":
        print(f'fff {val}')
        dis_3.change(val)
        disc_3_label.configure(text=f"Введенная скидка Бонусов = {dis_3.value()}")


def change_discount_convertable_bonuses():
    val = txt_4.get()
    print(type(val))
    print(val)
    if val and val != ".!entry":
        print(f'fff {val}')
        dis_4.change(val)
        disc_4_label.configure(text=f"Скидки которые прошли бонусами\nна карту лояльности = {dis_4.value()}")


skidka_rp = Discount("0.0") # ('Введите значение скидки РП: ')
kupon = Discount("0")    # ('Введите размер купона, если есть (или введите 0) : ')
bonuses = Discount("0")  # ('Введите размер использованных бонусов при оплате \nесли есть (или введите) 0: ')))
convertable_bonuses = Discount("0.0")  # ('Введите размер скидок, которые прошли бонусами\nна карту лояльности (или введите 0): ')))


dis_1 = skidka_rp
dis_2 = kupon
dis_3 = bonuses
dis_4 = convertable_bonuses


def open_file():
    #file = filedialog.askopenfilename()
    file = filedialog.askopenfilename(filetypes = (("Template files", "*.type"), ("All files", "*")))
    return file


w = Tk()
w.title('Vkus Receipt')
w.geometry('800x400')

lbl = Label(w, text="Задайте размеры скидок, если есть.", font=("Times New Roman", 16), highlightthickness=6, highlightcolor="RED"
                                                                                                                             "")
lbl.grid(column=0, row=0, sticky="W")
l2 = Label(w, text="  0.0 по умолчанию.", font=("Arial Bold", 16))
l2.grid(column=1, row=0)
# btn = Button(w, text="Не нажимать!", bg="white", fg="red", command=clicked)
# btn.grid(column=3, row=0)

disc_1_label = Label(w, text=f"Скидка РП = {dis_1.value()}", font=("Arial Bold", 16))
disc_1_label.grid(column=0, row=2)
txt_1 = Entry(w, width=10)
txt_1.grid(column=1, row=2)
btn_1 = Button(w, text="Изменить", command=change_discount_rp)
btn_1.grid(column=2, row=2)

disc_2_label = Label(w, text=f"Размер купона = {dis_2.value()}", font=("Arial Bold", 16))
disc_2_label.grid(column=0, row=3)
txt_2 = Entry(w, width=10)
txt_2.grid(column=1, row=3)
btn_2 = Button(w, text="Изменить", command=change_discount_kupon)
btn_2.grid(column=2, row=3)

disc_3_label = Label(w, text=f"Размер использованных бонусов = {dis_3.value()}", font=("Arial Bold", 16))
disc_3_label.grid(column=0, row=4)
txt_3 = Entry(w, width=10)
txt_3.grid(column=1, row=4)
btn_3 = Button(w, text="Изменить", command=change_discount_bonuses)
btn_3.grid(column=2, row=4)

disc_4_label = Label(w, text=f"Размер скидок, которые прошли бонусами\nна карту лояльности = {dis_4.value()}", font=("Arial Bold", 16))
disc_4_label.grid(column=0, row=5)
txt_4 = Entry(w, width=10)
txt_4.grid(column=1, row=5)
btn_4 = Button(w, text="Изменить", command=change_discount_convertable_bonuses)
btn_4.grid(column=2, row=5)

emp = Label(w, text="")
emp.grid()
x = Label(w, text="Загрузите Excel файл чека с разрешением .xlsx")
x.grid()
broButton = Button(master=w, text='Browse file', width=10, command=browse_file)
broButton.grid()

# w.update()

# file = browse_file()
#
# print(type(file))
#
# if ".xlsx" in str(file):
#     start_btn = Button(w, text="Начать просчёт", command=partial(make_results, browse_file(), dis_1, dis_2, dis_3, dis_4))
#     start_btn.grid()





# сумма_с_рп = без рп * (100 - %) пример 5% есть = 100 * 0.95 = 95 рублей
# если есть купон: сумма с купоном = (сумма с рп - Размер купона)
# если использованы бонусы: (сумма с купоном - Размер купона)
# если есть бонусы, зачисленные на карту: (сумма после всех вычетов + количество конвертируемых бонусов на карту)
# Делаем проверки значения сверху и Сумма списанную с карты покупателя.
# Если списало с карты больше, чем мы насчитали - ошибка. Выдаём разницу в сумме.
# Вторая проверка, проверяем сумма списсаную по карте и сумму по чеку покупателя. Если что вызываем Предупреждение!
# Проверяем повторяющиеся товары в списке, кроме пакета-майки. Если > 1 Выдаём Предупреждение.



w.mainloop()

print(f"my new value is = {skidka_rp.value()}")
