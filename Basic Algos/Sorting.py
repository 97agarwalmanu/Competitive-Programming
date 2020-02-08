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
