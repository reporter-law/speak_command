"""程序说明"""
# -*-  coding: utf-8 -*-
# Author: cao wang
# Datetime : 2020
# software: PyCharm
# 收获:
import os
from sys import path
path_=os.path.abspath(os.path.dirname(__file__))
path.append(path_)
from command_tasks.baidu_spider import baidu_spider as bs
from command_tasks.WeatherAPITest import weather_main as wm
from command_tasks.cnki import main
from command_tasks.time_know import get_time as gt
import speak_command as sc
from command_tasks.selenium_csdn import csdn_main as cm


def task_api(text,option):
    print(text)
    time_words = ["几点钟", "时间","今天","现在"]
    if "查询" in text :
        if "天气" in text:
            """天气查询"""
            if option == 1:
                if len(text) > 2:
                    print("请确认任务名称： ", text[1:])
                    for i in text:
                        if "市" in i:
                            print("任务正在进行中")
                            wm(i.strip("市"))
            elif option == 0:
                print("任务正在进行中")
                wm(text[1])
        else:
            #print("".join(text[1:]))
            text = bs("".join(text[1:]))
            sc.Sound_from_text().sound(text)


    elif "爬取" in text:
        #print("此任务暂不开放...")
        print("任务正在进行中")
        main(text[1])

    elif text[0] =="执行":
        #print("相关任务建设中...")

        if "阅读" in text and "任务" in text:
            print("开始执行阅读量增加任务")
            cm()


    elif map(lambda x:x in text,time_words):
        text = gt()
        sc.Sound_from_text().sound(text)
        print(text)
    else:
        print("相关任务建设中...")





