# -*- coding: utf-8 -*-
'''
Created on 2015年5月26日

@author: Administrator
'''

import time
import threading

def newtread(t):
    time.sleep(t)

t = threading.Thread(target=newtread, args=(10,))
t.daemon = False # 设置为后台线程
t.start()
print("start")
