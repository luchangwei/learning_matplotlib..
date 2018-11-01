import matplotlib.pyplot as plt
from random import choice
import time


y_values = [0]
x_values = [0]
pionts_value = 0
x_value = 0
y_value = 0
while pionts_value <10000:
    x_direction = choice([-1,1])
    #print (x_direction)
    x_step = choice([0,1,2,3,4])
   # print (x_step)
    x_value = x_value + (x_step * x_direction)
    #print (x_value)
    x_values.insert(1,x_value)
    #print (x_values)
    y_direction = choice([-1,1])
    y_step = choice([0,1,2,3,4])
    y_value = x_value + (y_step * y_direction)
    y_values.append(y_value)
    pionts_value += 1
  #  print(x_values)

   # print(y_values)
plt.scatter(x_values,y_values,c='red',s=5)
          #  ,c=x_value,cmap=plt.cm.Reds,s=20)
plt.show()