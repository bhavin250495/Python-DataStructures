
'''Insertion sort is simply checking if value is greater then its previous value
if yes then hold its  value to insert somwhere else and make its index available for another element
Now keep swaping the values at hole till you reach starting index 
'''


def insertion_sort(array):
    
        for i in range(1,len(array)):
            if array[i] < array[i-1]:
                print(i)
                hole = i
                key = array[hole]
                while array[hole - 1]>key:
                    array[hole],array[hole-1] = array[hole-1],array[hole]
                    '''Keep decreasing hole index till we reach starting index'''
                    if hole > 1:
                        hole-=1            
        print(array)    
            

test_unsorted_array = [14, 17, 13, 15, 19, 10, 3, 16, 9, 12]
insertion_sort(test_unsorted_array)      
