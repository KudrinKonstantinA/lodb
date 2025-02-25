import db
import sys
import time
def logo():
    print('///        ///-----\\\\\\       |||-----\\\\\\  |||-----\\\\\\')
    print('///        |||     |||       |||     |||  |||     |||')
    print('///        |||     |||       |||     |||  |||-----///')
    print('///        |||     |||       |||     |||  |||-----\\\\\\')
    print('///        |||     |||       |||     |||  |||     |||')
    print('/////////  \\\\\\-----///       |||-----///  |||-----///')
    print('')
    print('-------------------------------------------------------')
    print('')
    print('Hello, user!')


splt = {
    'exit' : {
        'name' : 'exit', 
        'error' : '', 
        'arg' : None
    }, 
    'CREAT' : {
        'name' : None, 
        'error' : 'What to creat?', 
        'arg' : {
            'DATABASE' : {
                'name' : 'CREAT_DB',
                'error' : 'What is the name of the database?',
                'arg' : {
                    'input' : {
                        'name' : 'input',
                        'error' : '',
                        'arg' : None
                    }
                }
            }
        }
    },
    'SHOW' : {
        'name' : None,
        'error' : 'What to show?',
        'arg' : {
            'DATABASE' : {
                'name' : 'SHOW_DB',
                'error' : '',
                'arg' : None
            }
        }
    },
    'DROP' : {
        'name' : None, 
        'error' : 'What to drop?', 
        'arg' : {
            'DATABASE' : {
                'name' : 'DROP_DB',
                'error' : 'What is the name of the database?',
                'arg' : {
                    'input' : {
                        'name' : 'input',
                        'error' : '',
                        'arg' : None
                    }
                }
            }
        }
    }
}   
def exit():
    print('Goodbay, user!')
    time.sleep(1)
    sys.exit(0) 

def user():
    global is_bool 
    is_bool= False
    query = input("\033[0mlodb>")
    if len(query.split()) > 0:
        #ЕСЛИ БОЛЬШЕ 0 АРГУМЕНТОВ
        for i1 in splt:
            if query.split()[0] == i1:
                if splt[i1]['error'] == '' and splt[i1]['name'] != None:
                    a = splt[i1]['name']
                    globals()[a]()
                    is_bool = True
                    break
                elif len(query.split()) > 1:
                    #ЕСЛИ БОЛЬШЕ 1 АРГУМЕНТА
                    for i2 in splt[i1]['arg']:
                        if splt[i1]['arg'][i2]['error'] == '' and splt[i1]['arg'][i2]['name'] != None:
                            if splt[i1]['arg'][i2]['name'] == 'input':
                                a = splt[i1]['name']
                                fun = getattr(db, a)
                                fun(query.split()[2])
                                is_bool = True
                                break
                            else:
                                a = splt[i1]['arg'][i2]['name']
                                fun = getattr(db, a)
                                fun()
                                is_bool = True
                                break
                        elif len(query.split()) > 2:
                            #ЕСЛИ БОЛЬШЕ 2 АРГУМЕНТОВ
                            for i3 in splt[i1]['arg'][i2]['arg']:
                                if splt[i1]['arg'][i2]['arg'][i3]['error'] == '' and splt[i1]['arg'][i2]['arg'][i3]['name'] != None:
                                    if splt[i1]['arg'][i2]['arg'][i3]['name'] == 'input':
                                        a = splt[i1]['arg'][i2]['name']
                                        fun = getattr(db, a)
                                        fun(query.split()[2])
                                        is_bool = True
                                        break
                                    else:
                                        a = splt[i1]['arg'][i2]['arg'][i3]['name']
                                        fun = getattr(db, a)
                                        is_bool = True
                                        break
                                else:
                                    print(splt[i1]['arg'][i2]['arg'][i3]['error'])
                                    is_bool = True
                                    break
                        else:
                            print(splt[i1]['arg'][i2]['error'])
                            is_bool = True
                            break
                else:
                    print(splt[i1]['error'])
                    is_bool = True
                    break

    if is_bool == False:
        print('\033[31mNotFoundCommand')   

def prog():
    query = sys.argv
    if len(query) > 1:
        if query[1] == "CREAT":
            if len(query) > 2:
                if  query[2] == "DATABASE":
                    if len(query) > 3:
                        db.CREAT_DB(query[3])
                        sys.exit()
                    else:
                        print('WARNING:The name of the database being created is not specified')
                        sys.exit()
                else:
                    print('ERROR:NotFoundCommand')
                    sys.exit()
            else:
                print('WARNING:The type of the object being created is not specified')
                sys.exit()
        elif query[1] == "SHOW":
            if  query[2] == "DATABASE":
                db.SHOW_DB()
            else:
                print('ERROR:NotFoundCommand')
                sys.exit()
        else:
            print('ERROR:NotFoundCommand')
            sys.exit()

if len(sys.argv) > 1:
    prog()

if len(sys.argv) < 2:
        logo()

while True:
    if len(sys.argv) < 2:
        user()
    