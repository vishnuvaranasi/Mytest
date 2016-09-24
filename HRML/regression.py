import numpy as np

# read feature vector size and training set size
string = raw_input()
tmp = string.split()
F = int(tmp[0])
N = int(tmp[1])

# read training data
M = np.zeros((N,F+2))
for i in range(N):
   string = raw_input()
   tmp = string.split()
   M[i,0] = 1
   for j in range(F+1):
      M[i,j+1] = float(tmp[j])

# how many test rows are present
string = raw_input()
T = int(string)

# read test data 
Mt = np.zeros((T,F+1))
for i in range(T):
   string = raw_input()
   tmp = string.split()
   Mt[i,0] = 1
   for j in range(F):
      Mt[i,j+1] = float(tmp[j])

#print('Completed reading')

# type cast into matrix
M = np.matrix(M)
Mt = np.matrix(Mt)

# solution
a = np.linalg.pinv(M[:,:F+1]) * M[:,F+1]

# test results
results = Mt * a
[tmp1,tmp2] = results.shape
for i in range(tmp1):
   print(round(results[i,0],2)) 
