class Soultion:
    def largest(self,arr):
        largest_Value = -1
        for value in arr:
            if value > largest_Value:
                largest_Value = value
        return largest_Value

data1 = Soultion()
# print(data1.largest([10,20,30,40,50,60,70]))

data2 = Soultion().largest([20,30,80,152,89,56,89])

# print(data2)

data3 = Soultion()
# print(data3.largest([-8]))


class SecondMethodOfLargest:
    def largest(self,arr):
        large = -1
        for value in arr:
            if value > large:
                large = value
        return large


data1 = SecondMethodOfLargest()

print(f"The largest element of given array is : {data1.largest([-1,-2,-3,-4,-5,-6])}")