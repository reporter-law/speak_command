# -*-  coding: utf-8 -*-
# Author: caowang
# Datetime : 2020
# software: PyCharm
from selenium import webdriver
from selenium.webdriver import FirefoxProfile
import time
import random
from selenium.webdriver.firefox.options import Options


sec = random.randint(1,2)
'''randint生成整数'''
def csdn():
    sec = random.randint(1, 5)
    ops = Options()
    #driver = webdriver.Chrome(r'd:\xxx\chromedriver.exe')
    #原因：可能是chrome未在系统盘注册


#selenium.common.exceptions.WebDriverException: Message: unknown error: DevToolsActivePort file doesn't exist

#解决办法

#禁用sandbox
    '''
    ops.add_argument('--no-sandbox')
    ops.add_argument('--disable-dev-shm-usage')


    ops.add_argument('window-size=1920x3000')  # 指定浏览器分辨率
    ops.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
    ops.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面
    ops.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
    '''
    profile = FirefoxProfile()
    profile.set_preference('browser.migration.version', 9001)
    profile.set_preference('permissions.default.image', 2)
    ops.add_argument('--headless')


    browser = webdriver.Firefox(profile,options=ops)

    browser.implicitly_wait(1)
    browser.get('https://blog.csdn.net/python__reported')
    index = 1

    for i in range(20, 60):
        try:
            button1 = browser.find_element_by_xpath('/html/body/div[6]/main/div[2]/div[%d]/h4/a' % index)
            # print('第%d篇文章浏览中。。。。。。。。。。。。。。。。。。。。。。'  %index)
            button1.click()

            browser.switch_to.window(browser.window_handles[1])#由于是火狐浏览器
            '''firefox原因不明，一定要移动一次'''
            browser.close()
            browser.switch_to.window(browser.window_handles[0])
            time.sleep(1)
            index += 1
            print("\r第%d页阅读量增加中.............................."%index,end="")
        except:
            pass
    browser.quit()
    print('浏览器关闭成功.............................................................',end="")



'''
xpath地址更换
    for it in range(sec):
        browser.switch_to.window(browser.window_handles[0])  # Message: no such window: target window already closed
        button_2 = browser.find_element_by_xpath('//*[@id="mainBox"]/main/div[2]/div[2]/h4/a"href"][')
        button_2.click()
        time.sleep(sec)
        browser.switch_to.window(browser.window_handles[1])
        browser.close()
    for it in range(sec):
        browser.switch_to.window(browser.window_handles[0])
        button_3 = browser.find_element_by_xpath('//*[@id="mainBox"]/main/div[2]/div[3]/h4/a["href"]')
        button_3.click()
        time.sleep(sec)
        browser.switch_to.window(browser.window_handles[1])
        browser.close()

    for it in range(sec):
        browser.switch_to.window(browser.window_handles[0])
        button_4 = browser.find_element_by_xpath('//*[@id="mainBox"]/main/div[2]/div[4]/h4/a["href"]')
        button_4.click()
        time.sleep(sec)
        browser.switch_to.window(browser.window_handles[1])
        browser.close()

    browser.switch_to.window(browser.window_handles[0])
    button_5 = browser.find_element_by_xpath('//*[@id="mainBox"]/main/div[2]/div[5]/h4/a["href"]')
    button_5.click()
    time.sleep(sec)
    browser.switch_to.window(browser.window_handles[1])
    browser.close()

    browser.switch_to.window(browser.window_handles[0])
    button_8 = browser.find_element_by_xpath('//*[@id="mainBox"]/main/div[2]/div[8]/h4/a["href"]')
    button_8.click()
    time.sleep(sec)
    browser.switch_to.window(browser.window_handles[1])
    browser.close()

    browser.switch_to.window(browser.window_handles[0])
    button_9 = browser.find_element_by_xpath('//*[@id="mainBox"]/main/div[2]/div[9]/h4/a["href"]')
    button_9.click()
    time.sleep(sec)
    browser.switch_to.window(browser.window_handles[1])
    browser.close()

    browser.switch_to.window(browser.window_handles[0])
    button_10 = browser.find_element_by_xpath('//*[@id="mainBox"]/main/div[2]/div[10]/h4/a["href"]')
    button_10.click()
    time.sleep(sec)
    browser.switch_to.window(browser.window_handles[1])
    browser.close()

    browser.switch_to.window(browser.window_handles[0])
    button_11 = browser.find_element_by_xpath('//*[@id="mainBox"]/main/div[2]/div[11]/h4/a["href"]')

    button_11.click()
    time.sleep(sec)
    browser.switch_to.window(browser.window_handles[1])
    browser.close()

    browser.switch_to.window(browser.window_handles[0])
    button_12 = browser.find_element_by_xpath('//*[@id="mainBox"]/main/div[2]/div[12]/h4/a["href"]')
    button_12.click()
    time.sleep(sec)
    browser.switch_to.window(browser.window_handles[1])
    browser.close()

    browser.switch_to.window(browser.window_handles[0])
    button_13 = browser.find_element_by_xpath('//*[@id="mainBox"]/main/div[2]/div[13]/h4/a["href"]')
    button_13.click()
    time.sleep(sec)
    browser.switch_to.window(browser.window_handles[1])
    browser.close()

    browser.switch_to.window(browser.window_handles[0])
    button_14 = browser.find_element_by_xpath('//*[@id="mainBox"]/main/div[2]/div[14]/h4/a["href"]')
    button_14.click()
    time.sleep(sec)
    browser.switch_to.window(browser.window_handles[1])
    browser.close()

    browser.switch_to.window(browser.window_handles[0])
    button_15 = browser.find_element_by_xpath('//*[@id="mainBox"]/main/div[2]/div[15]/h4/a["href"]')
    button_15.click()
    time.sleep(sec)
    browser.switch_to.window(browser.window_handles[1])
    browser.close()

    browser.switch_to.window(browser.window_handles[0])
    button_16 = browser.find_element_by_xpath('//*[@id="mainBox"]/main/div[2]/div[16]/h4/a["href"]')
    button_16.click()
    time.sleep(sec)
    browser.switch_to.window(browser.window_handles[1])
    browser.close()

    browser.switch_to.window(browser.window_handles[0])
    button_17 = browser.find_element_by_xpath('//*[@id="mainBox"]/main/div[2]/div[17]/h4/a["href"]')
    button_17.click()
    time.sleep(sec)
    browser.switch_to.window(browser.window_handles[1])
    browser.close()

    browser.switch_to.window(browser.window_handles[0])
    button_18 = browser.find_element_by_xpath('//*[@id="mainBox"]/main/div[2]/div[18]/h4/a["href"]')
    button_18.click()
    time.sleep(sec)
    browser.switch_to.window(browser.window_handles[1])
    browser.close()

    for i in range(3):
        browser.switch_to.window(browser.window_handles[0])
        button_19 = browser.find_element_by_xpath('//*[@id="mainBox"]/main/div[2]/div[19]/h4/a["href"]')
        button_19.click()
        time.sleep(sec)
        browser.switch_to.window(browser.window_handles[1])
        browser.close()

    browser.switch_to.window(browser.window_handles[0])
    button_20 = browser.find_element_by_xpath('//*[@id="mainBox"]/main/div[2]/div[20]/h4/a["href"]')
    button_20.click()
    time.sleep(sec)
    browser.switch_to.window(browser.window_handles[1])
    browser.close()

    browser.switch_to.window(browser.window_handles[0])
    button_21 = browser.find_element_by_xpath('//*[@id="mainBox"]/main/div[2]/div[21]/h4/a["href"]')
    button_21.click()
    time.sleep(sec)
    browser.switch_to.window(browser.window_handles[1])
    browser.close()

    browser.switch_to.window(browser.window_handles[0])
    button_22 = browser.find_element_by_xpath('//*[@id="mainBox"]/main/div[2]/div[22]/h4/a["href"]')
    button_22.click()
    time.sleep(sec)
    browser.switch_to.window(browser.window_handles[1])
    browser.close()

    browser.switch_to.window(browser.window_handles[0])
    button_22 = browser.find_element_by_xpath('//*[@id="mainBox"]/main/div[2]/div[29]/h4/a["href"]')
    button_22.click()
    time.sleep(sec)
    browser.switch_to.window(browser.window_handles[1])
    browser.close()
'''


    # print('这是{number}次csdn阅读量的增加...................................................'.format(number=index))

    # browser.switch_to.window(browser.window_handles[0])
def csdn_main():
    index = 1
    for it in range(50):
        time.sleep(5)
        csdn()
        print('\r这是{number}次csdn阅读量的增加...................................................'.format(number=index),end="")
        index += 1

    print('\r点击量增加完结................................................................................................',end="")