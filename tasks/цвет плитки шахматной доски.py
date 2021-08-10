#print('skolko proshlo minut?')
#n=(input())
#print('proshlo ' + n + ' minut ili')
#nn=int(n)
#n=nn/60
#print (n + 'minut')
#s0=(n-1)*m
#s00=n*(m-1)

#ПРОГРАММА ДЛЯ РЕШЕНИЯ ШОКОЛАДКИ

#n=int(input())
#m=int(input())
#k=int(input())

#bn=k/n
#bm=k/m
#bm<=n
#bn<=m
#if k%m==0 and bm<=n:
 #   print('yes')
#elif k%n==0 and bn<=m:
 #   print('yes')
#else:
 #   print('no')

#ПРОГРАММА ДЛЯ РЕШЕНИЯ ШАХМАТНОЙ ДОСКИ
print('дана бесконечная шахматная доска')
print('укажите координаты клетки по очереди нажимая enter')
print('выведется сообщение о цвете клетки')
d1=int(input())
s1=int(input())
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
    


