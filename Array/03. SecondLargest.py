class SecondLargestElement:
    def SecondLargest(self,arr):
        largest = float('-inf')
        for value in arr:
            if value > largest:
                largest = value
        secondLargest = float('-inf')
        for value in arr:
            if secondLargest < value and largest > value:
                secondLargest = value
        return secondLargest
    
# data1 = SecondLargestElement()
# print(data1.SecondLargest([-10,-20,-30,-40,-50,-60]))



class AnotherMethod:
    def SecondMethod(self,arr):
        largest = max(arr)
        second_largest = float('-inf')
        for value in range(0,len(arr)):
            if second_largest < arr[value]  and largest > arr[value]:
                second_largest = arr[value]
        return second_largest

data2 = AnotherMethod()
print(data2.SecondMethod([-1,-2,-4,-5,-6,0,1]))