#!/usr/bin/env python

in_list = [5, 8, 0, 12, 3, 1, 6]

mid = len(in_list)//2
begin = 0
end = len(in_list)

def merge_sort(in_list, begin, mid, end):
    if len(in_list)>1:
        #mid = len(in_list)//2
        #left_half = in_list[:mid]
        for i in range(begin, mid, 1):
            left_half = in_list[i]
        for i in range(begin, mid, 1):
            right_half = in_list[i]
        #right_half = in_list[mid:]
        
        #merge_sort(left_half)
        merge_sort(in_list, begin, mid, end)
        #merge_sort(right_half)
        
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                in_list[k] = left_half[i]
                i = i + 1
            else:
                in_list[k] = right_half[j]
                j = j + 1
            k = k + 1
            
        while i < len(left_half):
            in_list[k] = left_half[i]
            i = i + 1
            k = k + 1
            
        while j < len(right_half):
            in_list[k] = right_half[j]
            j = j + 1
            k = k + 1
            
#print in_list            
#merge_sort(in_list)
#print in_list
#print begin, mid, end
