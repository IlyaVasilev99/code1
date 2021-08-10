def swap_colums(massive, colume_1,colume_2):
    massive.insert(colume_2,massive[colume_1])
    massive.pop(colume_1)
    massive.insert(colume_1,a[colume_2])
    massive.pop(colume_2+1)
    print('    ',massive)
    
m, n = [int(i) for i in input().split()]
i, j = [int(i) for i in input().split()]
a=[[0+i for j in range(m)] for i in range(n)]

if i<=j:
    swap_colums(a,i,j)
    #a.insert(j,a[i])
    #a.pop(i)
    #a.insert(i,a[j])
    #a.pop(j+1)
    #print('финальная',a)
else:
    swap_colums(a,j,i)
    #a.insert(i,a[j])
    #a.pop(j)
    #a.insert(j,a[i])
    #a.pop(i+1)
    #print('финальная',a)
