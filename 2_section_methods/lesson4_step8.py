from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

# Функция для вычисления значения выражения
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

browser = webdriver.Chrome()
# говорим WebDriver искать каждый элемент в течение 5 секунд
browser.implicitly_wait(5)

try:
  # Открыть страницу по ссылке
  browser.get(link)

  # Найти элемент, отображающий цену и ждать пока она не будет равна 100
  price = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

  # Нажать на кнопку
  book_button = browser.find_element_by_id("book")
  book_button.click()

  browser.execute_script("return arguments[0].scrollIntoView(true);", book_button)

  # Найти вводные данные для вычисления
  x_value = browser.find_element_by_id("input_value")

  # Вычислить результат
  result = calc(x_value.text)

  # Найти поле ввода ответа
  input_answer = browser.find_element_by_id("answer")
  input_answer.send_keys(result)

  # Найти кнопку submit и отправить решение
  submit_button = browser.find_element_by_id("solve")
  submit_button.click()

finally:
  time.sleep(10)
  # Закрыть браузер
  browser.quit()
  
# Пустая строка в конце
