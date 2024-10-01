# 1. Создай гистограмму для случайных данных, сгенерированных с помощью
# функции `numpy.random.normal`.
# Параметры нормального распределения
# mean = 0       # Среднее значение
# std_dev = 1    # Стандартное отклонение
# num_samples = 1000  # Количество образцов
#
# # Генерация случайных чисел, распределенных по нормальному распределению
# data = np.random.normal(mean, std_dev, num_samples)

import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(0, 1, 1000)

plt.hist(x, 50)
plt.xlabel('Нормально распределенные случайные числа')
plt.ylabel('Частота')
plt.title('Гистограмма нормального распределения')

plt.show()