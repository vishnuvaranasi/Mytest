import numpy as np
height = np.array([1.73, 1.68, 1.71, 1.89, 1.79]) 
weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
bmi = weight /(height ** 2) 
print(bmi)
print(bmi > 23)
print(bmi[bmi > 23])
print(type(bmi))
