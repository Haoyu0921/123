#!/user/bin/env python3
# -*- coding: utf-8 -*-
#@Author : Arthur SUN
import time
from core import accounts
from config import settings
def repay(user_data):
    pass
def transfer(user_data):
    pass
def withdraw(user_data):
    while True:
        money = input("请输入取出的金额：")
        if money.isdigit():
            money = int(money)
            lixi = money*settings.ATM_SETTINGS['withdraw']['interest'] /100
            user_data['money'] = user_data['money'] - money
            accounts.dumps(user_data)
            break
        else:
            print("请输入数字：")
def save(user_data):
    pass
def admin(user_data):
    pass
def select(user_data):
    print(
        "------ 用户信息 ------\n"
        "用户名：%s\n"
        "可透支：%s元\n"
        "存款：%s元\n"
        "----------------------"%(user_data['name'],user_data['credit'],user_data['money'])
    )
    time.sleep(1)
def logoff(user_data):
    pass