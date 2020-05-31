'''

'''


def modify_list(lst):
    for i in range(0, (len(lst)-1), -1):
        if lst[i] // 2 != 0:
            del lst[i]
        else:
            lst[i] = lst[i] // 2


lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))
