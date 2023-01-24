#import numpy as np
#datafromfile=np.loadtxt("D:\\School Project\\Python\\Files for tests\\1.txt",dtype="str")



with open('D:\\School Project\\Python\\Files for tests\\1.txt', 'r') as f:
    myNames = [line.strip() for line in f]

#print(myNames)
#print(type(myNames))

for i in range(len(myNames)):
    print(myNames[i])

