import time
from selenium.webdriver.common.by import By
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"



def test_find_button_add_card(browser):
    browser.get(link)
    assert browser.find_elements(By.CSS_SELECTOR, '.product_main > button'), "Кнопка не найдена"
    time.sleep(30)

"""
Запускаем тест
    pytest --language=es test_items.py
"""

