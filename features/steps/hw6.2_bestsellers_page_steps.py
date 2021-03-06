from behave import when, then
from selenium.webdriver.common.by import By
from time import sleep

#This method allows bypass "Stale element exception"
#Locators declared as an variables
BEST_SELLERS_PAGE = (By.XPATH, "//a[contains(@href, 'bestsellers')]") #(By.XPATH, "//a[@class='nav-a  ']")
TOP_LINKS = (By.XPATH, "//a[contains(@href, 'zg_bsms_tab')]") #(By.CSS_SELECTOR, "li.zg_selected") #(By.CSS_SELECTOR, '#zg_tabs a')
HEADER = (By.CSS_SELECTOR, '#zg_banner_text_wrapper')

#Given 'Open Amazon page' works with the step in another file-it finds it by default

@when('Open Best Sellers page')
def click_on_best_sellers_page(context):
    context.driver.find_element(*BEST_SELLERS_PAGE).click()

@then('User can click through top links and verify correct page opens')
def click_thru_top(context):

    top_links = context.driver.find_elements(*TOP_LINKS)

    for x in range(len(top_links)):

        link_to_click = context.driver.find_elements(*TOP_LINKS)[x]
        link_text = link_to_click.text

        link_to_click.click()
        sleep(1)

        new_text = context.driver.find_element(*HEADER).text
        assert link_text in new_text, f'Expected {link_text} to be in {new_text}'

