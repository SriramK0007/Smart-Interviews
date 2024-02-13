Count Set Bits

Max Score: 50

Given a number N, find the number of bits that are set to 1 in its binary representation.



Input Format

The first line of input contains T - the number of test cases. It is followed by T lines, each line contains a single integer N.



Output Format

For each test case, print the number of bits set to 1 in the binary representation of N, separated by a new line.



Constraints

1 <= T <= 104

0 <= N <= 1018



Example

Input

3

4

15

10



Output

1

4

2



Explanation



Test-Case 1

The binary representation of 4 is 100.

The number of 1's in the binary representation of 4 is 1.



Test-Case 2

The binary representation of 15 is 1111.



def countsetbits(n):
    if n==0:
        return 0
    else:
        return 1 + countsetbits(n &(n-1))
for i in range(int(input())):
    n=int(input()) 
    print(countsetbits(n))
The number of 1's in the binary representation of 15 is 4.
