Rearrange Sequence 1

Max Score: 100

You are given an array of size N containing unique integers. Find the size of the largest subarray that can be rearranged to form a contiguous sequence.

A contiguous sequence means that the difference of adjacent elements should be 1.



Input Format

The first line of input contains T - the number of test cases. It's followed by 2T lines, the first line contains N - the size of the array. The second line contains the elements of the array.



Output Format

For each test case, print the size of the largest subarray that can be rearranged to form a contiguous sequence, on a new line.



Constraints

1 <= T <= 100

1 <= N <= 1000

0 <= A[i] <= 105



Example

Input

2

5

1 3 2 6 5

9

0 8 6 5 7 10 3 2 1



Output

3

4



Explanation



Test-Case 1

The largest subarray that can be rearranged to form a contiguous sequence is [1, 3, 2] which can be rearranged to form [1, 2, 3].



Test-Case 2

The largest subarray that can be rearranged to form a contiguous sequence is [8, 6, 5, 7] which can be rearranged to form [5, 6, 7, 8].




for _ in range(int(input())):
    ans=0
    n=int(input())
    arr=list(map(int,input().split()))
    for i in range(n):
        mi=float('inf')
        ma=float('-inf')
        for j in range(i,n):
            mi=min(mi,arr[j])
            ma=max(ma,arr[j])
            if (ma-mi+1)==j-i+1:
                ans=max(ans,j-i+1)
    print(ans)
