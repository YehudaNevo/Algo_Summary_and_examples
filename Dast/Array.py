import ctypes


class DynamicArray(object):

    def __init__(self):

        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)

    def __len__(self):
        return self.n

    def __getitem__(self, k):

        if not 0 <= k < self.n:
            return IndexError(f'{k} is out of bound..')

        return self.A[k]

    def append(self, ele):

        if self.n == self.capacity:
            self._resize(2 * self.capacity)

        self.A[self.n] = ele
        self.n += 1

    def _resize(self, new_cap):

        B = self.make_array(new_cap)

        for k in range(self.n):
            B[k] = self.A[k]

        self.A = B

        self.capacity = new_cap

    def make_array(self, new_cap):

        return (new_cap * ctypes.py_object)()


def is_anagram(s1, s2):
    s1.replace(' ', '').lower()
    s2.replace(' ', '').lower()

    # return sorted(s1) == sorted(s2) #              1 solution

    if len(s1) != len(s2):  # second solution
        return False
    count = {}
    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] += 1

        for k in count:
            if count[k] != 0:
                return False

        return True


# if len(s1) == len(s1):#                        third solution
#     for c in s1:
#         if c in s2:
#             s2 = s2.replace(c, '', 1)
#     if len(s2) == 0:
#         return True
# return False


def Array_pair(arr, k):
    seen = set()
    output = set()

    for num in arr:
        target = k - num
        if target not in seen:
            seen.add(num)
        else:
            output.add((target, num))
    return output
    # pairs = [] #  n square solution
    # for i in range(len(arr)):
    #     for j in range(i,len(arr)):
    #         if i + j == k:
    #             pairs.append((i, j))
    # return pairs


def finder(arr1, arr2):
    # return sum(arr1) - sum(arr2) lol

    # one approach  NlogN
    # arr1.sort()
    # arr2.sort()
    # for num1, num2 in zip(arr1, arr2):
    #     if num1 != num2:
    #         return num1
    # return arr1[-1]

    # linear time solution
    elements = {}
    seen = ()

    for a in arr1:
        if a not in seen:
            elements[a] = 1
        else:
            elements[a] += 1
    for a in arr2:
        elements[a] -= 1
    for key, val in elements.items():
        if val > 0:
            return key

#   arr = arr1 + arr2
#   res = 0
#     for num in arr:
#       res ^= num # XOR
#    return res
#

def largest_continuous_sum(arr):
    sum = arr[0]
    max_sum = arr[0]
    temp = []
    for num in arr:
        sum += num
        if sum > max_sum:
            max_sum = sum
    return max_sum


def reverse_sent(str1):
    words = []
    i = 0
    while i < len(str1):
        if str1[i] != ' ':
            start = i
            while i < len(str1) and str1[i] != ' ':
                i += 1
            words.append(str1[start:i])
        i += 1
    return ' '.join(reverse_arr(words))



    # lst = str1.split()
    # new_sent = ''
    # for word in reversed(lst):
    #     new_sent += word
    #     new_sent += ' '
    # return new_sent.strip()

def reverse_arr(arr):
    stuck = arr
    temp = []
    while len(stuck) != 0:
        temp.append(stuck.pop())
    return temp


def string_compression(s):
    size = len(s)
    index = 1
    counter = 1
    compress_word = ''

    while index < size:
        if s[index] == s[index-1]:
            counter += 1
        else:
            compress_word += s[index-1] + str(counter)
            counter = 1
        index += 1
    compress_word += s[index - 1] + str(counter)

    return compress_word




import random

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(len(lst)):
    j = random.randint(i, len(lst) - 1)
    lst[i], lst[j] = lst[j], lst[i]
print(lst)