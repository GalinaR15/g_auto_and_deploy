import configparser
import os
import pandas as pd
from datetime import datetime, timedelta
import random
import string

dirname = os.path.dirname(__file__)
config = configparser.ConfigParser()
config.read(os.path.join(dirname, "config.ini"), encoding='utf8')

SHOPS_NUM = eval(config["Shops_cash_list"]["SHOPS_NUM"])
CASH_NUM = eval(config["Shops_cash_list"]["CASH_NUM"])
PRODUCT = eval(config["Product_info"]["PRODUCT"])
PRODUCT_CATEGORY = eval(config["Product_info"]["PRODUCT_CATEGORY"])
PRODUCT_PRICE = eval(config["Product_info"]["PRODUCT_PRICE"])
PRODUCT_DISCOUNT = eval(config["Product_info"]["PRODUCT_DISCOUNT"])
DIRECTORY = config["Files"]["DIRECTORY"]

file_name_list = [] # список всех файлов с выгрузками
for s in SHOPS_NUM:
    for c in CASH_NUM:
        file_name_list.append(f'{s}_{c}')

all_letters_digits = string.ascii_letters + string.digits #буквы англ алфавита, цифры

# выгрузки с информацией по чекам и продажам в папку data (эмуляция)
today_dt = datetime.today().date()
if 0 <= today_dt.weekday() <= 5:
    for shop_cash in file_name_list:
        n_doc = random.randint(1, 3) # кол-во чеков в магазине_кассе
        for_csv = []
        for d in range(n_doc):
            r = ''.join(random.choice(all_letters_digits) for _ in range(8)) + '_' + str(today_dt)  # численно-буквенный идентификатор чека
            n_item = random.randint(1, 10) # кол-во товаров в каждом чеке
            list_product_check = []
            for i in range(n_item):
                rand = random.choice(PRODUCT)
                if rand not in [j for i,j in enumerate(list_product_check)]: #проверка, что нет повтора продуктов в одном чеке
                    product_random = rand
                    d = {
                        "dt":today_dt,
                        "shop_cash": shop_cash, #магазин_касса
                        "doc_id": r, #численно-буквенный идентификатор чека
                        "product": product_random, #название товара
                        "category": PRODUCT_CATEGORY[product_random], #категория товара
                        "amount": random.randint(1,100), #кол-во товара в чеке
                        "price": PRODUCT_PRICE[product_random], # цена одной позиции без учета скидки
                        "discount": random.choice(PRODUCT_DISCOUNT) * PRODUCT_PRICE[product_random] # скидка на 1 позицию
                        }
                    list_product_check.append(d['product']) # заносим данные в лист с продуктами в чеке
                    for_csv.append(d)
        # формируем csv файл по каждому магазину_кассе
        df = pd.DataFrame(for_csv)
        df.to_csv(os.path.join(dirname, DIRECTORY ,f'{shop_cash}.csv'), index=False)


