from collections import OrderedDict 
no_of_testcases = int(input())
res = [0 for x in range(no_of_testcases)]

for i in range(no_of_testcases):
    flag = 0
    c_busy=0
    j_busy=0
    no_of_activities = int(input())
    start_time = [0 for x in range(no_of_activities)]
    end_time = [0 for x in range(no_of_activities)]
    dic = {}
    for j in range(no_of_activities):
        start_time[j],end_time[j] = input().split()
    
    start_time = (list(map(int, start_time)))
    end_time = (list(map(int, end_time)))

    dic = {start_time[i]: end_time[i] for i in range(no_of_activities)}
    dic = OrderedDict(sorted(dic.items()))
    start_time = sorted(start_time)
    work = ''
    work = work + "C"
    for m in range(len(start_time)-1):
        if(dic[start_time[m]] <= start_time[m+1] and c_busy==0):
            work = work + "C"
            c_busy = 1
        elif(dic[start_time[m]] > start_time[m+1] and j_busy==0):
            if(work[-1]=='J' and dic[start_time[m-1]]>start_time[m]):
                flag = 1
                break
            else:
                work = work + "J"
    if(flag == 1):
        res[i] = "IMPOSSIBLE"
    else:
        res[i] = work
    
for i in range(no_of_testcases):
    print(res[i])
