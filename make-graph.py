#定義#####################################################################################################################################################################
import math
import numpy as np
import matplotlib.pyplot as plt
import linecache
import re
import subprocess
import time
import os
import sys
from subprocess import PIPE


fig = plt.figure()

# Axesを追加
ax = fig.add_subplot(111)

x=[0,2,2,100]
y =[0,0,1,1]
# 線の太さを指定してデータをプロット
ax.plot(x, y, linewidth = 4)
plt.xlim(0,3)
plt.ylim(0,2)
#plt.plot(x,y)
# 線の太さを指定してデータをプロット
#ax.plot(x, y, linewidth = 4)
plt.xlabel('H / J',{'fontsize':15}) 
plt.ylabel('Sztot',{'fontsize':15}) 
plt.show()


fig = plt.figure()
#x = H/J 
x = np.linspace(0, 3, 500)
y=x
y_1 = (1/2 - x)
y_2 = 1/2 + x
y_3 = 1/2 + x*0
y_4 = -3/2 + x*0

plt.plot(x,y_1,label="Sztot  = 1")
plt.plot(x,y_2,label = 'Sztot  = 0')
plt.plot(x,y_3,label = 'Sztot  = 0')
plt.plot(x,y_4,label = 'Sztot  = -1')

#plt.xlim(0,2)

plt.xlabel('H / J',{'fontsize':15}) 
plt.ylabel('E',{'fontsize':15}) 
#plt.show()
