from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')  # Добавляем аргумент для headless режима
options.add_argument('--disable-gpu')  # Отключаем GPU для headless режима
options.add_argument('--no-sandbox')  # Безопасный режим (используется в некоторых системах)


# Создайте экземпляр драйвера
driver = webdriver.Chrome()

base_url = "https://www.cian.ru/cat.php?deal_type=rent&engine_version=2&offer_type=flat"
additional_params = "&region=1&room1=1&room2=1&type=4"

# Открываем файл для записи
with open('prices_5pages.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Записываем заголовок
    writer.writerow(['Price'])

    try:
        for p in range(1, 6):
            # Формируем URL для каждой страницы
            full_url = f"{base_url}&p={p}{additional_params}"
            driver.get(full_url)

            # Подождем немного, чтобы страница полностью загрузилась
            time.sleep(5)

            # Находим элементы с ценами
            prices = driver.find_elements(By.XPATH, "//span[@data-mark='MainPrice']/span")

            # Записываем цены в файл
            for price in prices:
                writer.writerow([price.text])

    finally:
        # Закрываем драйвер
        driver.quit()