import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    # эта строка на страницу по URL
    page.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
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