#!/user/bin/env python3
# -*- coding: utf-8 -*-
# Author : Arthur SUN
import json
import os
import time
from core import main
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def loads(account_name):
    with open(r"%s\doc\users\%s.json" % (BASE_DIR, account_name), 'r') as f:
        main.user_status['user_data'] = json.loads(f.read())
def dumps(account):
    with open(r"%s\doc\users\%s.json" % (BASE_DIR, account['name']), 'w') as f:
        print(account)
        f.write(json.dumps(account))
        time.sleep(2)
        #main.user_status['user_data'] = json.dumps(account)