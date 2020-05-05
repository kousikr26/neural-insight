import random
import numpy as np
import pickle

train_size = 2000*2
test_size = 500*2


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
lis2=[]
i=0
while (i<(train_size//2+test_size//2+100)):
    
    num = random.randint(3, 2**15-10)
    if(not is_prime(num)):
        lis2.append(num)
        i+=1
    else:
       # print(i)
       pass


print(len(lis),len(lis2))

primes = []
non_primes = []
for i in range(train_size//2):
    print(lis[i])
    primes.append(list(map(int, list(format(lis[i], "015b")))))
for i in range(train_size//2):
    non_primes.append(list(map(int, list(format(lis2[i], "015b")))))
temp = list(zip(primes+non_primes, [1]*len(primes)+[0]*len(non_primes)))

xtrain, ytrain = zip(*temp)
ytrain_new = []
for i in range(len(ytrain)):
    if(ytrain[i] == 1):
        ytrain_new.append([0, 1])
    else:
        ytrain_new.append([1, 0])
ytrain = ytrain_new

xtrain = np.array(xtrain)
ytrain = np.array(ytrain)
np.save('xtrain', xtrain)
np.save('ytrain', ytrain)
print(xtrain[:10])
print(ytrain[:10])
primes = []
non_primes = []
for i in range(train_size//2, train_size//2+test_size//2):
    primes.append(list(map(int, list(format(lis[i], "015b")))))
for i in range(train_size//2, train_size//2+test_size//2):
    non_primes.append(list(map(int, list(format(lis2[i], "015b")))))

#print(primes)
temp = list(zip(primes+non_primes, [1]*len(primes)+[0]*len(non_primes)))
random.shuffle(temp)
xtrain, ytrain = zip(*temp)
ytrain_new = []
for i in range(len(ytrain)):
    if(ytrain[i] == 1):
        ytrain_new.append([0, 1])
    else:
        ytrain_new.append([1, 0])
ytrain = ytrain_new

xtrain = np.array(xtrain)
ytrain = np.array(ytrain)
np.save('xtest', xtrain)
np.save('ytest', ytrain)
print(xtrain[:10])
print(ytrain[:10])
