Triple Trouble

Given an array of size 3X+1, where every element occurs three times, except one element, which occurs only once. Find the element that occurs only once.



Input Format

The first line of input contains T - the number of test cases. It's followed by 2T lines, the first line contains N - the size of the array (of the form 3X + 1) and second line contains the elements of the array.



Output Format

For each test case, print the number which occurs only once, separated by new line.



Constraints

30 points

1 <= T <= 100

4 <= N <= 103



70 points

1 <= T <= 100

4 <= N <= 106



Example

Input

2

10

5 7 8 7 7 9 5 9 5 9

7

10 20 20 30 20 30 30



Output

8

10



Explanation



Self Explanatory


def findelement(arr):
    ones=0
    twos=0
    for num in arr:
        twos= twos | (ones & num)
        ones = ones ^ num
        commonbit =  ~(ones & twos)
        ones = ones & commonbit
        twos = twos & commonbit
    return ones    
for i in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    unique=findelement(arr)
    print(unique)
