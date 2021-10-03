from selenium.webdriver.common.by import By
from selenium import webdriver
import time

def test_item(browser):
    link =  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    button_add_to_basket = browser.find_element(By.CLASS_NAME, "add-to-basket")
    time.sleep(10)
    assert button_add_to_basket, "Should be 'Add to basket' button"
