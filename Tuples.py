if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    result=[int(i) for i in integer_list]
    tuple(result)
    print(hash(tuple(result)))
