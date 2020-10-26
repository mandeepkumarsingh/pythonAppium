import unittest
import os
from appium import webdriver
class DemoAppium():
    def setUp(self) :
        str=f'{os.popen("pwd").read().rstrip()}/data/apps/ApiDemos-debug.apk'
        ##str=str+"/data/app/ApiDemos-debug.apk",

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
    def test_Assignment_task(self):
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

ct=DemoAppium();
ct.setUp()
ct.test_Assignment_task()