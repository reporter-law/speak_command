"""程序说明"""
# -*-  coding: utf-8 -*-
# Author: cao wang
# Datetime : 2020
# software: PyCharm
# 收获:
from datetime import datetime

def get_time():

    now = datetime.today()
    now = now.strftime('当前时间为:%H时%M分%S秒')
    return now
#print(get_time())