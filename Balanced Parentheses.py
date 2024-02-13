Balanced Parentheses

Max Score: 100

Write a program to generate all possible strings with balanced parentheses having N pairs of curly braces.



Input Format

The first line of input contains T - the number of test cases. It's followed by T lines, each containing a single integer N.



Output Format

For each test case, print each combinational pair of balanced parenthesis of length N in a lexicographical order along with the test case number, separated by a new line.



Constraints

1 <= T <= 12

1 <= N <= 12



Example

Input

2

3

2



Output

Test Case #1:
{{{}}}
{{}{}}
{{}}{}
{}{{}}
{}{}{}
Test Case #2:
{{}}
{}{}


Explanation



Self Explanatory


def par(num,a,open,close,i):
    if i==num*2:
        b=''.join(a)
        print(b)
        return
    if open < num:
        a[i]='{'
        par(num,a,open+1,close,i+1)
    if open>close:
        a[i]='}'
        par(num,a,open,close+1,i+1)
for i in range(1,int(input())+1):
    print(f"Test Case #{i}:")
    num=int(input())
    a=['']*num*2
    par(num,a,0,0,0)
