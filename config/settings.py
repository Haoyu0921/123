#!/user/bin/env python3
# -*- coding: utf-8 -*-
# Author : Arthur SUN

"""配置文件"""
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATABASE = {
    'engine': 'file_storage',
    'name':'accounts',
    'path': r"%s\doc\users" % BASE_DIR
}
SOPPPING_MENU = {
    1:{'name':'书','price':100},
    2:{'name':'手机','price':2000},
    3:{'name':'单车','price':2300},
    4:{'name':'客车','price':1000000},
    5:{'name':'轿车','price':100000}
}

ATM_SETTINGS = {
    'withdraw':{'name':'None','action':'plus','interest':0.05},
    'save':{'name':'None','action':'plus','interest':0},
    'tracefor':{'name':'None','action':'special','interest':0}
}