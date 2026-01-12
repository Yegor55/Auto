from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.text_input_page import TextInputPage
from pages.email_field_page import EmailFieldPage


def test_email_field_valid_email_no_errors(page: Page) -> None:
    home = HomePage(page)
    home.open()
    home.go_to_text_input()

    text_input = TextInputPage(page)
    text_input.assert_opened()
    text_input.go_to_email_field()

    email_page = EmailFieldPage(page)
    email_page.assert_opened()

    valid_email = "egor.kh@mail.ru"
    email_page.fill_and_submit_by_enter(valid_email)
    # После отправки формы значение может очиститься, проверяем только валидацию
    email_page.assert_no_validation_error()


def test_email_field_invalid_email_shows_error_message(page: Page) -> None:
    home = HomePage(page)
    home.open()
    home.go_to_text_input()

    text_input = TextInputPage(page)
    text_input.assert_opened()
    text_input.go_to_email_field()

    email_page = EmailFieldPage(page)
    email_page.assert_opened()

    invalid_email = "egor.kh@mail"  # без домена .ru/.com
    email_page.fill_and_submit_by_enter(invalid_email)
    # После отправки формы значение может очиститься, проверяем только валидацию
    email_page.assert_validation_error_message("Enter a valid email address.")
