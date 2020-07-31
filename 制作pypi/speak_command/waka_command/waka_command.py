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
from pyaudio_demo import record as r
import os
from PocketSphinx import know_file as kf
import speak_command as sc
import schedule
from command_api import task_api as wa
import jieba
import logging
jieba.setLogLevel(logging.INFO)


def wake_speak():
    """语音唤醒"""

    filename = path_+"\\temp"
    if not os.path.exists(filename):
        os.makedirs(filename)
    file = filename+"\\waking.wav"
    r(file)
    text = kf(file)
    #print(text)
    try:
        name = ["先惠","贤惠","先会","新会","监会","同学"]

        #print(type(list(map(lambda x:x in text,name))[0]))#布尔值
        if True in list(map(lambda x:x in text,name)):
            print("进去正式命令读取阶段")
            # filepath的存在影响语音命令接口
            # filepath = r"J:\pyinstaller\Python3.8版本项目\语音命令库\speak_command\speak_command\Step1_1_StatsGov.txt"
            filepath = ""
            if filepath == "":
                option = 0
                text = sc.command_speak()
                wa(text, option)
            else:
                option = 1
                text = sc.command_speak(filepath)
                wa(text, option)
        else:
            print("\r非唤醒命令", end="")
    except Exception as e:
        print(e)



def schedule_waka():
    schedule.every(1).seconds.do(wake_speak)

    while True:
        # print("语音交互项目建设中")
        # break
        schedule.run_pending()
#schedule_waka()
