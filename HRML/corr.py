import numpy as np
physics = [15,12,8,8,7,7,7,6,5,3]
history = [10,25,17,11,13,17,20,13,9,15]
print(np.corrcoef(physics, history)[0,1])
