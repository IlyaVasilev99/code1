print('введите последовательность чисел, после чего впишите "*"')
n=str(input())
i=0
x=n[:]
print(x)
q=int(n.find('*'))
t=0
for i in range(q):
    z=int(x[i])
    t+=z
    i+=1
    s=t/q
print('_______| среднее арифметическое последовательности равно', s,'|____________')

deltas=0
from math import sqrt
for i in range(q):
    z=float(x[i])
    y=(z-s)*(z-s)
    deltas+=y
    delta=sqrt(deltas/(q-1))
    i+=1
print('_______| стандартное отклонение последовательности  равно', delta,'|____________')
