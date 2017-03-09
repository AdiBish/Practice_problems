import random 
import projections as pr

x_red = []
x_green = []
y_red = []
y_green = []
LEDvector = []
headDirection=[]
for i in range (10):
    x_red.append(random.randrange(0,640))
    x_green.append(random.randrange(0,640))
    y_red.append(random.randrange(0,480))
    y_green.append(random.randrange(0,480))
    LEDvector.append([x_red[i]- x_green[i], y_red[i]- y_green[i]]) 
    headDirection.append(pr.proj2d(LEDvector[i]))
    
print('LEDvector ==>\n ', LEDvector)
print('head direction==>\n', headDirection)
