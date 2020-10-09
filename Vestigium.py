no_of_testcases = int(input())
trace = [0 for x in range(no_of_testcases)]
dup_row = [0 for x in range(no_of_testcases)]
dup_col = [0 for x in range(no_of_testcases)]

for i in range(no_of_testcases):
    size = int(input())
    matrix = [[0 for x in range(size)] for y in range(size)]
    for j in range(size):
        row = input().split(" ")
        for k in range(size):
            matrix[j][k] = row[k]
    
    for j in range(size):
        for k in range (size):
            if(j==k):
                trace[i] = trace[i] + int(matrix[j][k])
    
    for m in range(size):
        flag = 0
        for j in range(size):
            for k in range(j+1,size):
                if(matrix[m][j]==matrix[m][k]):
                    flag = 1
        if(flag==1):
            dup_row[i] = dup_row[i] + 1
        
    for m in range(size):
        flag = 0
        for j in range(size):
            for k in range(j+1,size):
                if(matrix[j][m]==matrix[k][m]):
                    flag = 1
        if(flag==1):
            dup_col[i] = dup_col[i] + 1

for i in range(no_of_testcases):
    print("Case #{0}: {1} {2} {3}".format(i+1,trace[i],dup_row[i],dup_col[i]))