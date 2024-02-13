First Repeating Character - 1

Max Score: 50

Given a string of characters, find the first repeating character.



Input Format

The first line of input contains T - the number of test cases. It's followed by T lines, each line contains a single string of characters.



Output Format

For each test case, print the first repeating character, separated by a new line. If there are none, print '.'.



Constraints

1 <= T <= 1000

'a' <= str[i] <= 'z'

1 <= len(str) <= 104



Example

Input

4

datastructures

algorithms

smartinterviews

hackerrank



Output

a

.

s

a



Explanation



Self Explanatory



from collections import Counter
for i in range(int(input())):
    str=Counter(input())
    f=1
    for i in str.keys():
        if str[i]>1:
            print(i)
            f=0
            break
    if f:
        print(".")
