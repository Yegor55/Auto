import re
from playwright.sync_api import Page, expect

def test_qapractice_homepage(page: Page):
    # открываем сайт
    page.goto("https://www.qa-practice.com/")

    # проверяем заголовок страницы
    expect(page).to_have_title(re.compile("QA Practice"))
    expect(page.locator("h1")).to_be_visible()

    # проверка видимого текста или кнопки
    expect(page.locator("text=Not")).to_be_visible()

    # кликаем по кнопке "Text input"
    page.click("text=Text input")

    # проверяем, что произошёл переход (URL изменился)
    expect(page).to_have_url(re.compile("https://www.qa-practice.com/elements/input/simple"))

    # проверяем, что на странице есть input
    expect(page.locator("input[type='text']")).to_be_visible()

    # вводим текст в input
    page.fill("input[type='text']", "Hello")

    # проверяем, что текст в input введён и нажимаем Enter
    expect(page.locator("input[type='text']")).to_have_value("Hello")
    page.press("input[type='text']", "Enter")

    # проверяем, что на странице есть текст "Hello"
    expect(page.get_by_text("Hello")).to_be_visible()





