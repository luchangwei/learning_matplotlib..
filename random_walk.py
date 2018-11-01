import matplotlib.pyplot as plt
from random import choice
import time

'''
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

'''
class RandomWalk():
    def __init__(self,number_points=5000):
        self.number_points = number_points
        self.y_values = [0]
        self.x_values = [0]
    def fill_walk(self):
        while len(self.x_values) < self.number_points:
            x_direction = choice([-1,1])
            x_distance = choice([0,1,2,3,4])
            x_step = x_direction * x_distance

            y_direction = choice([-1, 1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            if x_step == 0 and y_step == 0:
                continue

            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
            