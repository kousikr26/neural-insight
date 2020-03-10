import random
import numpy as np
import pickle
xtrain=np.random.randint(2,size=(9000,64))
ytrain=xtrain[:,-1]
y=[]
for i in range(9000):
	if(ytrain[i]==1):
		y.append(0)
	else:
		y.append(1)
ytrain=np.array(y)
np.save('xtrain',xtrain)
np.save('ytrain',ytrain)
print(xtrain)
print(ytrain)