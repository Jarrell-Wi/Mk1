def BinarySearch(nums, target):
    if len(nums) == 1:
        return nums
    if target < nums[len(nums) // 2]:
        return BinarySearch(nums[:len(nums) // 2], target)
    else:
        return BinarySearch(nums[len(nums) // 2:], target)
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = 6
print(BinarySearch(a, b))

