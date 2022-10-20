import math
x1=input(
    "What is x1")
y1=input(
    "What is y1")
x2=input(
    "What is x2")
y2=input(
    "What is y2")
x3=int(x1)
x4=int(y1)
x5=int(x2)
x6=int(y2)
print("The distance is" + ' ' +
      str((math.sqrt(((x5-x3)*(x5-x3))+((x6-x4)*(x6-x4))))))
