# from ppadb.client import Client as AdbClient 
# from adb_shell.adb_device import AdbDeviceTcp, AdbDeviceUsb
# from adb_shell.auth.sign_pythonrsa import PythonRSASigner
# #https://pypi.org/project/pure-python-adb/
# #https://pypi.org/project/instappium/

# client = AdbClient(host="127.0.0.1", port=5037)
# devices = client.devices()
# # device = devices[0]
# device = client.device("emulator-5554")
# # print(devices)
# # print(client.version())
# device.shell("echo hello world !")
import uiautomator2 as u2 #https://github.com/openatx/uiautomator2
import time #https://velog.io/@chacha/UIAutomator2-스크립트-작성해보기
 
# # 연결 테스트
d = u2.connect() 
# print(device.info)

ID = 'abigailsmithley'
PW = 'abigailsmithley3'
## 앱 시작 
app_package = 'com.instagram.android'
d.app_start(app_package)

## 기다리기 
d.app_wait(app_package, timeout=20.0)

## 로그인 이있으면 로그인 하고 없으면 안함 
d.xpath('//*[@resource-id="com.instagram.android:id/log_in_button"]').click()

time.sleep(3)

# #1
# ## Username,email or phone 아이디 입력
# device.xpath('//*[@resource-id="com.instagram.android:id/inline_error"]').set_text(ID)

# ## NEXT 선택
# device.xpath('//*[@resource-id="com.instagram.android:id/button_text"]"]').click()
# time.sleep(10)

d.xpath('//*[@resource-id="com.instagram.android:id/login_username"]').set_text(ID)
time.sleep(1)
d.xpath('//*[@resource-id="com.instagram.android:id/password_input_layout"]').set_text(PW)
d(resourceId="com.instagram.android:id/button_text").click()

time.sleep(3)




# # apk_path = 'HangulKeyboard.apk'

# # device.install(apk_path)
#     # device.install(apk_path)
# # print(device.is_installed("HangulKeyboard.package"))
# #         self,

# import instappium 
# client = instappium.AppiumWebDriver(devicename='zerowater_play',devicetimeout=30,client_host="127.0.0.1",client_port=5037)
# # # from instappium.engine import FSMSession
# # session = instappium.InstAppium(username='deborahr.robinson43', password='YHHKFUl4YtLH', device='zerowater_play', show_logs=True)
# # session._webdriver.go_search('whoever you want', 'accounts')

# # # doing one action using the FSM

# # fsm = FSMSession(session._webdriver)

# # # # should respond idle
# # # fsm.state

# # # let's go to the home page
# # fsm.go_homepage()