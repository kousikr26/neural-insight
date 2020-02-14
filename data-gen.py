import random
import numpy as np
import pickle
xtrain=np.random.randint(2,size=(100,8))
ytrain=xtrain[:,-1]

np.save('xtest',xtrain)
np.save('ytest',ytrain)
print(xtrain)
print(ytrain)