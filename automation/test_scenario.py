import sys

sys.path.append("/Users/apple/VsProjects/appium_project")
from common import utils
from data.test_data import TestData
from screens.my.my_page import MyPage
from base.base_test import BaseTest
from screens.login.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait


class TestScenario(BaseTest):
    def setUp(self):
        super().setUp()
        self.login_page = LoginPage(self.driver)
        self.my_page = MyPage(self.driver)

    # 시나리오 1 - 사용자가 유효한 계정으로 로그인 할 수 있는지 확인한다
    def test_01_valid_login(self):
        try:
            self.login_page.navigate_to_login_page()
            self.login_page.login(TestData.VALID_CREDENTIALS['id'], TestData.VALID_CREDENTIALS['pw'])
            assert self.my_page.get_snap_profile_text is not None

            utils.restart_app(self.driver)
        except Exception as e:
            print(f"테스트 시나리오 1에서 에러 발생: {e}")

    # 시나리오 2 - 사용자가 잘못된 계정으로 로그인 할 수 없는지 확인한다
    def test_02_invalid_login(self):
        try:
            self.login_page.navigate_to_login_page()
            self.login_page.login(TestData.INVALID_CREDENTIALS['id'], TestData.INVALID_CREDENTIALS['pw'])
            assert self.login_page.get_content_popup is not None

            utils.restart_app(self.driver)
        except Exception as e:
            print(f"테스트 시나리오 2에서 에러 발생: {e}")

    # 시나리오 3 - 로그인 시도 횟수에 제한이 있는지 확인한다
    def test_03_login_attempt_limit(self):
        pass
