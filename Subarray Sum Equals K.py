def subarraySum(nums, k):
    d = dict()
    summa = 0
    count = 0
    for el in nums:
        if summa not in d.keys():
            d[summa] = 1
        else:
            d[summa] += 1

        summa += el
        if summa - k in d.keys():
            count += d[summa - k]

    return count



print(subarraySum([1,2,3], 5))