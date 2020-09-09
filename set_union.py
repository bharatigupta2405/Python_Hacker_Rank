# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
s=input().split(" ")
l=[]
for i in s:
    l.append(int(i))
n=int(input())
t=input().split(" ")
m=[]
for i in t:
    m.append(int(i))
u=set(l)
v=set(m)
print(len(u.union(v)))