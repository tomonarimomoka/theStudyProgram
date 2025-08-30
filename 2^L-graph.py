#定義#####################################################################################################################################################################
import math
import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure()
#x = np.linspace(0,100,1)
x = np.linspace(0, 100, 100)
y=pow(2,x)

#plt.xlim(100)
#plt.ylim(100)
plt.plot(x,y)

plt.xlabel('L',{'fontsize':15}) 
plt.ylabel('2^L',{'fontsize':15}) 

print("2^100=",pow(2,100))
plt.show()
