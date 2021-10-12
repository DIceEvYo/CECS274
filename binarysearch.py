
class bso():
    def __init__(self):
        # Every node holds a key and a value
        self.first_index = None
        self.last_index = None

    def binary_search(self, arr, target):
        print(1)
        lo = 0
        hi = len(arr) - 1
        if (hi >= lo):
            while lo < hi:
                mid = (lo + hi) // 2
                if arr[mid] == target:
                    print(2)
                    try:
                        try:
                            if (arr[mid + 1] != mid):
                                self.last_index = mid
                        except:
                            k = "waste"
                        try:
                            if (arr[mid + 1] != mid):
                                self.first_index = mid
                        except:
                            k = "waste"
                    except:
                        return mid
                elif arr[mid] > target:
                    self.binary_search(arr, ((mid - 1) + lo) // 2)
                else:
                    self.binary_search(arr, ((mid + 1) + hi) // 2)
        else:
            return -1

    def binary_searchOccurence(self, arr,target):
        print(1)
        temp = arr
        index = self.binary_search(arr,target)
        temp2 = []
        print(2)
        for i in range (0,index):
            temp2[i] = temp[i]
        for i in range (index+1,len(temp)):
            temp2[i] = temp[i]
        temp = temp2
        index = self.binary_search(arr, target)
        print(3)
t = 4
arr = [0, 1, 2, 3, 4, 4, 4, 4, 5, 6, 7, 8]
b = bso()
b.binary_searchOccurence(arr,t)
print("FI",b.first_index, "LI", b.last_index)