import logging
from selenium.common.exceptions import TimeoutException  
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def wait_for_element(driver, locator, timeout=10):
    """
    특정 요소가 나타날 때까지 기다립니다.

    Args:
        driver: Appium WebDriver 객체
        locator: 요소를 찾기 위한 Locator (튜플 형태: (AppiumBy.XPATH, 'xpath') 또는 (AppiumBy.ID, 'id'))
        timeout: 최대 대기 시간 (초)

    Returns:
        WebElement: 찾은 요소

    Raises:
        TimeoutException: timeout 시간 내에 요소를 찾지 못한 경우
        Exception: 기타 예외 발생 시
    """
    try:
        wait = WebDriverWait(driver, timeout)
        element = wait.until(
            EC.presence_of_element_located(locator)
        )
        logger.info(f"요소 찾음: {locator}")
        return element
    except TimeoutException:
        logger.error(f"Timeout: {timeout}초 내에 요소를 찾지 못했습니다: {locator}")
        raise  
    except Exception as e:
        logger.error(f"예외 발생: {e}")
        raise 