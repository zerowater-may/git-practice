import uiautomator2 as u2
from time import time,sleep
from random import randint, uniform
import logging,getpass

class Insta_App:
    def __init__(self):
        super().__init__()
        # # 연결 테스트
        self.d = u2.connect() 
        self.app_package = 'com.instagram.android'
        # print(device.info)
        ## 앱 시작 

    def __random_sleep__(self, minimum=10, maximum=20):
        t = randint(minimum, maximum)
        sleep(t)

    def __wait_for_element__(self, element_tag, locator, ele,timeout=30, text=False):
        """Wait till element present. Max 30 seconds"""
        result = False
        # print(timeout)
        for i in range(timeout):
            try:
                if locator == 'xpath' and element_tag == 'click':
                    self.d.xpath(ele).click()
                    result = True
                    break
                elif locator == 'xpath' and element_tag == 'set_text' and text != False :
                    self.d.xpath(ele).set_text(text)
                    result = True
                    break
            except Exception as e:
                logging.error(e)
                print(f"Exception when __wait_for_element__ : {e}")

            # sleep(1 - (time() - initTime))
            self.__random_sleep__(3,5)
        return result

    def __type_slow__(self,ele,input_text=''):
        """Type the given input text"""
        try:
            element = self.d.xpath(ele)
            for s in input_text:
                element.send_keys(s)
                sleep(uniform(0.22, 0.88))

        except Exception as e:
            logging.error(e)
            print(f'Exception when __typeSlow__ : {e}')





    def login(self,ID,PW):
        '''인스타그램 로그인'''

        self.ID , self.PW  = ID,PW

        ## 앱 열기 
        app_package = 'com.instagram.android'
        self.d.app_start(app_package)
        self.d.app_wait(app_package, timeout=20.0)

        ## 로그인 표시있으면 하기 
        self.__wait_for_element__('click','xpath','//*[@resource-id="com.instagram.android:id/log_in_button"]',timeout=2)
        
        ## ID ,PW 버튼 누르기 
        self.__wait_for_element__('set_text','xpath','//*[@resource-id="com.instagram.android:id/login_username"]',text=ID)
        self.__wait_for_element__('set_text','xpath','//*[@resource-id="com.instagram.android:id/password_input_layout"]',text=PW)
        self.d(resourceId="com.instagram.android:id/button_text").click()

        return True


    def send_dm(self,username):
        '''다이렉트 메세지를 보냅니다. '''

        ## 만약 DM 버튼이있으면 눌러라 ## 
        if self.d(resourceId="com.instagram.android:id/action_bar_inbox_button").exists():
            self.d(resourceId="com.instagram.android:id/action_bar_inbox_button").click()

        sleep(1)
        ## 새로운 메세지 버튼이 있을시 눌러라 
        newmsg_btn = self.d(description="New Message")
        if newmsg_btn.exists():
            newmsg_btn.click()

        ## 아이디 검색
        self.__wait_for_element__('set_text','xpath','//*[@resource-id="com.instagram.android:id/recipients_container"]',text=username)

        ## 검색된거 확인
        self.d(resourceId="com.instagram.android:id/user_row_background").click()
        sleep(1)
        self.d(resourceId="com.instagram.android:id/action_bar_button_text").click()

        self.__type_slow__('//*[@resource-id="com.instagram.android:id/row_thread_composer_edittext"]','안녕하세요 저는 김영수입니다 .')

        


