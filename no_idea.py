# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m=map(int,input().split())

s=input().split(" ")
k=[]
count=0
for i in s:
    k.append(int(i))
a=set()
z=input().split()
for i in z:
    a.add(int(i))
b=set()
x=input().split()
for i in x:
    b.add(int(i))
for i in range(n):
    if k[i] in a:
        count+=1
    if k[i] in b:
        count-=1
print(count)
