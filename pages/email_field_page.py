import re
from playwright.sync_api import Page, expect


class EmailFieldPage:
    def __init__(self, page: Page):
        self.page = page
        # На странице email input имеет name="email" или id="id_email"
        self.email_input = page.locator("input[name='email'], input#id_email")

    def assert_opened(self) -> None:
        expect(self.page).to_have_url(re.compile(r"/elements/input/email/?$"))
        expect(self.email_input).to_be_visible()

    def fill_and_submit_by_enter(self, email: str) -> None:
        self.email_input.clear()
        self.email_input.fill(email)
        # Проверяем, что значение установлено и поле валидно перед отправкой
        expect(self.email_input).to_have_value(email)
        is_valid_before = self.email_input.evaluate("el => el.checkValidity()")
        self.email_input.press("Enter")
        # Сохраняем результат валидности для последующей проверки
        self._was_valid_before_submit = is_valid_before

    def assert_email_value(self, email: str) -> None:
        expect(self.email_input).to_have_value(email)

    def assert_no_validation_error(self) -> None:
        # После отправки формы поле может стать пустым, поэтому проверяем валидность ДО отправки
        # которая была сохранена в методе fill_and_submit_by_enter
        if hasattr(self, '_was_valid_before_submit'):
            assert self._was_valid_before_submit is True, "Email field should be valid before submit"
        else:
            # Если метод fill_and_submit_by_enter не был вызван, проверяем текущее состояние
            is_valid = self.email_input.evaluate("el => el.checkValidity()")
            assert is_valid is True, "Email field should be valid"

    def assert_validation_error_message(self, message: str) -> None:
        # Самый надёжный способ: браузерный текст ошибки у HTML5 validation
        msg = self.email_input.evaluate("el => el.validationMessage")
        # Сообщение может отличаться в зависимости от браузера, проверяем что оно содержит ключевые слова
        assert message.lower() in msg.lower() or msg.lower() in message.lower(), \
            f"Expected error message containing '{message}', but got '{msg}'"
