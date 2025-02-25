import json
import os
import shutil
ensure_ascii=False
def CREAT_DB(name_db):
    try:
        with open('./db/db.json', 'r', encoding='utf-8') as file:
            db_list = json.load(file)
            db = db_list
            db_list = list(db_list.keys())
            for i in db_list:
                if i == name_db:
                    return f'Database {name_db} already exists. Choose a different database name.'
            with open('./db/db.json', 'w', encoding='utf-8') as file:
                pathtable = f'./db/{name_db}/table.json'
                path = f'./db/{name_db}'
                db[name_db] = {}
                db[name_db]["name"] = name_db
                db[name_db]["path"] = path
                db[name_db]["table"] = pathtable
                json.dump(db, file)
                print(f'Database {name_db} was created successfully. \r\n')
                os.makedirs(path, exist_ok=True)
                print(f'Database derectory {path} was created successfully. \r\n')
                with open(pathtable, 'w') as file:
                    print(f'Database table file {pathtable} was created successfully.')
    except Exception:
        print('An unexpected error has occurred')

def SHOW_DB():
    try:
        with open('./db/db.json', 'r', encoding='utf-8') as file:
            db_list = json.load(file)
            db_list = list(db_list.keys())
            msg = ''
            for i in db_list:
                msg = msg + i + '\n'
            print(msg)
    except Exception:
       print('An unexpected error has occurred')

SHOW_DB()

def DROP_DB(name_db):
    try:
        with open('./db/db.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            shutil.rmtree(data[name_db]['path'])
            with open('./db/db.json', 'w', encoding='utf-8') as file:
                del data[name_db]
                json.dump(data, file)
    except (KeyError, FileNotFoundError):
        print(f'The database {name_db} of favorites has not been created yet.')

