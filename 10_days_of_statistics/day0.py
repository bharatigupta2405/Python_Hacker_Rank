# Enter your code here. Read input from STDIN. Print output to STDOUT
from scipy import stats
def mean(n,l):
    total=0
    for i in range(n):
        total+=l[i]
    return (total/n)

def median(n,l):
    
    xi=int(n/2)
    xj=int(n/2)-1
    s=sorted(l)
    median=(s[xi]+s[xj])/2
    return median


n=int(input())
l=[]
string=input().split(" ")
for i in string:
    l.append(int(i))
print("{:.1f}".format(mean(n,l)))
print("{:.1f}".format(median(n,l)))


print(int(stats.mode(l)[0]))

