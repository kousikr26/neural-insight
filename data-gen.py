import random
import numpy as np
import pickle
num_samples=25000
xtrain=np.random.randint(2,size=(num_samples,256))
ytrain=xtrain[:,-1]
y=[]
for i in range(num_samples):
	if(ytrain[i]==1):
		y.append(0)
	else:
		y.append(1)
ytrain=np.array(y)
np.save('xtrain',xtrain)
np.save('ytrain',ytrain)
print(xtrain)
print(ytrain)