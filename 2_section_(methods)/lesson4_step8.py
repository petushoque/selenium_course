from selenium import webdriver

link = "http://suninjuly.github.io/explicit_wait2.html"

browser = webdriver.Chrome()
# говорим WebDriver искать каждый элемент в течение 5 секунд
browser.implicitly_wait(5)

try:
  browser.get(link)

  button = browser.find_element_by_id("verify")
  button.click()
  message = browser.find_element_by_id("verify_message")

  assert "successful" in message.text
    
finally:
    # Закрыть браузер
    browser.quit()

# Пустая строка в конце
