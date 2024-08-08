import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
import logging

appium_server_url = "http://localhost:4723"
logger = logging.getLogger(__name__)


class BaseTest(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        """ Appium 서버와 연결하고 드라이버를 초기화합니다."""
        options = UiAutomator2Options()
        options.platform_name = "Android"
        options.automation_name = "uiautomator2"
        options.app_package = "com.musinsa.store"
        options.app_activity = ".scenes.deeplink.DeepLinkActivity"
        options.auto_grant_permissions = True
        options.app_wait_activity = ".scenes.main.main.MainActivity"
        options.device_name = "QA_Emulator_Name"
        options.no_reset = True

        cls.driver = webdriver.Remote(appium_server_url, options=options)
        logger.info(f"driver setUp")

    @classmethod
    def tearDownClass(cls):
        """ 테스트 종료 후 Appium 세션을 종료하고 드라이버를 정리합니다."""
        if cls.driver:
            logger.info(f"driver tearDown")
            cls.driver.quit()
