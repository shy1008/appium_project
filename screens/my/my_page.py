from base.base_page import BasePage
from common.locators import Locators


class MyPage(BasePage):
    def is_snap_profile_visible(self):
        return self.find_element(Locators.snap_profile_text_xpath)
