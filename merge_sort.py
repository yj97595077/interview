#!/usr/bin/python

def merge_two_lists(l1, l2):
    if not l1 and l2:
        l = l2
    elif l1 and not l2:
        l = l1
    else:
        l = []
        while l1 and l2:
            a = l1[0]
            b = l2[0]
            if a > b:
                l.append(b)
                l2.pop(0)
            else:
                l.append(a)
                l1.pop(0)

        if l1:
            l += l1
        if l2:
            l += l2

    return l


def merge_sort(l):
    l_len = len(l)
    l1 = l[:l_len/2]
    l2 = l[l_len/2:]
    if len(l1) == 0 or len(l2) == 0:
        l_sorted = merge_two_lists(l1, l2)
    else:
        l1_sorted = merge_sort(l1)
        l2_sorted = merge_sort(l2)
        l_sorted = merge_two_lists(l1_sorted, l2_sorted)

    return l_sorted

print merge_sort([10, 5, 20, 13, 4, 74, 29, 54, 42, 100, 2])

