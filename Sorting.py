


def selection_sort(arr):
    min_idx = 0

    for i in range(0,len(arr)):
        swaped = True
        print("Top loop",i)
        min_idx = i
        for j in range(i+1,len(arr)-1):
            print("Inner loop",j)
            if arr[j]<arr[min_idx]:
                swaped = False
                min_idx = j
                arr[i],arr[min_idx] = arr[min_idx],arr[i]
        if  swaped:
            break          
    print(arr) 

def bubble_sort(arr):
    for i in range(0,len(arr)):
        print("Top loop",i)
        for j in range(0,len(arr)-1):
            print("Inner loop",j)
            
            if arr[j]>arr[j+1]:
                arr[j+1],arr[j] = arr[j],arr[j+1]  

    print(arr)       

def optimized_bubble_sort(arr):

    for i in range(0,len(arr)):
        print("Top loop",i)
        swaped = True

        for j in range(0,len(arr)-1):
            print("Inner loop",j)
            
            if arr[j]>arr[j+1]:
                arr[j+1],arr[j] = arr[j],arr[j+1]
                swaped = False
        if  swaped:
            break   

    print(arr)        

unsorted_array = [9,8,7,6,5,4,1,2,3]
selection_sort(unsorted_array)         






           
