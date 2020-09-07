# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
for i in range(n):
    s=input()
    k=''
    j=''
    for m in range(len(s)):
        if m%2==0:
            k+=s[m]
        else:
            j+=s[m]
    print(k+' '+j)