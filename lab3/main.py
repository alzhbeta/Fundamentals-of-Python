# ЛАБОРАТОРНАЯ РАБОТА №3
# ПРЕДСТАВЛЕНИЕ ДАННЫХ В PYTHON

import os
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # Настройка для работы на серверах без экрана

import statsmodels.api as sm
from sklearn.datasets import load_iris, load_wine

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

# Задание 1. Построение диаграммы рассеяния
# Вариант 1. Датасет iris

iris = load_iris()
x_iris = iris.data[:, 0]  # sepal length (cm)
y_iris = iris.data[:, 1]  # sepal width (cm)
classes_iris = iris.target

plt.scatter(x_iris, y_iris, c=classes_iris)
plt.xlabel('Sepal length (cm)')
plt.ylabel('Sepal width (cm)')
plt.title('Iris Scatter Plot (Variant 1)')
plt.savefig(os.path.join(CURRENT_DIR, 'iris_scatter.png'))
plt.close()

# Задание 1. Построение диаграммы рассеяния
# Вариант 3. Датасет wine

wine = load_wine()
x_wine = wine.data[:, 0]  # alcohol
y_wine = wine.data[:, 4]  # proline
classes_wine = wine.target

plt.scatter(x_wine, y_wine, c=classes_wine)
plt.xlabel('Alcohol')
plt.ylabel('Proline')
plt.title('Wine Scatter Plot (Variant 3)')
plt.savefig(os.path.join(CURRENT_DIR, 'wine_scatter.png'))
plt.close()

# Задание 2. Построение графика динамики временных рядов
# Вариант 1. Датасет co2 

co2_data = sm.datasets.co2.load().data
co2_filtered = co2_data['1958':'1980']

plt.plot(co2_filtered.index, co2_filtered['co2'])
plt.xlabel('Year')
plt.ylabel('CO2 levels')
plt.title('CO2 Dynamics: 1958-1980 (Variant 1)')
plt.savefig(os.path.join(CURRENT_DIR, 'co2_dynamics.png'))
plt.close()

# Задание 2. Построение графика динамики временных рядов
# Вариант 3. Датасет elnino

elnino_table = sm.datasets.elnino.load().data
elnino_filtered = elnino_table[(elnino_table['YEAR'] >= 1990) & (elnino_table['YEAR'] <= 2010)]

plt.plot(elnino_filtered['YEAR'], elnino_filtered['AIR'])
plt.xlabel('Year')
plt.ylabel('Temperature Anomalies')
plt.title('Elnino Dynamics: 1990-2010 (Variant 3)')
plt.savefig(os.path.join(CURRENT_DIR, 'elnino_dynamics.png'))
plt.close()
