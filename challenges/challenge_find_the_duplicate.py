def find_duplicate(nums):
    obj = {}
    for num in nums:
        obj[num] = obj.get(num, 0) + 1
        if (obj[num] == 2 and num > 0):
            return num
    return False
