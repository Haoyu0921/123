#!/user/bin/env python3
# -*- coding: utf-8 -*-
#@Author : Arthur SUN
#登录模块
import json
import os

from core import main

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
"""调试
print(BASE_DIR)
"""
def login(fnc):
    """用于登录使用的装饰器"""
    def exterior(*args,**kwargs):
        while True:
            name = input("username:")
            password = input("password:")
            with open(r'%s\doc\users\%s.json' % (BASE_DIR, name), "r") as f:
                main.user_status['user_data'] = json.loads(f.read())
            if name == main.user_status['user_data']['name'] and password == main.user_status['user_data']['password']:
                if main.user_status['user_data']['is_lock'] >= 3:
                    print('用户已经被锁定，请联系管理员解锁')
                    break
                else:
                    main.user_status['user_data']['is_lock'] = 0
                    main.user_status['status'] = True
                    fnc(*args, **kwargs)
                    break
            else:
                print('用户名或者密码错误')
                main.user_status['user_data']['is_lock'] += 1
    return exterior
try :
    with open(r'%s\doc\users\admin.json'%BASE_DIR,"r") as f:
        pass
except FileNotFoundError:
    name = {
        'name':'admin',
        'password':'admin',
        'money':None,
        'is_admin':True,
        'credit':0,
        'is_lock':0
    }
    with open(r'%s\doc\users\admin.json'%BASE_DIR,'w') as f:
        f.write(json.dumps(name))