# 天气语音播报
# 1. 输入城市
# 2. 发送请求api，得到天气信息
# 3. 筛选信息，选取需要的内容，并处理
# 4. 使用百度语音，baidu-aip,生成mp3
# 5. 播报信息

# 导入的模块
import requests                                     # 用于请求天气信息
from aip import AipSpeech                           # 用于文本合成语音
from pydub import AudioSegment
from pydub.playback import play# 用于播放语音
import os,sys                                # 文件清理

# 发送请求api，得到天气信息
def getWeather_infor(city):

    url = "http://apis.juhe.cn/simpleWeather/query?"    # 请求的地址头部
    params = {                                          # 地址参数
        "city": city,
        "key": "a1967d854996051f711fd48a456b6c1e"
    }
    resp = requests.get(url, params=params).json()       # 发出请求,使用json()，返回了字典类型数据
    return  resp


# 筛选信息，选取需要的内容，并处理
def select_info(resp):
    
    if resp["result"]:  # 请求成功
        realtime_Weather = resp["result"]["realtime"]           # 当前温度
        day_Weather = resp["result"]["future"][0]               # 当天天气
        temp = day_Weather["temperature"].split("/")            # 分割最低温度和最高温度
        speak_content = f'当前温度是{realtime_Weather["temperature"]}℃,相对湿度{realtime_Weather["humidity"]}%' \
                        f',天气：{realtime_Weather["info"]},{realtime_Weather["direct"]},' \
                        f'强度：{realtime_Weather["power"]}。\n' \
                        f'温度范围：{temp[0]}--{temp[1]},天气变化：{day_Weather["weather"]}'
    else:
        speak_content = resp["reason"]
    return speak_content


# 使用百度语音，baidu-aip,生成mp3
def create_Mp3(content):
    APP_ID = '19236313'
    API_KEY = 'gZ4E58quu5HgFalbda9ktNl7'
    SECRET_KEY = 'QzGPaVmFUQoSZGO1zbr18MAzldmKY01K'

    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)            # 获取一个在线请求的client
    result = client.synthesis(content, 'zh', 1, {'spd':6,'vol': 5})  # 设置并获取返回语音的二进制文件流

    if not isinstance(result, dict):                           # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
        path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))+"\\temp"
        if not os.path.exists(path):
            os.makedirs(path)
        path = path+'\\auido.mp3'
        with open(path, 'wb') as f:
            f.write(result)

def cleanMp3():
    path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))+"\\temp\\auido.mp3"
    if os.path.exists(path):
        os.remove(path)
        #print("语音文件已经清除了..........")


# 主函数, 程序的主体
def weather_main(city):

    print("-"*20,"天气播报程序","-"*20)

    city = city
    if city != 'exit':
        resp = getWeather_infor(city)  # 发送请求api，得到天气信息
        
        we_con = select_info(resp)  # 筛选信息，选取需要的内容，并处理
        we_con = "当前城市为： {},    ".format(city) + we_con
        print(we_con)
        create_Mp3(we_con)  # 使用百度语音，baidu-aip,生成mp3
         # 天气的文字输出
        path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))+"\\temp\\auido.mp3"
        
        audio = AudioSegment.from_mp3(path)
     
        play(audio)  # 天气的语音输出
    else:
        print("程序退出")

    cleanMp3()
#weather_main("郴州")





























