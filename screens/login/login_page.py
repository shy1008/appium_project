from base.base_page import BasePage
from login.login_page_locators import MusinsaLoginPageLocators


class LoginPage(BasePage):

    def login(self, username, password):
        self.send_keys(MusinsaLoginPageLocators.login_id_input_xpath, username)
        self.send_keys(MusinsaLoginPageLocators.login_password_input_xpath, password)
        self.click(MusinsaLoginPageLocators.login_button_xpath)

    def navigate_to_login_page(self):
        # 광고 닫기
        self.click(
            MusinsaLoginPageLocators.stop_watching_button_id, raise_exception=False
        )
        # 마이페이지 버튼 클릭
        self.click(MusinsaLoginPageLocators.mypage_button_id)
        # 로그인/회원가입하기 텍스트 클릭
        self.click(MusinsaLoginPageLocators.login_singup_text_xpath)

    def is_container_visible(self):
        return self.find_element(MusinsaLoginPageLocators.popup_content_container_id)

    def close_login_popup(self):
        self.click(
            MusinsaLoginPageLocators.popup_confirm_button_id, raise_exception=False
        )

    def is_recaptcha_visible(self):
        return self.find_element(MusinsaLoginPageLocators.login_rc_container_id)
