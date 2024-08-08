from appium.webdriver.common.appiumby import AppiumBy


class Locators:
    # XPath
    login_id_input_xpath = (AppiumBy.XPATH, '//android.webkit.WebView[@text="로그인 | 무신사 '
                                            '스토어"]/android.view.View/android.view.View[2]/android.view.View['
                                            '1]/android.widget.EditText[1]')
    login_password_input_xpath = (AppiumBy.XPATH, '//android.webkit.WebView[@text="로그인 | 무신사 '
                                                  '스토어"]/android.view.View/android.view.View[2]/android.view.View['
                                                  '1]/android.widget.EditText[2]')
    login_button_xpath = (AppiumBy.XPATH, '//android.widget.Button[@text="로그인"]')
    login_signup_text_xpath = (AppiumBy.XPATH, '//android.widget.TextView[@text="로그인/회원가입하기"]')
    login_appbar_text_xpath = (AppiumBy.XPATH, '//android.widget.TextView[@text="로그인"]')
    snap_profile_text_xpath = (AppiumBy.XPATH, '//android.widget.TextView[@text="스냅 프로필"]')

    # ID
    stop_watching_button_id = (AppiumBy.ID, 'com.musinsa.store:id/text_view_stop_watching_today')
    popup_content_container_id = (AppiumBy.ID, 'android:id/content')
    popup_confirm_button_id = (AppiumBy.ID, 'android:id/button1')
    login_rc_container_id = (AppiumBy.ID, 'rc-anchor-container')

    # accessibility ID
    mypage_button_id = (AppiumBy.ACCESSIBILITY_ID, '마이')
