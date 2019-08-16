# encoding=utf-8
from selenium import webdriver
import time

def test_title(driver):
    try:
        time.sleep(5)
        success = u'Проект' in driver.title
    except:
        success = False
    return success


def test_button_main(driver):
    try:
        time.sleep(5)
        elem = driver.find_element_by_id('main_page')
        success = elem.text == u'Головна'
    except:
        success = False
    return success


def test_click_all_databases(driver):
    try:
        time.sleep(5)
        driver.find_element_by_link_text(u'Всі бази даних').click()
        time.sleep(5)
        success = driver.current_url == u'http://localhost:8080/site/all-databases'
    except:
        success = False
    return success


def run_tests():

    driver = webdriver.Chrome('/Users/vitaliyvrublevskiy/projects/Verificcation/Web/chromedriver_mac')
    driver.get("http://localhost:8080/")

    if test_title(driver):
        print 'Test passed'
    else:
        print 'Test failed'

    if test_button_main(driver):
        print 'Test passed'
    else:
        print 'Test failed'

    if test_click_all_databases(driver):
        print 'Test passed'
    else:
        print 'Test failed'

    driver.close()

run_tests()