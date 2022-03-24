# Dynamic programming amounts to breaking down an optimization problem into simpler sub-problems, and storing the
# solution to each sub-problem so that each sub-problem is only solved once.

# step 1 : Identifying the sub problem
# step 2 : Write out the sub-problem as a recurring mathematical decision..( F = max (arr[i] + F( arr[1:]),F(arr[1:]) )
# step 3 : Solve the original problem using Steps 1 and 2
# step 4 : Determine the dimensions of the memoization array and the direction in which it should be filled


# max subset  - no adj...-------------------------------------------------------------------------------------

# recursive solution - not optimal but explain why the problem can be solved in dynamic technic
def maxSubsetSumNoAdjacent_rec(array):
    if len(array) == 0:
        return 0
    elif len(array) == 1:
        return array[0]
    else:
        return max(array[0] + maxSubsetSumNoAdjacent_rec(array[2:]), maxSubsetSumNoAdjacent_rec(array[1:]))


# optimal solution..
def maxSubsetSumNoAdjacent(array):
    if len(array) == 0:
        return 0
    if len(array) < 3:
        return max(array)
    if array[1] < array[0]:
        array[1] = array[0]

    for i in range(2, len(array)):
        array[i] = max(array[i - 1], array[i - 2] + array[i])
    return array[-1]


# longest common subsequence -------------------------------------------------------------------------------

# recursive solution for understanding...
def longestCommonSubsequence_rec(str1, str2, size=0):
    if len(str1) == 0 or len(str2) == 0:
        return size

    elif str1[-1] == str2[-1]:
        return longestCommonSubsequence_rec(str1[:-1], str2[:-1], size + 1)
    else:
        return max(longestCommonSubsequence_rec(str1[:-1], str2, size),
                   longestCommonSubsequence_rec(str1, str2[:-1], size))


# optimal solution
def longestCommonSubsequence(str1, str2):
    res = [[[] for _ in range(len(str1) + 1)] for _ in range(len(str2) + 1)]

    for i in range(1, len(str2) + 1):
        for j in range(1, len(str1) + 1):
            if str2[i - 1] == str1[j - 1]:
                res[i][j] = res[i - 1][j - 1] + [str2[i - 1]]
            else:
                res[i][j] = max(res[i - 1][j], res[i][j - 1], key=len)

    return res[-1][-1]
