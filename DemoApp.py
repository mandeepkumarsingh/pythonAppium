import time
import unittest
import os
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class DemoAppium():
    def setUp(self) :
        str=f'{os.popen("pwd").read().rstrip()}/data/apps/ApiDemos-debug.apk'
        print(str)
        desirecap={
            "device":"Android",
            "deviceName": "emulator-5554",
            "platformName": "Android",
            "appPackage": "io.appium.android.apis",
            "appActivity" : "io.appium.android.apis.ApiDemos",
           # "app":str
        }
        self.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desirecap);
    def scrollDown(self):
        for i in range(9):
            touch=TouchAction(self.driver)
            touch.press(x=318,y=940).move_to(x=338,y=476).release().perform()
            time.sleep(5)
    def test_Assignment_task(self):
        self.setUp()
        self.driver.implicitly_wait(30)
        """"Assignment2 Task 1 """
        preference=self.driver.find_element_by_xpath("//android.widget.TextView[@text='Preference']")
        preference.click()
        print("clicked on the Preference")
        """"Assignment2 task 2 """
        preferenceDependencies=self.driver.find_element_by_xpath("//android.widget.TextView[@text='3. Preference dependencies']")
        preferenceDependencies.click()
        print("Clicked on Prefrences Dependencies")
        """"Assignment2 task 3 """
        wifi=self.driver.find_element_by_id("android:id/checkbox")
        wifi.click()
        print("checked  on Wifi")
        """"Assignment2 task 4 """
        wifiSetting=self.driver.find_element_by_xpath("//android.widget.LinearLayout[@index='2']/android.widget.RelativeLayout[@index='0']")
        wifiSetting.click()
        """"Assignment2 task 5 """
        print("clicked on the  Wifi Settings")
        wifiSetting_Name= self.driver.find_element_by_class_name("android.widget.EditText");
        wifiSetting_Name.send_keys("Hello")
        print("entered  the  Wifi Settings name")
        """"Assignment2 task 6 """
        wifi_Setting_ok_button=self.driver.find_element_by_class_name("android.widget.Button")
        wifi_Setting_ok_button.click()
        print("click on  the  Wifi Settings Ok option ")
        """"Assignment2 task 7 """
        time.sleep(10)
        self.driver.back()
        print("backed once")
        time.sleep(10)
        self.driver.back()
        print("backed twice")
        views=self.driver.find_element_by_xpath("//*[@text='Views']")
        views.click()
        self.scrollDown()
        print("Scrolled")
        textClock = self.driver.find_element_by_xpath("//*[@text='TextClock']")
        textClock.click()
        print("clicked on textclock")
        """"Assignment2 task 8 """

ct=DemoAppium();
ct.test_Assignment_task()