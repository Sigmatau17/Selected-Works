import pandas as pd
from pandas import Series, DataFrame
import matplotlib as plt
auto = pd.read_csv('auto-mpg-quiz (1).csv', delimiter=',', decimal='.', index_col = 'name')
auto.drop(columns=['mpg', 'displ', 'yr', 'origin'])
print(auto.drop(columns=['mpg', 'displ', 'yr', 'origin']))
cars = auto[(auto.cyl == 4) & (auto.hp > 80) | (auto.cyl == 8) & (auto.hp > 90)]
print(cars.weight.mean())