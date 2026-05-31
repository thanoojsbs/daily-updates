# ============================================================
# PROBLEM 1: Find Largest Number
# ============================================================
# Problem Statement:
# Given three integers A, B, and C, find the largest number among them.
#
# Input Format: Three space-separated integers.
# Sample Input: 10 25 15
# Sample Output: 25
#
# Solution:

a, b, c = map(int, input().split())

largest = a

if b > largest:
    largest = b

if c > largest:
    largest = c

print(largest)


# ============================================================
# PROBLEM 2: Sum of First N Natural Numbers
# ============================================================
# Problem Statement:
# Given an integer N, find the sum of first N natural numbers.
#
# Input Format: A single integer N.
# Sample Input: 5
# Sample Output: 15
# Explanation: 1 + 2 + 3 + 4 + 5 = 15
#
# Solution:

n = int(input())

total = 0

for i in range(1, n + 1):
    total += i

print(total)