#программу сделал так что яша плыл до ближайшего бортика в любом случае+
print('Яша плавал в бассейне размером N × M метров и устал. В этот')
print('момент он обнаружил, что находится на расстоянии x метров от')
print('одного из длинных бортиков и y метров от одного из коротких бортиков. ')
print('какое минимальное расстояние должен проплыть Яша,')
print('чтобы выбраться из бассейна на бортик?')
print('')
print('Программа получает на вход числа N, M, x, y.')
print('Программа должна вывести число метров, которое нужно проплыть Яше до бортика.')
print('которое нужно проплыть Яше до бортика.')
print('Введите по очереди размеры бассейна и расстояние до бортиков')
N=int(input())#y axis
M=int(input())#x axis
y=int(input())#y axis
x=int(input())#x axis
#if (N-y)>y and (M-x)>x:
 #   if y<N and x<M:
  #      if x>y:
  #          g=y
  #     else:
   #         g=x
    #    print(g)
#if (N-y)<=y and (M-x)<=x:
 #   if (N-y)<=N and (M-x)<=M:
  #      if (N-y)>(M-x):
   #         g=N-y
    #    else:
     #       g=M-x
      #  print(g)    
#else:
 #   print('неверные данные')
#
#
#
t=N-y
r=M-x
if y<N and x<M:
    if y<=t and y<=r and y<=x:
        g=y
    elif t<=y and t<=r and t<=x:
        g=t
    elif x<=y and x<=r and x<=t:
        g=x
    elif r<=y and r<=x and r<=t:
        g=r
    print(g)
else:
    print('неверные данные')

