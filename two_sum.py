#!/usr/bin/python

'''
https://blog.csdn.net/coder_orz/article/details/52039233
'''

def two_sum(num_list, target):
    result = []
    num_dict = {}
    for i in range(len(num_list)):
        num_dict[num_list[i]] = i
        if target - num_list[i] in num_dict:
            result = [i, num_dict[target-num_list[i]]]

    return result

num_list = [1, 3, 6, 9, 12, 23, 4, 8, 15]
print two_sum(num_list, 13)
print two_sum(num_list, 100)

