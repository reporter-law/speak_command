"""程序说明"""
# -*-  coding: utf-8 -*-
# Author: cao wang
# Datetime : 2020
# software: PyCharm
# 收获:
import speech_recognition as sr


r = sr.Recognizer()

def file_open(file):
    # 打开语音文件
    audio_file = file.strip('\u202a')
    with sr.AudioFile(audio_file) as source:
        audio = r.record(source)
    return audio

def know_file(file):
    """语音识别"""

    if file.split("\\")[-1].split(".")[1] == "wav" :#注意此处的路径分割
        #text = "音频文件格式正确，可以直接进行语音识别"
        #print(r.recognize_google(file_open(file),language="zh_CN"))
        try:
            try:
                return r.recognize_google(file_open(file), language='zh_CN')
            except:
                res = r.recognize_google(file_open(file), language='zh_CN', show_all=True)  # 汉语
                if res == []:
                    return "无命令"
                else:
                    return res["alternative"][0]["transcript"]
        except Exception:
            return Exception

#text = know_file(r"J:\test2.wav".strip("\u202a"))
#print(text)
