def merge_the_tools(string, k):
    for i in range(0,len(string),k):
        new=list(dict.fromkeys(string[i:i+k]))
        print(''.join(new))
        
            
    # your code goes here

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)