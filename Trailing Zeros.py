Trailing Zeros

Max Score: 100

Count the number of trailing 0s in the factorial of a given number.



Input Format

The first line of input contains T - the number of test cases. It is followed by T lines, each containing an integer N.



Output Format

For each test case, print the number of trailing 0s in N!, separated by a new line.



Constraints

1 <= T <= 10000

1 <= N <= 1015



Example

Input

3

2

5

100



Output

0

1

24



Explanation



2! = 2 [No trailing zeros]

5! = 120 [Trailing zeros=1]

20! = 2432902008176640000 [Trailing zeros=4]


def count_zeroes(n):
    count=0
    while n>=5:
        n//=5
        count+=n
    return count
for i in range(int(input())):
    N=int(input())
    print(count_zeroes(N))
