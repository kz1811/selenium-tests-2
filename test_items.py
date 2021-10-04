from selenium.webdriver.common.by import By
from selenium import webdriver
import time

def test_button_add_to_basket_is_here(browser):
    link =  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    assert browser.find_elements(By.CLASS_NAME, "btn-ad-to-basket"), "Should be 'Add to basket' button"
