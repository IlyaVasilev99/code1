#print('skolko proshlo minut?')
#n=(input())
#print('proshlo ' + n + ' minut ili')
#nn=int(n)
#n=nn/60
#print (n + 'minut')
#s0=(n-1)*m
#s00=n*(m-1)

#ПРОГРАММА ДЛЯ РЕШЕНИЯ ШОКОЛАДКИ
print('Условие')
print('Шоколадка имеет вид прямоугольника, разделенного на n×m')
print('долек. Шоколадку можно один раз разломить по прямой на две')
print('части. Определите, можно ли таким образом отломить от')
print('шоколадки часть, состоящую ровно из k долек. Программа')
print('получает на вход три числа: n, m, k и должна вывести YES или NO.')
n,m,k=int(input()),int(input()),int(input())

bn=k/n
bm=k/m
bm<=n
bn<=m
if k%m==0 and bm<=n:
    print('YES')
elif k%n==0 and bn<=m:
    print('YES')
else:
   print('NO')

#ПРОГРАММА ДЛЯ РЕШЕНИЯ ШАХМАТНОЙ ДОСКИ

print('Условие')
print('задана бесконечная шахматная доска')
print('введите координаты клетки и узнайте какого она цвета')
d1,s1=int(input()),int(input())

#x%2==1 черный
#x%2==0 белый
if d1%2==1 and s1%2==1:
    print('клетка черная')
    K1=1
elif d1%2==0 and s1%2==0:
    print('клетка черная')
    K1=1
else:
    print('клетка белая')
    K1=0
d2=int(input())
s2=int(input())
if d2%2==1 and s2%2==1:
    print('клетка черная')
    K2=1
elif d2%2==0 and s2%2==0:
    print('клетка черная')
    K2=1
else:
    print('клетка белая')
    K2=0
if K1==K2:
    print('YES, Клетки одного цвета')
else:
    print('NO, Клетки разных цветов')
    


