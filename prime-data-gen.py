import random
import numpy as np
import pickle
train_size=500000
test_size=2000

def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n % 2 == 0: return False
    if n < 9: return True
    if n % 3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        # print('\t', f)print()c
        if n % f == 0: return False
        if n % (f+2) == 0: return False
        f += 6
    return True



# print(is_prime(2**40-87))
prime_count=0
non_prime_count=0
primes=[]
non_primes=[]
while(prime_count<train_size/2):
    
    num=random.randint(1,2**40-1)
    if(is_prime(num)):
        primes.append(list(map(int,list(format(num, "040b")))))
        prime_count+=1
        if(prime_count % 100 == 0):
            print("primes", prime_count)

while(non_prime_count < train_size/2):
    
    num = random.randint(1, 2**40-1)

    if(not (is_prime(num))):
        non_primes.append(list(map(int, list(format(num, "040b")))))
        non_prime_count += 1
        if(non_prime_count % 100 == 0):
            print("Non prime ", non_prime_count)

print(len(primes))
print()
print()
print()
print(len(non_primes))
temp =list(zip(primes+non_primes,[1]*len(primes)+[0]*len(non_primes)))
random.shuffle(temp)
xtrain,ytrain=zip(*temp)
ytrain_new=[]
for i in range(len(ytrain)):
    if(ytrain[i]==1):
        ytrain_new.append([0,1])
    else:
        ytrain_new.append([1,0])
ytrain=ytrain_new

xtrain=np.array(xtrain)
ytrain = np.array(ytrain)
np.save('xtrain',xtrain)
np.save('ytrain',ytrain)

