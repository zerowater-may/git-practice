from api import Insta_App



class send_DM:

    def __init__(self):
        super().__init__()

        self.api = Insta_App()

    
    def send_direct_msg(self):
        ''' 다이렉트 메세지를 보냅니다. '''
        
        # self.api.login('abigailsmithley','abigailsmithley3')
        self.api.send_dm('zerowater_health')





if __name__ == '__main__':
    s = send_DM()
    s.send_direct_msg()