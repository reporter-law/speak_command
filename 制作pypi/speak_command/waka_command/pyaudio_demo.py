"""程序说明"""
# -*-  coding: utf-8 -*-
# Author: cao wang
# Datetime : 2020
# software: PyCharm
# 收获:
import wave
import pyaudio


def record(filename):
    """官方录音教程,,增加了音量以及时间计算的录音退出功能
    """
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100  # 读取速度
    RECORD_SECONDS = 5  # 记录秒数
    second = 10
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,channels=CHANNELS,rate=RATE,input=True,
        frames_per_buffer=CHUNK)

    frames = []#录音列表
    print("\r唤醒语音识别开始.......................................", end="")
    for i in range(100):
        data = stream.read(CHUNK, exception_on_overflow=False)
        frames.append(data)
    print("\r唤醒语音识别结束.......................................",end="")
    stream.stop_stream()
    stream.close()
    p.terminate()
    """存储写入"""
    wf = wave.open(filename, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    return filename
filename = r"J:\PyCharm项目\学习书籍成果\其他库\语音识别\语音文件\确认语音.wav"
#record(filename)