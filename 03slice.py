import numpy as np
 
x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]])  
print ('我们的数组是：' )
print (x)
print ('\n')


rows = [1,2]
cols= [[0,0],[2,2]]
y = x[rows,cols]
print(y)
