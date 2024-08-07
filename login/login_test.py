# import unittest
# from appium import webdriver
# import sys

# sys.path.append("/Users/apple/VsProjects/appium_project/base")
# sys.path.append("/Users/apple/VsProjects/appium_project/common")
# from common import utils
# from credentials import Credentials
# from login.login_page_locators import MusinsaLoginPageLocators
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from appium.options.android import UiAutomator2Options
# from selenium.common.exceptions import NoSuchElementException

# class MusinsaLoginTest(unittest.TestCase):

#     def setUp(self):
#         print("driver setUp")
#         self.driver = webdriver.Remote(appium_server_url, options=options)

# # # 마이페이지 버튼 클릭
# #         wait = WebDriverWait(self.driver, 10)
# #         mypage_button = wait.until(
# #             EC.element_to_be_clickable((MusinsaLoginPageLocators.mypage_button_id))
# #         )
# #         mypage_button.click()
    

#     def test_valid_login(self):
#         print("test_valid_login start")
#         self.navigate_to_login_page()

#         utils.wait_for_element(
#             self.driver, MusinsaLoginPageLocators.login_appbar_text_xpath
#         )

#         id_field = self.driver.find_element(
#             *MusinsaLoginPageLocators.login_id_input_xpath
#         )
#         id_field.send_keys(Credentials.ID)

#         pw_field = self.driver.find_element(
#             *MusinsaLoginPageLocators.login_password_input_xpath
#         )
#         pw_field.send_keys(Credentials.PASSWORD)

#         login_button = self.driver.find_element(
#             *MusinsaLoginPageLocators.login_button_xpath
#         )
#         login_button.click()

#         snap_profile_text = utils.wait_for_element(
#             self.driver, MusinsaLoginPageLocators.snap_profile_text_xpath
#         )
#         self.assertIsNotNone(snap_profile_text)

#     def tearDown(self):
#         print("driver end")
#         self.driver.quit()


# if __name__ == "__main__":
#     unittest.main()
