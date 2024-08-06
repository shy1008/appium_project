import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

# 로거 설정 (파일 저장)
logging.basicConfig(filename='test_log.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 각 디바이스에 대한 설정 정보를 담은 리스트
devices_config = [
    {
        'device_name': 'Pixel4_api33',
        'udid': 'emulator-5554',
    },
    {
        'device_name': 'Pixel7a_api34',
        'udid': 'emulator-5556',
    },
    # 필요한 만큼 추가
]

appium_server_url = 'http://localhost:4723'

@pytest.fixture(params=devices_config) 
def driver(request):
    capabilities = dict(
        platformName='Android',
        automationName='uiautomator2',
        deviceName=request.param['device_name'],
        udid=request.param['udid'],
        appPackage='com.android.settings',
        appActivity='.Settings',
    )
    driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
    
    yield driver  # 테스트 함수에 driver 객체 전달
    driver.quit()

def test_find_battery(driver):
    print("test_find_battery")

    # "Battery" 요소 찾기 및 클릭
    battery_element = driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Battery"]')
    battery_element.click()

    wait = WebDriverWait(driver, 10)  # 최대 10초 동안 대기
    
    # 배터리 상태 정보 찾기
    battery_status_element = wait.until(
        EC.presence_of_element_located((AppiumBy.ID, 'com.android.settings:id/usage_summary')) 
    )
    
    battery_status = battery_status_element.text

    # 디바이스 이름과 배터리 상태 출력
    print(f"Device: {driver.capabilities['deviceName']}, Battery Status: {battery_status}")
