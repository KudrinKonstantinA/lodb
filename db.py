import json
import os
import shutil
ensure_ascii=False

global use_db
use_db = None

#Database functions
def CREATE_DB(*args):
    if len(args) > 0:
        db_name = args[0]
        try:
            with open('./db/db.json', 'r', encoding='utf-8') as file:
                db_list = json.load(file)
                db = db_list
                db_list = list(db_list.keys())
                for i in db_list:
                    if i == db_name:
                        print(f'Database {db_name} already exists. Choose a different database name.')
                        return 1
                with open('./db/db.json', 'w', encoding='utf-8') as file:
                    pathtable = f'./db/{db_name}/table.json'
                    path = f'./db/{db_name}'
                    db[db_name] = {}
                    db[db_name]["name"] = db_name
                    db[db_name]["path"] = path
                    db[db_name]["table"] = pathtable
                    json.dump(db, file)
                    os.makedirs(path, exist_ok=True)
                    with open(pathtable, 'w') as file:
                        table = {'schema': {'name': 'schema', 'path' : 'schema', 'data' : 'schema/data.json'}}
                        json.dump(table, file)
                        os.makedirs(f'{path}/schema', exist_ok=True)
                        with open(f'{path}/schema/data.json', 'w') as file:
                            print(f'Database {db_name} was created successfully.')
        except Exception:
            print('An unexpected error has occurred')
    else:
        print('None arguments')

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


def DROP_DB(*args):
    if len(args) > 0:
        db_name = args[0]
        try:
            with open('./db/db.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
                shutil.rmtree(data[db_name]['path'])
                with open('./db/db.json', 'w', encoding='utf-8') as file:
                    del data[db_name]
                    json.dump(data, file)
                    print(f'The database {db_name} deleted successfully')
        except (KeyError, FileNotFoundError):
            print(f'The database {db_name} of favorites has not been created yet.')
    else:
        print('None arguments')

def USE_DB(*args):
    if len(args) > 0:
        db_name = args[0]
        try:
            global use_db
            with open('./db/db.json', 'r', encoding='utf-8') as file:
                    db_list = json.load(file)
                    db_list = list(db_list.keys())
                    for i in db_list:
                        if i == db_name:
                            use_db = db_name
                            print('Using database')
                            return 0
                    print(f'The database {db_name} of favorites has not been created yet.')
                    return 1
        except Exception:
            print('An unexpected error has occurred')
    else:
        print('None arguments')

#Table function
def CREAT_TABLE(*args):
    if len(args) > 0:
        table_name = args[0]
        global use_db
        try:
            if use_db != None:
                db_name = use_db
                with open(f'./db/{db_name}/table.json', 'r', encoding='utf-8') as file:
                    tables_list = json.load(file)
                    tables = tables_list
                    tables_list = list(tables_list.keys())
                    for i in tables_list:
                        if i == table_name:
                                print(f'Tables {table_name} in database {db_name} already exists. Choose a different table name.')
                        with open(f'./db/{db_name}/table.json', 'w', encoding='utf-8') as file:
                            pathdata = f'./db/{db_name}/{table_name}/data.json'
                            path = f'./db/{db_name}/{table_name}'
                            tables[table_name] = {}
                            tables[table_name]["name"] = db_name
                            tables[table_name]["path"] = path
                            tables[table_name]["table"] = pathdata
                            json.dump(tables, file)
                            os.makedirs(path, exist_ok=True)
                            with open(pathdata, 'w') as file:
                                print(f'Table {table_name} was created successfully.')
            else:
                print('None database use')
        except Exception:
            print('An unexpected error has occurred')
    else:
        print('None arguments')

