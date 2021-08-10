print('сколько кегель раставлено')
N=int(input())
a = [int(s+1) for s in range (N)]
#print(a)
print('сколько раз бросили шар')
K=int(input())
i,o,s=0,0,1

#если вписывать l и r вручную
stroka= ['I' for s in range (N)]
print('линия из кегель будет такая',stroka)

print('укажите первый и последний сбитые броском шара кегли через пробел')
for i in range(K):
    print(i+1,' шар сбил:')
    li, ri = map(int, input().split())
    if li<=ri:
        print('от кегли под номером',li,'до кегли под номером',ri)
        for o in range (li-1,ri):
            stroka.pop(o)
            stroka.insert(o,'.')
    else:
        print('ошибка! номер первой указаной кегли должен быть меньше второй')
        break
    #print('строка будет такая',stroka)
    print('результат:',''.join(stroka))
    if (''.join(stroka)).find('I')==-1:
        print('страйк! сбиты все кегли')
        break








#while o<li:
  #  stroka.append('.')
 #   o+=1
#else:
    #while o>=li and o<=ri:
     #   stroka.append('I')
    #    o+=1
   # else:
  #      stroka.append('.')
 #       o+=1  
#print(''.join(stroka))
        
#from random import randrange
#t=[randrange(1, 10) for i in range(K)]
#print(t)
