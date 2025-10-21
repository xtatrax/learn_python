



arr=[]


#arr[1] = 1
arr.insert(2,1)

print(arr)

dic={}

dic[1] = 1
dic[3] = 1
dic[5] = 1
dic[9] = 1
dic[18] = 1
dic[2] = 1

print(dic)

s_dic = sorted(dic.items(), key=lambda x:x[0])

print(s_dic)