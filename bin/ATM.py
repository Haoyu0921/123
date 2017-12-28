#!/user/bin/env python3
# -*- coding: utf-8 -*-
#@Author : Arthur SUN
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from core import main

print(BASE_DIR)  #调试使用
if __name__ == '__main__':
    main.run()