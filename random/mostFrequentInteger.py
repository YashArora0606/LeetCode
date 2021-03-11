# Source: Google Coding Interview - https://www.youtube.com/watch?v=yeCsuIk9vp0

def most_frequent_integer(nums):
    if len(nums) == 0:
        return None
    unique = {}
    most_frequent_amount = 0
    for num in nums:
        if num in unique:
            unique[num] += 1
        else:
            unique[num] = 1
        if unique[num] > most_frequent_amount:
            most_frequent_key = num
            most_frequent_amount = unique[num]
    return most_frequent_key

def print_pairs_sum_to_n(nums, n):
    compliments = {}
    for num in nums:
        if n-num in compliments:
            compliments[n-num] += 1
        else:
            compliments[n-num] = 1
    for num in nums:
        if num in compliments:
            if compliments[n-num] > 0 and compliments[num] > 0:
                compliments[num] -= 1
                compliments[n-num] -= 1
                if num > n - num:
                    num = n - num
                print(str(num) + " " + str(n - num))



print_pairs_sum_to_n([1, 2, 3], 5)
