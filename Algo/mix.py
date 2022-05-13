# # import os
# #
# # # just to check if there is compile time error
# #
# #
# # if os.system("g++ -o a  foo.cpp") == 0:
# #     print("Worked")
# #     # os.system('./a --target="int(5)"')
# # else:
# #     print("Failed")
#
#
# # you can write to stdout for debugging purposes, e.g.
# # print("this is a debug message")
#
# def solution(S):
#     lst = S.split()
#
#     mx = -1
#     for word in lst:
#         if valid_word(word):
#             temp_len = len(word)
#             if temp_len > mx:
#                 mx = temp_len
#
#     return mx
#
#
# def odd_digits(word):
#     count = 0
#     for let in word:
#         if '0' <= let <= '9':
#             count += 1
#     return (count % 2) == 1
#
#
# def even_let(word):
#     count = 0
#     for let in word:
#         if 'A' <= let <= 'Z' or 'a' <= let <= 'z':
#             count += 1
#     return (count % 2) == 0
#
#
# def valid_word(word):
#     for let in word:
#         if 'A' <= let <= 'Z' or 'a' <= let <= 'z' or '0' <= let <= '9':
#             continue
#         else:
#             return False
#     return (even_let(word) and odd_digits(word))
#
#
#
# def subarraySort(array):
#     sorted_array = array.sort()
#     left = -1
#     for i in range(len(array)):
#         if array[i] != sorted_array[i]:
#             left = i
#             break
#
#     right = -1
#     for i in reversed(range(len(array))):
#         if array[i] != sorted_array[i]:
#             right = i
#             break
#     return [left, right]
#
#
#
# dict = {}
#
# if 0 in dict.keys


#
# def f (str):
#     cap = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O',
#            'P','Q','R','S','T','U','V','W','X','Y','Z']
#
#     small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
#            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#
#
#     res = []
#     for i in range(len(cap)):
#         if cap[i] in str and small[i]in str:
#             res.insert(0,cap[i])
#
#     if len(res) == 0:
#         return "NO"
#     else:
#         return res[0]
#
#
#
#
#
# class Solution:
#     def sumZero(self, n):
#         ans=[]
#         for i in range(1,n//2+1):
#             ans.append(i)
#             ans.append(-i)
#         if n % 2 !=0:
#             ans.append(0)
#         return ans
#
#
#
#
#
# def func (num):
#     res= []
#     for i in range(1, num//2 + 1):
#         res.append(i)
#         res.append(-i)
#     if num % 2 != 0:
#         res.append(0)
#     return res
#
# res = []
#
#
# def permutations(str,res, iter = 0):
#     if iter == len(str):
#         temp = "".join(str)
#         res.append(temp)
#
#     for i in range(iter, len(str)):
#
#         str_copy = [c for c in str]
#
#         str_copy[iter], str_copy[i] =str_copy[i], str_copy[iter]
#
#         permutations(str_copy,res, iter + 1)
#     return res
#
#
# str = "po"
# for i in range(2):
#     str+='a'
# print(str)
#
# def erase_triple(lst):
#     for idx,str in enumerate(lst):
#         if "aaa" in str or "bbb" in str or "ccc"in str:
#             lst[idx] = ""

#
# def func(a, b, c):
#     str = ""
#     while more_then_one(a, b, c):
#         str += letters_to_insert(a, b, c)
#         a, b, c = update(a, b, c)
#     # in that point wll have only one type of letter to insert
#     let, num = remine_let(a, b, c)
#     while num > 0:
#         idx = place_to_insert(str, let)
#         if idx == -1:
#             break
#         else:
#             num -= 1
#             str = str[:idx] + let + str[idx:]
#     print(str,len(str))
#
#
# def more_then_one(a, b, c):
#     return a * b != 0 or a * c != 0 or b * c != 0
#
#
# def letters_to_insert(a, b, c):
#     str = ""
#     if a != 0:
#         str += 'a'
#     if b != 0:
#         str += 'b'
#     if c != 0:
#         str += 'c'
#     return str
#
#
# def update(a, b, c):
#     if a != 0:
#         a -= 1
#     if b != 0:
#         b -= 1
#     if c != 0:
#         c -= 1
#     return a, b, c
#
#
# def remine_let(a, b, c):
#     if a != 0:
#         return 'a', a
#     if b != 0:
#         return 'b', b
#     if c != 0:
#         return 'c', c
#     else:
#         return 'a', 0
#
#
# def place_to_insert(str, let):
#     # edge cases
#     if str[0] != let:
#         return 0
#     if str[1] != let:
#         return 0
#     elif str[-1] != let:
#         return len(str)
#     elif str[-2] != let:
#         return len(str)
#     #
#     else:
#         for i in range(3, len(str) - 4):
#             if str[i] != let and str[i + 1] != let or str[i - 1] != let and str[i + 1] != let:
#                 return i +1
#         return -1
#
#
# func(160,8,30)