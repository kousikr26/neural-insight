import random
import numpy as np
import pickle

train_size = 200000
test_size = 10000


def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        # print('\t', f)print()c
        if n % f == 0:
            return False
        if n % (f+2) == 0:
            return False
        f += 6
    return True

file1=open("primes1.txt","r")

file2 = open("primes2.txt", "r")
lis=file1.read().split()+file2.read().split()

lis=list(map(int,lis))
xtrain=[]
ytrain=[]
xtest=[]
ytest=[]
for i in range(1,train_size+1):
    xtrain.append([i])
    ytrain.append(lis[i-1])
for i in range(train_size+1,train_size+1+test_size):
    xtest.append([i])
    ytest.append(lis[i-1])

xtrain = np.array(xtrain)
ytrain = np.array(ytrain)
xtest = np.array(xtest)
ytest = np.array(ytest)
np.save('xtrain2', xtrain)
np.save('ytrain2', ytrain)
np.save('xtest2', xtest)
np.save('ytest2', ytest)
print(xtrain[:10])
print(ytrain[:10])
print(xtest[:10])
print(ytest[:10])
print(lis[199995:200003])