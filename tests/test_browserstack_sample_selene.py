__author__ = 'miserylab'

import allure
from allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import have
from selene.support.shared import browser
from utils.attach import add_video


@allure.title('Wikipedia search BrowserStack')
def test_search_browserstack(setup_browser):
    with step('Search for content'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()

        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type("BrowserStack")

    with step('Content should be found'):
        browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).should(have.size_greater_than(0))

