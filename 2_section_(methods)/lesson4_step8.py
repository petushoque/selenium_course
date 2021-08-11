from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

link = "http://suninjuly.github.io/explicit_wait2.html"

browser = webdriver.Chrome()
# говорим WebDriver искать каждый элемент в течение 5 секунд
browser.implicitly_wait(5)

try:
  # Открыть страницу по ссылке
  browser.get(link)

  price = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "100"))

  book_button = browser.find_element_by_id("book")
  book_button.click()

    
finally:
    # Закрыть браузер
    browser.quit()

# Пустая строка в конце
