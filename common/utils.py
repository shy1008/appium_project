from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

app_package = "com.musinsa.store"


def restart_app(driver):
    """
    앱을 종료하고 다시 시작합니다.
    """
    driver.terminate_app(app_package)
    driver.activate_app(app_package)
