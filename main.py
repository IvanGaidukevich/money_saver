"""
Программа учета расходов.
Использует библиотеку pandas для работы с CSV.
Данные хранятся в файле purchase.csv
Реализована функционал:
1) добавления записи в CSV с проверкой через регулярные выражения вводимой пользователм даты и
стоимости покупки.
2) выведения всех записей на экран
3) выведения всех записей по категории
4) выведения всех записаей по конкретной дате
5) выведения отсортированных по возрастанию стоимости полкупки всех записей
6) удаления записи по ID

В модуле core реализованы интрефейсные функции для ввода данных и вывода сообщений пользователю,
а также функции по работе с данным.

У всех функций прописаны docstring, у некоторых doctest.
Реализован перехват возможных исключений

"""

import pandas as pd
from core import add_new_item, show_for_date, del_item, show_by_category, show_message, input_actions

try:
    df = pd.read_csv("purchase.csv")
    show_message("hi")
    while True:
        show_message("menu")
        match input_actions("menu_item"):
            case "1":
                show_message("add_item")
                record = []
                date = input_actions("add_date")
                if date:
                    record.append(date)
                    record.append(input_actions("add_category"))
                    record.append(input_actions("add_product"))
                    cost = input_actions("add_cost")
                    if cost:
                        record.append(int(cost))
                        add_new_item(df, record)
                        input_actions("press_enter")

                    else:
                        show_message("wrong_cost")
                        input_actions("press_enter")
                else:
                    show_message("wrong_date")
                    input_actions("press_enter")
            case "2":
                show_message("show_all", df)
                input_actions("press_enter")
            case "3":
                show_message("date", show_for_date(df, input_actions("show_date")))
                input_actions("press_enter")
            case "4":
                show_message("which_category", df)
                show_message("category", show_by_category(df, input_actions("category")))
                input_actions("press_enter")
            case "5":
                show_message("min_to_max", df)
                input_actions("press_enter")
            case "6":
                show_message("show_all", df)
                show_message("del", del_item(df, input_actions("del_item")))
                input_actions("press_enter")
            case "7":
                show_message("bye")
                break
            case _:
                show_message("wrong")
except FileNotFoundError:
    show_message("exception")
