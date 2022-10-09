__author__ = 'miserylab'

import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import have
from selene.support.shared import browser
from allure import step

from utils import attach


# @allure.title('Wikipedia search QA')
def test_wikipedia(setup_browser):

    with step('Search for content'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()

        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type("QA")

    with step('Content should be found'):
        browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).should(have.size_greater_than(0))
    attach.add_video(browser)