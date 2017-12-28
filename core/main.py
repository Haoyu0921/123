#!/user/bin/env python3
# -*- coding: utf-8 -*-
#@Author : Arthur SUN
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from core import login,ATM,accounts

user_status = {
    'status':False,
    'user_data':None,
}
def shopping():
    print("shopping")
@login.login
def atm():
    print(user_status['user_data'])
    while True:
        print("1.用户信息\n2.转账\n3.存款\n4.取款\n5.还款\n6.管理员入口\n7.注销")
        menu_atm = {
            '1': ATM.select,
            '2': ATM.transfer,
            '3': ATM.save,
            '4': ATM.withdraw,
            '5': ATM.repay,
            '6': ATM.admin,
            '7':ATM.logoff
        }
        choice = input('>>')
        if choice in menu_atm:
            #执行函数
            accounts.loads(user_status['user_data']['name'])
            menu_atm[choice](user_status['user_data'])
        else:
            print("请选择正确的选项")

def will_exit():
    exit("退出成功")
def run():
    print("1.购物车\n2.ATM\n3.退出程序")
    menu_nologin = {
        1:shopping,
        2:atm,
        3:will_exit
    }
    choice = input(">>")
    choice = int(choice)
    if choice in menu_nologin:
        #调试
        # print('choice:',choice)
        # print(menu_nologin[choice])
        #执行函数
        menu_nologin[choice]()