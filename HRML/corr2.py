import numpy as np
p = np.matrix([[1,15],[1,12],[1,8],[1,8],[1,7],[1,7],[1,7],[1,6],[1,5],[1,3]])
h = np.matrix([10,25,17,11,13,17,20,13,9,15])
a = np.linalg.pinv(p) * h.transpose()
print(a)
