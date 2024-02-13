Binary Representation

Max Score: 50

Given a positive integer, print its binary representation.



Input Format

The first line of input contains T - the number of test cases. It's followed by T lines, each line containing a single integer.



Output Format

For each test case, print a binary representation, separated by a new line.



Constraints

1 <= T <= 10000

0 <= N <= 109



Example

Input

5

10

15

7

1

120



Output

1010

1111

111

1

1111000



Explanation



Self Explanatory

def bin(n):
    if n>1:
        bin(n >>1)
    print(n & 1,end="")
     
for i in range(int(input())):
    n=int(input())
    bin(n) 
    print()
