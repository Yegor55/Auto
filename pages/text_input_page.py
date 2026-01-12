import re
from playwright.sync_api import Page, expect


class TextInputPage:
    def __init__(self, page: Page):
        self.page = page
        self.input_box = page.locator("input[type='text']")

    def assert_opened(self) -> None:
        expect(self.page).to_have_url(re.compile(r"/elements/input/simple/?$"))
        expect(self.input_box).to_be_visible()

    def submit_by_enter(self, text: str) -> None:
        self.input_box.fill(text)
        self.input_box.press("Enter")

    def submit_empty_by_enter(self) -> None:
        self.input_box.clear()
        self.input_box.press("Enter")

    def assert_result_contains(self, text: str) -> None:
        expect(self.page.get_by_text(text)).to_be_visible()

    def assert_html5_invalid(self) -> None:
        expect(self.page.locator("input:invalid")).to_be_visible()
        is_valid = self.input_box.evaluate("el => el.checkValidity()")
        assert is_valid is False

    def go_to_email_field(self) -> None:
        self.page.click("text=Email field")

    def go_to_email_field(self) -> None:
        self.page.click("text=Email field")