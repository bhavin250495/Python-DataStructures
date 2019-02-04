
def quick_sort(arr):

    # Check if array is divisable
    if len(arr)>1:
        
        start_index = 0
        end_index = len(arr)
        mid_point = int((start_index+end_index)/2)

        list1 = list(filter(lambda x : x < arr[mid_point],arr))
        list2 = list(filter(lambda x : x > arr[mid_point],arr))

        list1 = quick_sort(list1)
        list2 = quick_sort(list2)

        list1.append(arr[mid_point])

        return(list1+list2)   
    else:
        return arr      


test_unsorted_array = [14, 17, 13, 15, 19, 10, 3, 16, 9, 12]
print(quick_sort(test_unsorted_array))