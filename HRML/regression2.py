import numpy as np

# read feature vector size and training set size
string = raw_input()
tmp = string.split()
F = int(tmp[0])
N = int(tmp[1])
P = 3;

# read training data
M = np.zeros((N,F+2))
for i in range(N):
   string = raw_input()
   tmp = string.split()
   M[i,0] = 1
   for j in range(F+1):
      M[i,j+1] = float(tmp[j])

# append the polynomial features
Ma = np.zeros((N,P*F+2))
# first column and last column as it is
Ma[:,0] = M[:,0]
Ma[:,P*F+1] = M[:,F+1]
for i in range(1,F+1):
   for j in range(1,P+1):
      Ma[:,(i-1)*P+j] = M[:,i] ** j;   

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

# append polynomial features
Mta = np.zeros((T,P*F+1))
# first column as it is
Mta[:,0] = Mt[:,0]
for i in range(1,F+1):
   for j in range(1,P+1):
      Mta[:,(i-1)*P+j] = Mt[:,i] ** j;

#print('Completed reading')

# type cast into matrix
Ma = np.matrix(Ma)
Mta = np.matrix(Mta)

# solution
a = np.linalg.pinv(Ma[:,:P*F+1]) * Ma[:,P*F+1]

# test results
results = Mta * a
[tmp1,tmp2] = results.shape
for i in range(tmp1):
   print(round(results[i,0],2)) 
