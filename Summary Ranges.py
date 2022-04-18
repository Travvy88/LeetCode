def summaryRanges(nums):
    if not nums:
        return []

    start = nums[0]
    nums.append(nums[-1] + 2)
    ans = []
    for i in range(len(nums) - 1):
        if nums[i+1] - nums[i] > 1:
            if start == nums[i]:
                ans.append(str(start))
            else:
                ans.append(f'{start}->{nums[i]}')
            start = nums[i+1]
    return ans

print(summaryRanges([1, 1, 1, 1, 10]))