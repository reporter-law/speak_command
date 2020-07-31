"""程序说明"""
# -*-  coding: utf-8 -*-
# Author: cao wang
# Datetime : 2020
# software: PyCharm

from setuptools import setup, find_packages

setup(
    # pip install nnn
    name="speak_command",
    version="0.1.0",
    keywords=["baidu-aip", "speech_recognition", "pyaudio"],
    description="语音控制，增加了唤醒命令以及程序任务接口、部分接口程序",
    long_description="实现语音唤醒，基于调度命令长期调度直到唤醒命令，实现语音输入输出；"
                     "综合了语音转文本、文本转语音、录音、自然语言处理、爬虫等技术；"
                     "实现语音控制，依据传入命令调动该命令意图实现的程序，当然这需要任务程序的接口；"
                     "依据任务程序的数量实现程序泛化",
    # 协议
    license="GPL Licence",

    url="https://github.com/reporter-law/speak_command",
    author="cw",
    author_email="1063117365@qq.com",

    # 自动查询所有"__init__.py"
    python_requires = '>=3.7.*',
    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    # 提示前置包
    install_requires=['pyaudio',
                      'requests',
                      'pydub',
                      'baidu-aip',
                      'numpy',
                      'jieba',
                      'fuzzywuzzy',
                      'SpeechRecognition',
                      "schedule",
                      'lxml',
                      'selenium',
                      ]
)
#"speech_recognition"3.8.1需要这个包，但是pip install speak_command时不行，只能用的时候自行下载