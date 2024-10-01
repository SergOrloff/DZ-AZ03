# Необходимо спарсить цены на диваны с сайта divan.ru в csv файл, обработать данные,
# найти среднюю цену и вывести ее, а также сделать гистограмму цен на диваны​

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time
import csv
import matplotlib.pyplot as plt
import numpy as np

options = Options()
options.add_argument('--headless')  # Добавляем аргумент для headless режима
options.add_argument('--disable-gpu')  # Отключаем GPU для headless режима
options.add_argument('--no-sandbox')  # Безопасный режим (используется в некоторых системах)


def get_prices_from_current_page(dr):
    prices = []
    for span in dr.find_elements(By.CSS_SELECTOR, "span.ui-LD-ZU.KIkOH"):
        prices.append(int(span.text.replace('руб.', '').replace(' ', '')))
    return prices

driver = webdriver.Firefox(options=options)  #, service=service))
base_url = "https://www.divan.ru/category/divany-i-kresla/page-"
additional_params = "?types%5B%5D=1&types%5B%5D=4&types%5B%5D=54"

with open('data.csv', 'w', newline='', encoding='utf-8') as file:
    # Будем парсить первые 10 страниц результатов поиска диванов
    for p in range(1, 11):
        full_url = f"{base_url}{p}{additional_params}"

# url = "https://www.divan.ru/category/divany-i-kresla?types%5B%5D=1&types%5B%5D=4&types%5B%5D=54"
# url = "https://www.divan.ru/category/divany-i-kresla/page-2?types%5B%5D=1&types%5B%5D=4&types%5B%5D=54"

        driver.get(full_url)
        time.sleep(5)
        parsed_data = []
        parsed_data.extend(get_prices_from_current_page(driver))
        print(f"Обработана страница {p}")
# print(parsed_data)
# print(length = {len(parsed_data)}')

# with open('data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(parsed_data)
    print(f"Итого произведен парсинг {p} страниц")

with open('data.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        parsed_data.extend(row)
parsed_data_int = [int(item) for item in parsed_data]

print(parsed_data_int)
print(f'mean = {np.mean(parsed_data_int)}')
count = len(parsed_data_int)
print(f"(по {count} диванам)")

plt.hist(parsed_data_int, 10)
plt.xlabel('Цена дивана')
plt.ylabel('Частота')
plt.title(f"Гистограмма цен (по {count} диванам)")
plt.show()

