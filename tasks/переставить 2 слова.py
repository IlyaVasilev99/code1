print('введите 2 слова через пробел')
s=input()
k=s.find(' ')
print(s[k+1:]+s[k]+s[:k])
