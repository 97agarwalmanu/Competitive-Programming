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

if __name__ == "__main__":
    arr = [3,4,2,1,5]
    sort_obj = Sorting()
    arr = sort_obj.insertion_sort(arr)
    print(arr)