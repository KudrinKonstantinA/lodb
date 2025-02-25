import shutil
import os
import json
import requests


def install():
    url = 'https://github.com/lo-proger/lodb/releases/download/Beta/lodb.exe'
    save_path = './lodb.exe'
    response = requests.get(url)

    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)
            print("OK")
    else:
        print(f"Error: {response.status_code}")

    os.makedirs('./db', exist_ok=True)
    print('Databases derectory ./db was created successfully. \r\n')
    with open('./db/db.json', 'w', encoding='utf-8') as file:
        print('Databases file ./db/db.json was created successfully. \r\n')
        db = {"system": {"name": "system", "path": "db/system", "table": "db/system/table.json"}}
        json.dump(db, file)
        print('Database system was created successfully. \r\n')
        os.makedirs('./db/system', exist_ok=True)
        print('Database derectory ./db/system was created successfully. \r\n')
        with open('./db/system/table.json', 'w', encoding='utf-8') as file:
            print('Database table file ./db/system/table.json was created successfully.')

def uninstall():
    shutil.rmtree('./db')
    os.remove('lodb.exe')
    os.remove('PackManager.exe')

text = input('PK>')
if text == 'install':
    install()
elif text == 'uninstall':
    uninstall()
