import time
from selenium.webdriver.common.by import By
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"



def test_guest_should_see_login_link(browser):
    browser.get(link)
    assert browser.find_elements(By.CSS_SELECTOR, '.product_main > button'), "Кнопка не найдена"
    time.sleep(30)

"""
Запускаем тест
    pytest --language=es lesson6_step9_multi_language_dz.py
"""

