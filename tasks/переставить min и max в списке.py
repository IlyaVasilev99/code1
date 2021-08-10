print('введите последовательность через пробел')
a = [int(s) for s in input().split()]
print(a)
x,y=min(a),max(a)
xi=a.index(x)
yi=a.index(y)
if yi>xi:
    a[yi],a[xi]=a[xi],a[yi]
else:
    a[xi],a[yi]=a[yi],a[xi]
print(a)
