# ============================================================
# PROBLEM 1: Reverse a String
# ============================================================
# Problem Statement:
# Given a string S, print its reverse.
#
# Input Format: A single string S.
# Sample Input: hello
# Sample Output: olleh
#
# Solution:

s = input()

print(s[::-1])

# Alternative Solution:
# s = input()
#
# reverse = ""
#
# for ch in s:
#     reverse = ch + reverse
#
# print(reverse)


# ============================================================
# PROBLEM 2: Count Vowels in a String
# ============================================================
# Problem Statement:
# Given a string S, count the number of vowels present in it.
#
# Vowels are: a, e, i, o, u (both uppercase and lowercase)
#
# Input Format: A single string.
# Sample Input: programming
# Sample Output: 3
# Explanation: Vowels are: o, a, i
#
# Solution:

s = input()

count = 0

for ch in s.lower():
    if ch in "aeiou":
        count += 1

print(count)

# Example:
# Input: Education
# Output: 5