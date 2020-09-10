# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
s=input().split(" ")
k=[]
for i in s:
    k.append(int(i))
v=set(k)
m=int(input())
t=input().split(" ")
u=[]
for i in t:
    u.append(int(i))
w=set(u)
print(len(w.intersection(v)))