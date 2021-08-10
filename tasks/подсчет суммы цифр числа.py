#import math
#v=float(input())
#t=float(input())
#S0=v*t
#S1=S0%109
#if v<0:
#    S1=abs(S1)
#print(S1)

print('число должно быть меньше 1000')
import math
X=int(input())
X01=X/100
X1=math.floor(X01)
print('сотен - ')
print(X1)
X02=(X-(X1*100))/10
X2=math.floor(X02)
print('десятков - ')
print(X2)
X03=(X-(X2*10+X1*100))
X3=X03
print('единиц - ')
print(X3)
Y=X1+X2+X3
print('сумма цифр равна')
print(Y)


    
