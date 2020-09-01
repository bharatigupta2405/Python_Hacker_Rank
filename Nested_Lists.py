if __name__ == '__main__':
    marksheet=[]
    marks=[]
    for i in range(int(input())):
        name = input()
        score = float(input())
        marksheet+=[[name,score]]
        marks+=[score]
    sl=(sorted(set(marks)))[1]
    for i,j in sorted(marksheet):
        if j==sl:
            print(i)
