
def merge_sort(array):


    #array should contain more then 1 element
    if len(array) > 1 :

        mid_index = int((0 + len(array)) / 2 )

        first_half = array[:mid_index]
        second_half = array[mid_index:]

        #Keep deividing until we reach smallest undivisable part
        smallest_undivisable_part1 = merge_sort(first_half)
        smallest_undivisable_part2 = merge_sort(second_half)

        #Now start conquering above small parts
        finalSortedOutPut = merge(smallest_undivisable_part1,smallest_undivisable_part2)
        return finalSortedOutPut
        
    else:
        #Return single element array
        return array    

def merge(array1,array2):

    sortedArray = []

    while len(array1) != 0 and len(array2) != 0:

        if array1[0]>array2[0]:

            sortedArray.append(array2[0])
            del array2[0]

        else:

            sortedArray.append(array1[0])
            del array1[0]

    #Sorting is done now simply add remainig in sorted array
    
    while len(array1) != 0 :
        sortedArray.append(array1[0])
        del array1[0]

    while len(array2) != 0 :
        sortedArray.append(array2[0])
        del array2[0] 

    return sortedArray    
                

test_unsorted_array = [14, 17, 13, 15, 19, 10, 3, 16, 9, 12]
print(merge_sort(test_unsorted_array))
        




