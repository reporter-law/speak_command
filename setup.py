"""程序说明"""
# -*-  coding: utf-8 -*-
# Author: cao wang
# Datetime : 2020
# software: PyCharm

from setuptools import setup, find_packages

setup(
    # pip install nnn
    name="speak_command",
    version="0.0.6",
    keywords=("baidu-aip", "speech_recognition", "pyaudio"),
    description="语音控制",
    long_description="实现语音输入输出，综合组合了语音转文本、文本转语音、录音、自然语言处理等技术，实现语音控制 ",
    # 协议
    license="GPL Licence",

    url="https://github.com/reporter-law/speak_command",
    author="cw",
    author_email="1063117365@qq.com",

    # 自动查询所有"__init__.py"
    python_requires = '>=3.8.*',
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
                      'SpeechRecognition']
)
#"speech_recognition"3.8.1需要这个包，但是pip install speak_command时不行，只能用的时候自行下载