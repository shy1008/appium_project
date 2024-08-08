from base.base_page import BasePage
from common.locators import Locators


class LoginPage(BasePage):

    def login(self, username, password):
        self.send_keys(Locators.login_id_input_xpath, username)
        self.send_keys(Locators.login_password_input_xpath, password)
        self.click(Locators.login_button_xpath)

    def navigate_to_login_page(self):
        # 광고 닫기
        self.click(
            Locators.stop_watching_button_id, raise_exception=False
        )
        # 마이페이지 버튼 클릭
        self.click(Locators.mypage_button_id)
        # 로그인/회원가입하기 텍스트 클릭
        self.click(Locators.login_signup_text_xpath)

    def is_container_visible(self):
        return self.find_element(Locators.popup_content_container_id)

    def close_login_popup(self):
        self.click(
            Locators.popup_confirm_button_id, raise_exception=False
        )

    def is_recaptcha_visible(self):
        return self.find_element(Locators.login_rc_container_id)
