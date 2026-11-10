# Иванов Глеб
# 09.11.2026
# 15:00
# этот код переходит по ссылке, проверяет есть нужное слово, получает начальную ссылку, 
import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    # эта строка переходит на страницу по URL
    page.goto("https://monkeytype.com/") # поменял ссылку

    # проверяет наличие слов "".
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    page.goto("https://monkeytype.com/") # поменял ссылку

    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Ожидается, что на странице будет заголовок с названием Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()

# Локаторы представляют собой способ поиска элемента(ов) на странице в любой момент времени
# эта строка содаёт локатор
get_started = page.get_by_role("link", name="Get started")

# эта строка нажимает на элемент
get_started.click()

# Assertions(утверждения)-будут ждать выполнения ожидаемого условия.
# этот код будет ждать, пока страница не получит заголовок, содержащий "Playwright":
import re
from playwright.sync_api import expect

expect(page).to_have_title(re.compile("Playwright"))
