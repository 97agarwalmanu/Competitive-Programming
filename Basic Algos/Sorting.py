class Sorting:
    def bubble_sort(self, arr):
        n = len(arr)
        sorted = True
        for i in range(n-1):
            for j in range(n - i -1):
                if arr[j] > arr[j+1]: 
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    sorted = False
            if sorted: 
                break
        return arr

    def selection_sort(self, arr):
        n = len(arr)
        for i in range(n-1):
            min = i
            for j in range(i+1, n):
                if arr[j] < arr[min]:
                    min = j
            if i != min: arr[i], arr[min] = arr[min], arr[i]
        return arr
    
    def insertion_sort(self, arr):
        n = len(arr)
        for i in range(1,n):
            hole = i
            while hole > 0 and arr[hole - 1] > arr[hole]:
                arr[hole], arr[hole -1] = arr[hole -1], arr[hole]
                hole -= 1
        return arr
    
    def merge_sort(self, arr):
        n = len(arr)
        if n < 2: return arr
        mid = int(n/2)
        left_arr = [arr[i] for i in range(mid)]
        right_arr = [arr[i] for i in range(mid, n)]
        left_arr = self.merge_sort(left_arr)
        right_arr = self.merge_sort(right_arr)
        return self.__merge_array(left_arr, right_arr, arr)

    def __merge_array(self, left_arr, right_arr, arr):
        nl, nr = len(left_arr), len(right_arr)
        i, j, k = 0, 0, 0
        while(i < nl and j < nr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i +=1
            else:
                arr[k] = right_arr[j]
                j +=1
            k +=1
        while( i < nl):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        while j < nr:
            arr[k] = right_arr[j]
            j +=1
            k +=1 
        return arr 

    def quick_sort(self, arr, start, end):
        if start < end:
            pivot_index = self.__partition(arr, start, end)
            self.quick_sort(arr, start, pivot_index - 1)
            self.quick_sort(arr, pivot_index + 1, end)
    
    def __partition(self, arr, start, end):
        pivot_value = arr[end]
        partition_index = start
        for i in range(start, end):
            if arr[i] <= pivot_value:
                arr[i], arr[partition_index] = arr[partition_index], arr[i]
                partition_index += 1
        arr[end] , arr[partition_index] = arr[partition_index], arr[end] 
        return partition_index
    
    

import time
import random
if __name__ == "__main__":
    n = 100
    random.seed(1)
    arr = [random.randint(0,n) for i in range(n)]
    sort_obj = Sorting()
    t1 = time.time()
    sorted_arr = sort_obj.bubble_sort(arr)
    print("Time taken by bubble sort : %f" % (time.time() - t1))
    t1 = time.time()
    sorted_arr = sort_obj.insertion_sort(arr)
    print("Time taken by insertion sort : %f" % (time.time() - t1))
    t1 = time.time()
    sorted_arr = sort_obj.selection_sort(arr)
    print("Time taken by selection sort : %f" % (time.time() - t1))
    t1 = time.time()
    sorted_arr = sort_obj.merge_sort(arr)
    print("Time taken by merge sort : %f" % (time.time() - t1))
    t1 = time.time()
    sort_obj.quick_sort(arr, 0, len(arr) - 1)
    print("Time taken by quick sort : %f" % (time.time() - t1))