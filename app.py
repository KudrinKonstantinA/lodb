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

def exit():
    print('Goodbay, user!')
    time.sleep(1)
    sys.exit(0) 

def user(qerry):
    parts = qerry.strip().split()
    if len(parts) > 0:
        i = 0
        while i < len(parts):
            found = False
            for cmd in sorted(commands.keys(), key=lambda x: -len(x)):
                cmd_len = len(cmd)
                if i + cmd_len <= len(parts) and tuple(parts[i:i+cmd_len]) == cmd:
                    func = commands[cmd]
                    args = parts[i+cmd_len:]
                    func(*args)
                    i += cmd_len
                    found = True
                    return
            if not found:
                i += 1 

        for a in commands:
            list1 = list(a)
            for b in list1:
                for c in parts:
                    if b == c:
                        print('Incomplete command')
                        return

commands = {
    ("CREATE", "DATABASE"): db.CREATE_DB,
    ("SHOW", "DATABASE"): db.SHOW_DB,
    ("DROP", "DATABASE"): db.DROP_DB,
    ("USE",): db.USE_DB,
    ("exit",): exit,
}

logo()
while True:
    if db.use_db != None:
        qerry = input(f"lodb>{db.use_db}>")
        user(qerry)
    else:
        qerry = input(f"lodb>")
        user(qerry)
while True:
    if len(sys.argv) < 2:
        user()
    
