n=int(input())
k=[]
for i in range(n):
    alphabets = [int(v) if v.isnumeric() else v for v in input().split()]
    k.append(alphabets)
m=int(input())
p=[]
for i in range(n):
    alphabets = [int(v) if v.isnumeric() else v for v in input().split()]
    p.append(alphabets)
cost=0
for i in range(n):
    for j in range(m):
        if p[j][0]==k[i][0]:
            if p[j][2]<k[i][2]:
                cost+=(p[j][1]*p[j][2])+((k[i][1]-p[j][1])*k[i][2])
            else:
                cost+=k[i][1]*k[i][2]
print(cost) 