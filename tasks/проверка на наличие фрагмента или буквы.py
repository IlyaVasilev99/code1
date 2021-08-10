print('введите строку(любой набор символов)')
s=input()
print('введите нужный фрагмент (букву)')
print('выведется индекс расположения первого и последнего символа)')
T=input()
q=s.find(T)
w=s.rfind(T)
if q>=0 and w==q:
    print(q)
elif q>=0 and w!=q:
    print(q)
    print(w)
else:
    print('фрагмент(буква) "' + T + '" не обнаружена')

