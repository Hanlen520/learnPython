#!/user/bin/env python
# -*- coding:utf-8 -*-
from appium import webdriver
import time

def main():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '4.4.2'
    desired_caps['deviceName'] = 'ead1cc4a'
    desired_caps['appPackage'] = 'com.lianchuan.kaledai'
    desired_caps['appActivity'] = 'com.lianchuan.kaledai.activity.SplashActivity'

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    time.sleep(10)
    driver.find_element_by_id('com.lianchuan.kaledai:id/repay').click()

    driver.quit()

if __name__ == '__main__':
    main()


