from math import sqrt
def distance(x1,y1,x2,y2):
    res=0
    res=sqrt((x2-x1)**2+(y2-y1)**2)
    return res
print('введите координаты в порядке x1 y1 x2 y2 после каждой нажимая enter')
print(distance(float(input()),float(input()),float(input()),float(input())))
 
