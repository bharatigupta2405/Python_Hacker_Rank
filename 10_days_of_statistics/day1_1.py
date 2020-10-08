n=int(input())
s=input().split( )
l=[]
for i in s:
    l.append(int(i))

m=0
stand=0
for i in range(n):
    m+=l[i]
mean=m/n
for i in range(n):
    stand+=(l[i]-mean)**2
standard_dev=(stand/n)**(0.5)
print(f'{standard_dev:.1f}')
