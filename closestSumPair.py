# list1 and list2 are the given lists, and target is the target sum.
# The output should be a tuple of two integers, one from each array.

def closest_sum_pair(list1, list2, t):
    l1 = sorted(list1)
    l2 = sorted(list2)
    p1 = 0
    p2 = len(l2) - 1
    best1 = l1[p1]
    best2 = l2[p2]
    closest = l1[p1] + l2[p2]
    while p1 < len(l1) and p2 > -1:
        sum = l1[p1] + l2[p2]
        if abs(t - sum) < abs(t - closest):
            closest = sum
            best1 = l1[p1]
            best2 = l2[p2]
        if sum == t:
            return (best1, best2)
        elif sum < t:
            p1 += 1
        else:
            p2 -= 1
    return (best1, best2)

# NOTE: You can use the following values to test this function.
a1 = [-1, 3, 8, 2, 9, 5]
a2 = [4, 1, 2, 10, 5, 20]
a_target = 24
# closest_sum_pair(a1, a2, a_target) should return (5, 20) or (3, 20).

b1 = [7, 4, 1, 10]
b2 = [4, 5, 8, 7]
b_target = 13
# closest_sum_pair(b1, b2, b_target) should return (4,8), (7, 7), (7, 5), or (10, 4).

c1 = [6, 8, -1, -8, -3]
c2 = [4, -6, 2, 9, -3]
c_target = 3
# closest_sum_pair(c1, c2, c_target) should return (-1, 4) or (6, -3).

d1 = [19, 14, 6, 11, -16, 14, -16, -9, 16, 13]
d2 = [13, 9, -15, -2, -18, 16, 17, 2, -11, -7]
d_target = -15
# closest_sum_pair(d1, d2, d_target) should return (-16, 2) or (-9, -7).
