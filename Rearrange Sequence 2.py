Rearrange Sequence 2

Max Score: 100

You are given an array of size N containing integers which may not be unique. Find the size of the largest subarray that can be rearranged to form a strictly contiguous sequence.



Input Format

The first line of input contains T - number of test cases. Its followed by 2T lines, the first line contains N - the size of the array. The second line contains the elements of the array.



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

4 3 3 1 1

9

8 8 6 7 3 5 7 1 1



Output

2

3



Explanation



Test-Case 1

The largest subarray which can be rearranged to form a contiguous sequence here, is {4, 3} which can be rearranged to form {3, 4}.



Test-Case 2

The largest subarray which can be rearranged to form a contiguous sequence here, is {8, 6, 7} which can be rearranged to form {6, 7, 8}.

for _ in range(int(input())):
    ans=0
    n=int(input())
    arr=list(map(int,input().split()))
    for i in range(n):
        hs=set()
        mi=float('inf')
        ma=float('-inf')
        for j in range(i,n):
            mi=min(mi,arr[j])
            ma=max(ma,arr[j])
            hs.add(arr[j])
            if (ma-mi+1)==len(hs):
                ans=max(ans,len(hs))
    print(ans)
