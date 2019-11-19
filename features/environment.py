from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from features.hw7_application import Application

def browser_init(context):
    """
    :param context: Behave context
    """
    context.driver = webdriver.Chrome(executable_path = "C:\Webdrivers\chromedriver")
    #context.driver = webdriver.Firefox(executable_path = "C:\Webdrivers\geckodriver")
    # context.driver = webdriver.Edge(executable_path = "C:\Webdrivers\MicrosoftWebDriver")
    # context.browser = webdriver.Safari()


    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 15)

    context.app = Application(context.driver)

def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name, '.')
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step, '.')


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step, '.')


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
    print('\nTest done: ', feature, '!')