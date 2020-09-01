if __name__ == '__main__':
    n = int(input())
    sum=0
    student_marks = {}
    for i in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
        student_marksi={}
        student_marksi[name]=scores

    query_name = input()
    for i,j in student_marks.items():
        if i==query_name:
            lst=j.copy()
            summation=(lst[0]+lst[1]+lst[2])/3
            print(f'{summation:.2f}')
