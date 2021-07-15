def find_max_number(lst):
    num= float('-inf')
    for i in lst:
        if i > num:
            max_number=i
            num=i
    return max_number


print(find_max_number([10,1,70,5,100,8,299,20]))
