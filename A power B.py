A power B

Max Score: 100

Given 2 numbers - A and B, evaluate AB.



Note:

Do not use any inbuilt functions / libraries for your main logic.



Input Format
The first line of input contains T - the number of test cases. It's followed by T lines, each line containing 2 numbers - A and B, separated by space.



Output Format

For each test case, print AB, separated by new line. Since the result can be very large, print result % 1000000007



Constraints

30 points

1 <= T <= 1000

0 <= A <= 106

0 <= B <= 103



70 points

1 <= T <= 1000

0 <= A <= 106

0 <= B <= 109



Example

Input

4

5 2

1 10

2 30

10 10



Output

25

1

73741817

999999937



Explanation



Self Explanatory


mod=1000000007
def power(base,exp,mod):
    result=1
    base=base % mod
    while exp>0:
        if exp%2==1:
            result=(result*base) % mod
        base=(base * base)% mod
        exp //=2
    return result 
for i in range(int(input())):
    a,b=map(int,input().split())
    print(power(a,b,mod))
