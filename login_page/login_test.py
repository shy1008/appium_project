import unittest
from appium import webdriver
import sys

sys.path.append("/Users/apple/VsProjects/appium_project")
sys.path.append("/Users/apple/VsProjects/common")
from common import utils
from credentials import Credentials
from login_page.login_page_locators import MusinsaLoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.options.android import UiAutomator2Options
from selenium.common.exceptions import NoSuchElementException

options = UiAutomator2Options()
options.platform_name = "Android"
options.automation_name = "uiautomator2"
options.app_package = "com.musinsa.store"
options.app_activity = ".scenes.deeplink.DeepLinkActivity"
options.auto_grant_permissions = True
options.app_wait_activity = ".scenes.main.main.MainActivity"
options.device_name = "QA_Emulator_Name"
options.no_reset = True

appium_server_url = "http://localhost:4723"


class MusinsaLoginTest(unittest.TestCase):

    def setUp(self):
        print("driver setUp")
        self.driver = webdriver.Remote(appium_server_url, options=options)

    def navigate_to_login_page(self):
        # 광고 닫기
        try:
            stop_watching_button = self.driver.find_element(
                *MusinsaLoginPageLocators.stop_watching_button_id
            )

            stop_watching_button.click()
            print("오늘 그만 보기 버튼 클릭 성공")
        except NoSuchElementException:
            print("오늘 그만 보기 버튼을 찾을 수 없습니다.")

        # 마이페이지 버튼 클릭
        wait = WebDriverWait(self.driver, 10)
        mypage_button = wait.until(
            EC.element_to_be_clickable((MusinsaLoginPageLocators.mypage_button_id))
        )
        mypage_button.click()

        # 로그인/회원가입하기 텍스트 클릭
        wait = WebDriverWait(self.driver, 10)
        login_signup_text = wait.until(
            EC.element_to_be_clickable(
                (MusinsaLoginPageLocators.login_singup_text_xpath)
            )
        )
        login_signup_text.click()

    def test_valid_login(self):
        print("test_valid_login start")
        self.navigate_to_login_page()

        utils.wait_for_element(self.driver, MusinsaLoginPageLocators.login_appbar_text_xpath)

        id_field = self.driver.find_element(*MusinsaLoginPageLocators.login_id_input_xpath)
        id_field.send_keys(Credentials.ID)

        pw_field = self.driver.find_element(*MusinsaLoginPageLocators.login_password_input_xpath)
        pw_field.send_keys(Credentials.PASSWORD)

        login_button = self.driver.find_element(*MusinsaLoginPageLocators.login_button_xpath)
        login_button.click()

        snap_profile_text = utils.wait_for_element(self.driver, MusinsaLoginPageLocators.snap_profile_text_xpath)
        self.assertIsNotNone(snap_profile_text)  

    def tearDown(self):
        print("driver end")
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
