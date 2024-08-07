from typing import Tuple

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging

logger = logging.getLogger(__name__)

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    def find_element(
        self, locator: Tuple[str, str]
    ):
        """
        특정 요소를 찾습니다. 요소가 없으면 None을 반환하거나 예외를 발생시킵니다.
        """
        try:
            wait = WebDriverWait(self.driver, self.timeout)
            element = wait.until(EC.presence_of_element_located(locator))
            logger.info(f"요소 찾음: {locator}, text={element.text}")
            return element
        except TimeoutException:
            logger.warning(
                f"Timeout: {self.timeout}초 내에 요소를 찾지 못했습니다: {locator}"
            )
            return None
        except Exception as e:
            logger.error(f"예외 발생: {e}")
            raise

    def click(self, locator: Tuple[str, str], raise_exception=True):
        """
        특정 요소를 클릭합니다.
        """
        try:
            element = self.find_element(locator)
            if element:  
                element.click()
                logger.info(f"요소 클릭: {locator}")
            else:
                if raise_exception:
                    raise TimeoutException(f"Timeout: {self.timeout}초 내에 요소를 찾거나 클릭할 수 없습니다: {locator}")
                else:
                    logger.warning(f"클릭할 요소를 찾지 못했습니다: {locator}") 
        except Exception as e:
            logger.error(f"예외 발생: {e}")
            raise

    def send_keys(self, locator: Tuple[str, str], text: str):
        """
        특정 요소에 텍스트를 입력합니다.
        """
        try:
            element = self.find_element(locator)
            if element:  
                element.send_keys(text)
                logger.info(f"텍스트 입력: {locator}, '{text}'")
            else:
                logger.warning(f"텍스트 입력 요소를 찾지 못했습니다: {locator}") 
        except Exception as e:
            logger.error(f"예외 발생: {e}")
            raise
