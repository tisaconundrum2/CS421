#!/usr/bin/env python

in_list = [5, 8, 0, 12, 3, 1, 6, 0]

begin = 0
end = len(in_list)


def merge(in_list, begin, mid, end):
    left_half = []
    right_half = []
    for i in range(begin, mid, 1):
        left_half.append(in_list[i])
    for i in range(mid, end, 1):
        right_half.append(in_list[i])
    i = j = k = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            in_list[k] = left_half[i]  # swap happens here
            i += 1
        else:
            in_list[k] = right_half[j]  # pushing the element in when they are in order
            j += 1
            k += 1

    while i < len(left_half):
        in_list[k] = left_half[i]
        i += 1
        k += 1

    while j < len(right_half):
        in_list[k] = right_half[j]
        j += 1
        k += 1


def merge_sort(in_list, begin, end):
    mid = len(in_list) // 2
    if len(in_list) > 1:
        # mid = len(in_list)//2
        # left_half = in_list[:mid]
        right_half = []
        left_half = []

        for i in range(begin, mid, 1):
            left_half.append(in_list[i])
        for i in range(mid, end, 1):
            right_half.append(in_list[i])

        merge_sort(left_half, begin, len(left_half))
        merge_sort(right_half, begin, len(right_half))
        merge(in_list, begin, mid, end)


# print in_list
# merge_sort(in_list)
# print in_list
# print begin, mid, end

merge_sort(in_list, begin, end)
print(in_list)
