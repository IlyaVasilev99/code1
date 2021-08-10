p='7 6 5 4 3 2 1'
a = [int(s) for s in p.split()]
print(a)
print('vvedite индекс')
k=int(input())
print('vvedite число')
c=int(input())
a.insert(k,c)
print(a)
