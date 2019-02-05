
def quick_sort(arr):

    ''' Check if array is divisable else 
    retrun single element array '''
    if len(arr)>1:
        
        start_index = 0
        end_index = len(arr)
        mid_index = int((start_index+end_index)/2)

        '''
        Divide the array in 2 sub arrays and arrange them as  
        1 - This will put the mid point in its sorted index
        2 - Smaller then mid_point 
        3 - Greater then mid_point
        '''
        list1 = list(filter(lambda x : x < arr[mid_index],arr))
        list2 = list(filter(lambda x : x > arr[mid_index],arr))

        '''Continue division till we get last undivisable element'''
        list1 = quick_sort(list1)
        
        list2 = quick_sort(list2)

        list1.append(arr[mid_index])

        '''Append sorted sub arrays and return '''
        return(list1+list2)   
    else:
        return arr      


test_unsorted_array = [14, 17, 13, 15, 19, 10, 3, 16, 9, 12]
print(quick_sort(test_unsorted_array))