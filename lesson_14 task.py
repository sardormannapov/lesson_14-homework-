nums = [3, 2, 7, 5, 9, -3]
n = len(nums)
for i in range(n):
    for j in range(n - i -1):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
print(nums)