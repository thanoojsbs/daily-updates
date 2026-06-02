# ============================================================
# PROBLEM 1: Find the Smallest Number
# ============================================================
# Problem:
# Given a list of numbers, find the smallest number.
#
# Input: 8 3 15 2 10
# Output: 2
#
# Solution:

nums = list(map(int, input().split()))

smallest = nums[0]

for num in nums:
    if num < smallest:
        smallest = num

print(smallest)


# ============================================================
# PROBLEM 2: Count Characters in a String
# ============================================================
# Problem:
# Find the number of characters in a string (excluding spaces).
#
# Input: hello world
# Output: 10
#
# Solution:

text = input()

count = 0

for ch in text:
    if ch != " ":
        count += 1

print(count)