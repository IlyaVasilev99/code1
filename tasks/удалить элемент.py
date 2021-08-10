p='7 6 5 4 3 2 1'
a = [int(s) for s in p.split()]
print(a)

#удаление элемента с помощью list.pop(i)

print('vvedite порядковый номер числа, который хотите удалить')
k1=int(input())
print(a.pop(k1-1))
print(a)

#удаление элемента с помощью list.remove(x)

print('vvedite порядковый номер числа, который хотите удалить еще раз')
k2=int(input())
a.remove(a[k2])
print(a)

