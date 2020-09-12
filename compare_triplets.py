# Complete the compareTriplets function below.
def compareTriplets(a, b):
    countl=0
    countr=0
    for i in range(3):
        if a[i]==b[i]:
            continue
        if a[i]>b[i]:
            countl+=1
        else:
            countr+=1
    return [countl,countr]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
