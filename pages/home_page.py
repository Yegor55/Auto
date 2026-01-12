from playwright.sync_api import Page, expect

BASE_URL = "https://www.qa-practice.com"


class HomePage:
    def __init__(self, page: Page):
        self.page = page

    def open(self) -> None:
        self.page.goto(f"{BASE_URL}/")
        expect(self.page).to_have_url(f"{BASE_URL}/")

    def go_to_text_input(self) -> None:
        self.page.click("text=Text input")
