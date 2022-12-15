some_str = map(int, input().split(' '))
list = sorted(some_str)
print(list)
new_list = []
result_list = []
for i in range(0, len(list)):
    if i != len(list)-1 and list[i] == list[i+1]-1:
        new_list.append(list[i])
    else:
        new_list.append(list[i])
        if len(new_list) == 1:
            result_list.append(str(new_list[0]))
        else:
            result_list.append(str(new_list[0]) + '-' + str(new_list[len(new_list)-1]))
        
        new_list = []

print(result_list)