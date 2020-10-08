# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
l=[]
m=[]
total=0
mona=0
stri=input()
string=stri.split()
for i in string:
    l.append(int(i))
char=input()
strin=char.split()
for i in strin:
    m.append(int(i))

for i in range(n):
    total+=l[i]*m[i]
    mona+=m[i]
print(f'{total/mona:.1f}')
