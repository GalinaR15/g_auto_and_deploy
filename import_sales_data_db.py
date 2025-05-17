import configparser
import os
import pandas as pd
from db_connect import DBconnect

dirname = os.path.dirname(__file__)
config = configparser.ConfigParser()
config.read(os.path.join(dirname, "config.ini"), encoding='utf8')

DB = config["DB"]
database = DBconnect(
    host=DB["HOST"],
    database=DB["DATABASE"],
    user=DB["USER"],
    password=DB["PASSWORD"]
)
DIRECTORY = config["Files"]["DIRECTORY"]

# запись в бд из csv файлов в папке data
csv_files = [f for f in os.listdir(DIRECTORY) if f.endswith('.csv')] #только csv файлы
for f in csv_files:
    file_df = pd.read_csv(f'{DIRECTORY}/{f}', sep=',', encoding='utf8')
    print(file_df)
    for i, row in file_df.iterrows():
         query = f"insert into auto_and_deploy (dt,	n_shop,	n_cash,	doc_id,	product, category, amount, price, discount) values ('{row['dt']}', '{row['shop_cash'].split('_')[0]}', '{row['shop_cash'].split('_')[1]}', '{row['doc_id']}', '{row['product']}', '{row['category']}', '{row['amount']}', '{row['price']}', '{row['discount']}')"
         database.post(query)