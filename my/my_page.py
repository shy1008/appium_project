from base.base_page import BasePage
from login.login_page_locators import MusinsaLoginPageLocators  

class MyPage(BasePage):
    def get_snap_profile_text(self):
        return self.find_element(MusinsaLoginPageLocators.snap_profile_text_xpath)  
