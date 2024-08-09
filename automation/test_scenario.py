import sys
import time

import allure
import pytest

sys.path.append("/Users/apple/VsProjects/appium_project")
sys.path.append("/Users/apple/VsProjects/appium_project/screens")
from common import utils
from data.test_data import TestData
from screens.my.my_page import MyPage
from base.base_test import BaseTest
from screens.login.login_page import LoginPage


class TestScenario(BaseTest):
    def setUp(self):
        super().setUp()
        self.login_page = LoginPage(self.driver)
        self.my_page = MyPage(self.driver)

    # 시나리오 1 - 사용자가 유효한 계정으로 로그인 할 수 있는지 확인한다
    @allure.description("사용자가 유효한 계정으로 로그인 할 수 있는지 확인한다")
    def test_02_valid_login(self):
        try:
            self.login_page.navigate_to_login_page()
            self.login_page.login(
                TestData.VALID_CREDENTIALS["id"], TestData.VALID_CREDENTIALS["pw"]
            )
            assert self.my_page.is_snap_profile_visible is not None

        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="screenshot",
                          attachment_type=allure.attachment_type.PNG)
            pytest.fail("테스트 시나리오 1 실패")
        finally:
            utils.restart_app(self.driver)

    # 시나리오 2 - 사용자가 잘못된 계정으로 로그인 할 수 없는지 확인한다
    @allure.description("사용자가 잘못된 계정으로 로그인 할 수 없는지 확인한다")
    def test_01_invalid_login(self):
        try:
            self.login_page.navigate_to_login_page()
            self.login_page.login(
                TestData.INVALID_CREDENTIALS["id"], TestData.INVALID_CREDENTIALS["pw"]
            )
            time.sleep(1)
            assert self.login_page.is_container_visible is not None

        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="screenshot",
                          attachment_type=allure.attachment_type.PNG)
            pytest.fail("테스트 시나리오 2 실패")
        finally:
            utils.restart_app(self.driver)

    # 시나리오 3 - 로그인 시도 횟수에 제한이 있는지 확인한다
    @allure.description("로그인 시도 횟수에 제한이 있는지 확인한다")
    def test_03_login_attempt_limit(self):
        max_attempts = 5  # 로그인 시도 최대횟수
        delay_between_attempts = 1  # 로그인 재시도 대기시간
        try:
            self.login_page.navigate_to_login_page()

            for attempt in range(max_attempts):
                self.login_page.login(
                    TestData.INVALID_CREDENTIALS["id"],
                    TestData.INVALID_CREDENTIALS["pw"],
                )

                if attempt < max_attempts:
                    self.login_page.close_login_popup()
                    print(f"{attempt + 1}번째 시도")
                time.sleep(delay_between_attempts)

            time.sleep(delay_between_attempts)
            assert self.login_page.is_recaptcha_visible() is not None

        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="screenshot",
                          attachment_type=allure.attachment_type.PNG)
            pytest.fail("테스트 시나리오 3 실패")
        finally:
            utils.restart_app(self.driver)
