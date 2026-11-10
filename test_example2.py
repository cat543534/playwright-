# Иванов Глеб
# 10.11.2026
# 15:00
# Вы можете использовать различные фикстуры(fixtures) для выполнения кода до или после тестов, а также для обмена объектами между ними.
# этот код запускает ссылку и после проверяет URL сайта
import pytest
from playwright.sync_api import Page, expect

@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    
    print("before the test runs")

    # Go to the starting url before each test.
    page.goto("https://github.com/login") # поменял ссылку
    yield
    
    print("after the test runs")

def test_main_navigation(page: Page):
    # Assertions use the expect API.
    expect(page).to_have_url("https://github.com/login")