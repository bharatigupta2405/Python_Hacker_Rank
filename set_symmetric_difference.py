# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
m=input().split( )
k=[]
for i in m:
    k.append(int(i))
s=set(k)
a=int(input())

o=input().split( )
l=[]
for i in o:
    l.append(int(i))
p=set(l)

print(len(s ^ p))