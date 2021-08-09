from selenium import webdriver

link = "http://SunInJuly.github.io/execute_script.html"

try:
    # Открыть страницу    
    browser = webdriver.Chrome()
    browser.get(link)

    # Найти вводные данные для вычисления
    browser.execute_script("alert('Robots at work');")
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

#спустая строка в конце
