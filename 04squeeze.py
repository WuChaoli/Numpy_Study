import numpy as np
 
x = np.arange(9).reshape(1,3,3)
 
print ('数组 x：')
print (x)
print ('\n')
y = np.squeeze(x)
 
print ('数组 y：')
print (y)
print ('\n')
 
print ('数组 x 和 y 的形状：')
print (x.shape, y.shape)

# z = np.squeeze(y,axis=0)
# print(z)