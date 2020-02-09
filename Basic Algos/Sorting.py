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

if __name__ == "__main__":
    arr = [3,4,2,1,5]
    sort_obj = Sorting()
    arr = sort_obj.merge_sort(arr)
    print(arr)