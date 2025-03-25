import numpy as np

a = 3
sigma = 1
volume = 22
l  = 3.9
np.random.seed(85) #задание random seed
sample = np.random.exponential(1/l, volume)
print(sample) #вывод выборки на печать
print(sum(sample)/len(sample)) #вывод выборочного среднего