import db
import sys
import time

def exit():
    print('Goodbay, user!')
    time.sleep(1)
    sys.exit(0) 

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

commands = {
    ("CREATE", "DATABASE", "arg"): db.CREATE_DB,
    ("SHOW", "DATABASE"): db.SHOW_DB,
    ("DROP", "DATABASE", "arg"): db.DROP_DB,
    ("USE", "arg"): db.USE_DB,
    ("EXIT",): exit,
    ("CREATE", "TABLE", "arg"): db.CREAT_TABLE,
}

def user(query):
    query = query.strip().split()
    query_commands = []  
    query_args = [] 

    for word in query:
        if word.isupper():
            query_commands.append(word)
        else:
            query_args.append(word)
            query_commands.append("arg")

    if len(query_commands) > 0:
        i = 0
        while i < len(query_commands):
            for cmd in sorted(commands.keys(), key=lambda x: -len(x)):
                cmd_len = len(cmd)
                if i + cmd_len <= len(query_commands) and tuple(query_commands[i:i+cmd_len]) == cmd:
                    func = commands[cmd]
                    args = query_args
                    func(*args)
                    return
            i += 1 

        for a in commands:
            list1 = list(a)
            for b in list1:
                for c in query_commands:
                    if b == c:
                        print('Incomplete command')
                        return

logo()                   
while True:
    if db.use_db != None:
        query = input(f"lodb>{db.use_db}>")
        user(query)
    else:
        query = input(f"lodb>")
        user(query)
