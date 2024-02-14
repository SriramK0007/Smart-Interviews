Equal 0s and 1s

Max Score: 100

You are given an array of 0's and 1's. Find the length of the longest subarray which has an equal number of 0's and 1's.



Input Format

The first line of input contains T - the number of test cases. It is followed by 2T lines, the first line contains N - the size of the array. The second line contains the elements of the array.



Output Format

For each test case, print the length of the longest subarray which has equal 0's and 1's, separated by a newline.



Constraints

10 points

1 <= T <= 100

1 <= N <= 100



20 points

1 <= T <= 100

1 <= N <= 1000



70 points

1 <= T <= 1000

1 <= N <= 104



Example

Input

2

5

0 1 1 0 1

6

1 1 1 1 1 0



Output

4

2



Explanation



Example 1: The longest subarray which has an equal number of 0's and 1's is [0 1 1 0]



Example 2: The longest subarray which has an equal number of 0's and 1's is [1 0]


for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    countmap={0:-1}
    l=c=0
    for i,num in enumerate(arr):
        c+=1 if num==1 else -1
        if c in countmap:
            l=max(l,i-countmap[c])
        else:
            countmap[c]=i
    print(l)
