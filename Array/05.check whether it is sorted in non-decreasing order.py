class IsSorted:
    def IsSortedValue(self,arr):
        isSortedValue = True
        for i in range(1,len(arr)):
            if arr[i] < arr[i-1]:
                isSortedValue = False
                break
        return isSortedValue

data = IsSorted()
print(data.IsSortedValue([10,20,30,40,50,60]))