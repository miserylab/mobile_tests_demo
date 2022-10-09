__author__ = 'miserylab'

import os

import pytest
from dotenv import load_dotenv
from appium import webdriver
from selene.support.shared import browser

from utils import attach


@pytest.fixture(scope='session', autouse=True)
def env():
    load_dotenv()


@pytest.fixture(scope='function')
def setup_browser():
    options = {
        #Specify device and os_version for testing
        "platformName": "android",
        "platformVersion": "9.0",
        "deviceName": "Google Pixel 3",

        #Set URL of the application under test
        "app": "bs://c700ce60cf13ae8ed97705a55b8e022f13c5827c",

        #Set other BrowserStack capabilities
        'bstack:options': {
            "projectName": "First Python project",
            "buildName": "browserstack-build-DEMO",
            "sessionName": "BStack first_test"
        }
    }
    '''Set your access credentials'''
    userName = os.getenv('LOGIN')
    accessKey = os.getenv('KEY')
    '''Initialize the remote Webdriver using BrowserStack remote URL 
    and options defined above'''
    browser.config.driver = webdriver.Remote(
        command_executor=f"https://{userName}:{accessKey}@hub-cloud.browserstack.com/wd/hub",
        desired_capabilities=options
    )
    browser.config.timeout = 4
    yield setup_browser
    # attach.add_video(browser)
    browser.quit()
