Проект содержит скрипты для генерации данных о продаж и импорта этих данных в БД. 

Инструкция по запуску проекта на новой машине:
- устанавливаем Python, PostgreSQL (или др.СУБД)
- клонируем проект
  git clone https://github.com/GalinaR15/g_auto_and_deploy.git
- папка
  cd g_auto_and_deploy
-устанавливаем зависимости
  pip install -r requirements.txt
- формируем файлы с данными о продажах
  python3 generate_sales_data.py
- создаем БД
  psql -U postgres -f sql/DLL -d auto_and_deploy
- настраиваем подключение к БД (файл config.ini -> [DB])
- импортируем данные в БД
  python3 import_sales_data_db.py
- настраиваем автоматизацию с помощью планировщика windows или cron (Linux) для выгрузок каждый день
  для Linux (cron):
  	- запускаем в терминале
  	  EDITOR = nano crontab -e
  	- генерация продаж
  	  00 22 * * 1-6 /home/auto_and_deploy/venv/bin/python /home/auto_and_deploy/generate_sales_data.py
  	- импорт данных в бд
  	  00 23 * * 1-6 /home/auto_and_deploy/venv/bin/python /home/auto_and_deploy/import_sales_data_db.py
  для Windows см.скриншоты по настройке расписания в папке IMG




