##############################################################################
##  Linear Search
##############################################################################


    


##############################################################################
##  Binary Search    
##----------------------------------------------------------------------------
"""
   * We can achieve O(logN) but the array must be sorted
"""

   
    

##############################################################################
##  Selection Sort    
##----------------------------------------------------------------------------
"""
   * The selection sort algorithm sorts an array by repeatedly finding 
     the minimum element (considering ascending order) from unsorted part 
     and putting it at the beginning. 
     
   * The algorithm maintains two subarrays in a given array.
     1) The subarray which is already sorted.
     2) Remaining subarray which is unsorted.

   * In every iteration of selection sort, the minimum element (considering 
     ascending order) from the unsorted subarray is picked and moved to the 
     sorted subarray.
"""



##############################################################################
##  Insertion Sort    
##----------------------------------------------------------------------------
"""
   * Insertion sort is a simple sorting algorithm that works similar to the 
     way you sort playing cards in your hands. 
     
   * The array is virtually split into a sorted and an unsorted part. 
     Values from the unsorted part are picked and placed at the correct 
     position in the sorted part.

   * To sort an array of size n in ascending order:
     1: Iterate from arr[1] to arr[n] over the array.
     2: Compare the current element (key) to its predecessor.
     3: If the key element is smaller than its predecessor, compare it to 
        the elements before. Move the greater elements one position up to 
        make space for the swapped element.
"""




##############################################################################
##  Bubble Sort    
##----------------------------------------------------------------------------
"""
   * Bubble Sort is the simplest sorting algorithm that works by 
     repeatedly swapping the adjacent elements if they are in wrong order.
"""

    
    

"""
   * Optimized Implementation:
     - The above function always runs O(n^2) time even if the array is sorted. 
     - It can be optimized by stopping the algorithm if inner loop didn’t 
       cause any swap.
"""      




##############################################################################
##  Quick Sort    
##----------------------------------------------------------------------------
"""
   * QuickSort is a Divide and Conquer algorithm. It picks an element 
     as pivot and partitions the given array around the picked pivot. 
     
   * There are many different versions of quickSort that pick pivot in 
     different ways.
     1) Always pick first element as pivot.
     2) Always pick last element as pivot (implemented below)
     3) Pick a random element as pivot.
     4) Pick median as pivot.

   * The key process in quickSort is partition(). 
     - Target of partitions is, given an array and an element x of array 
       as pivot, put x at its correct position in sorted array and 
       put all smaller elements (smaller than x) before x, and 
       put all greater elements (greater than x) after x. 
     - All this should be done in linear time.
"""

# This function takes last element as pivot, places 
# the pivot element at its correct position in sorted 
# array, and places all smaller (smaller than pivot) 
# to left of pivot and all greater elements to right 
# of pivot 





##############################################################################
##  Merge Sort    
##----------------------------------------------------------------------------
"""
   *  Merge Sort is a Divide and Conquer algorithm. 
      - It divides input array in two halves, calls itself for the two halves 
        and then merges the two sorted halves. 
      - The merge() function is used for merging two halves. 
      - The merge(arr, l, m, r) is key process that assumes that arr[l..m] 
        and arr[m+1..r] are sorted and merges the two sorted sub-arrays 
        into one. See following implementation for details.

   * MergeSort(arr, l,  r)
     If r > l
     1. Find the middle point to divide the array into two halves:  
             middle m = (l+r)/2
     2. Call mergeSort for first half:   
             Call mergeSort(arr, l, m)
     3. Call mergeSort for second half:
             Call mergeSort(arr, m+1, r)
     4. Merge the two halves sorted in step 2 and 3:
             Call merge(arr, l, m, r)
"""

