# **<u>Программы 'CYAN.py' и Divan.py'**

# ***<u>1) Программа 'CYAN.py':</u>*** парсинг и анализ цен на аренду квартир

Этот проект на Python предназначен для парсинга цен на аренду 1- и 2-комнатных квартир с сайта Cian.ru с использованием библиотеки Selenium, а также для анализа и визуализации собранных данных с помощью библиотек Pandas и Matplotlib.

## Требования

Перед началом работы убедитесь, что у вас установлены следующие компоненты:

- Python 3.x
- Библиотеки Python: `selenium`, `numpy`, `pandas`, `matplotlib`
- Браузер Firefox
- `geckodriver` (необходим для управления Firefox через Selenium)

### Установка необходимых библиотек

Вы можете установить все необходимые библиотеки с помощью pip:

```bash
pip install selenium numpy pandas matplotlib
```

### Установка geckodriver

- Скачайте `geckodriver` с [официального сайта](https://github.com/mozilla/geckodriver/releases) в зависимости от вашей операционной системы.
- Убедитесь, что `geckodriver` доступен в вашей системе (добавьте в PATH или укажите путь в коде).

## Описание работы

1. **Парсинг данных**: Скрипт использует Selenium для автоматизированного открытия страниц на сайте Cian.ru и извлечения цен на аренду квартир. Цены сохраняются в CSV файл `prices.csv`.

2. **Очистка данных**: Из извлеченных данных удаляются лишние символы (например, '₽/мес.'), и они преобразуются в числовой формат. Очищенные данные сохраняются в новый CSV файл `cleaned_prices.csv`.

3. **Анализ данных**: Загружаются очищенные данные с помощью Pandas, и рассчитывается средняя цена.

4. **Визуализация данных**: Построение гистограммы цен с использованием Matplotlib для визуального анализа распределения цен.

## Использование

1. **Запуск скрипта**

   Для запуска скрипта выполните следующую команду в терминале:

   ```bash
   python CYAN.py
   ```

2. **Результаты**

   - Цены сохраняются в файл `prices.csv`.
   - Очищенные данные сохраняются в файл `cleaned_prices.csv`.
   - Средняя цена и количество объектов выводятся в консоль.
   - Построенная гистограмма отображается на экране.

## Примечания

- Скрипт настроен для работы в headless режиме, что означает, что браузер будет работать в фоновом режиме без графического интерфейса.
- Убедитесь, что сайт Cian.ru доступен и не блокирует автоматизированные запросы.
- Обратите внимание на возможные изменения в структуре HTML сайта, которые могут потребовать обновления XPATH в скрипте.

## Лицензия

Этот проект предоставляется "как есть" и распространяется под свободной лицензией. Вы можете использовать и изменять его по своему усмотрению.

## Заключение

Данный скрипт позволяет автоматизировать процесс сбора и анализа данных о ценах на аренду 1- и 2-комнатных квартир, что может быть полезно для исследования рынка недвижимости.

# ***2) <u>Программа 'Divan.py':</u>*** парсинг и анализ цен на на диваны с сайта divan.ru

## Описание

Программа `Divan.py` написана на языке Python и предназначена для парсинга цен на диваны с сайта [divan.ru](https://www.divan.ru). Программа собирает данные о ценах на диваны, сохраняет их в CSV файл, вычисляет среднюю цену и отображает гистограмму распределения цен.

## Установка

Перед началом работы с программой убедитесь, что у вас установлены все необходимые библиотеки Python. Вы можете установить их с помощью `pip`:

```bash
pip install requests selenium matplotlib numpy
```

Также вам потребуется установить браузер Firefox и geckodriver для работы Selenium WebDriver.

## Использование

1. **Запуск программы**

   Скачайте файл `Divan.py` и запустите его в вашей среде Python:

   ```bash
   python Divan.py
   ```

2. **Процесс парсинга**

   Программа осуществляет парсинг первых 10 страниц категории "Диваны и кресла" на сайте divan.ru.

3. **Сохранение данных**

   Все собранные данные о ценах сохраняются в файл `data.csv` в текущей директории.

4. **Обработка данных**

   После парсинга программа обрабатывает данные, вычисляя среднюю цену диванов.

5. **Гистограмма цен**

   Программа строит и отображает гистограмму распределения цен на диваны.

## Детали реализации

- **Парсинг данных**

  Программа использует библиотеку `selenium` для автоматизации браузера Firefox и получения данных с сайта. Каждый элемент цены на странице извлекается с использованием CSS селекторов.

- **Сохранение данных в CSV**

  Цены сохраняются в файл `data.csv` с использованием библиотеки `csv`. 

- **Анализ данных**

  Данные загружаются из CSV файла, преобразуются в числовой формат и анализируются с помощью библиотеки `numpy`, чтобы вычислить среднюю цену.

- **Визуализация**

  Для визуализации данных используется библиотека `matplotlib`, которая строит гистограмму цен.

## Примечания

- Парсинг данных может занять некоторое время, поскольку программа ждет 5 секунд после загрузки каждой страницы для корректного отображения данных.
- Убедитесь, что у вас есть стабильное интернет-соединение во время работы программы.
- Будьте внимательны при использовании автоматизированных инструментов для веб-парсинга, так как они могут нарушать правила использования сайтов.

## Заключение

`Divan.py` — это простой инструмент для извлечения и анализа данных о ценах на диваны с сайта divan.ru. Этот проект может служить основой для более сложных систем сбора и анализа данных.
