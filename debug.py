def threeSum(nums):
    if len(nums) <= 2:
        return []

    nums.sort()
    sol_set = []

    for i, num in enumerate(nums):

        if i > 0 and num == nums[i - 1]:
            continue

        l, r = i + 1, len(nums) - 1
        while l < r:

            threeSum = nums[l] + num + nums[r]

            if threeSum == 0:
                sol_set.append([nums[l], num, nums[r]])
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1

            elif threeSum < 0:
                l += 1

            else:
                r -= 1

    return sol_set


l = [-1,0,1,2,-1,-4]
threeSum(l)
