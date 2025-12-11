import re

from playwright.sync_api import Page,expect

def test_verifyPageUrl(page: Page):
    page.goto("https://www.flipkart.com/")

    flipkarturl = page.url
    print("Url of the application: ", flipkarturl)

    expect(page).to_have_url("https://www.flipkart.com/")

def test_verifyTitle(page: Page):
    page.goto("https://www.flipkart.com/")

    flipkartTitle=page.title()
    print("Title of the page:",flipkartTitle)
    expect(page).to_have_title(re.compile("Flipkart"))
