import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    appPackage='com.android.settings',
    appActivity='.Settings',
)

appium_server_url = 'http://localhost:4723'

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        print("setUp")
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

    def tearDown(self) -> None:
        print("tearDown")

        if self.driver:
            print("tearDown self.driver")
            self.driver.quit()

    def test_find_battery(self) -> None:
        print("test_find_battery")

        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="배터리"]')
        el.click()

if __name__ == '__main__':
    unittest.main()