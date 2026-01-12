from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.text_input_page import TextInputPage


def test_text_input_success_pom(page: Page) -> None:
    home = HomePage(page)
    home.open()
    home.go_to_text_input()

    text_input = TextInputPage(page)
    text_input.assert_opened()
    text_input.submit_by_enter("Hello")
    text_input.assert_result_contains("Hello")


def test_text_input_empty_shows_validation_pom(page: Page) -> None:
    home = HomePage(page)
    home.open()
    home.go_to_text_input()

    text_input = TextInputPage(page)
    text_input.assert_opened()
    # Убеждаемся, что поле пустое перед проверкой валидации
    text_input.input_box.clear()
    text_input.submit_empty_by_enter()
    text_input.assert_html5_invalid()
