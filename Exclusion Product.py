Exclusion Product

Max Score: 100

You are given an array of integers of size N. Create a new array such that the element at an index i in the new array is the product of all the elements of the original array except the element present at index i.



Input Format

The first line of input contains T - the number of test cases. For each test case, the first line contains N - the size of the array. The second line contains N integers - the elements of the array.



Output Format

For each test case, print the new array, separated by a new line. Since these numbers can be very large, print the numbers % 109 + 7



Constraints

1 <= T <= 100

1 <= N <= 105

0 <= A[i] <= 105



Example

Input

2

5

1 5 3 2 8

6

4 10 1 2 8 3



Output

240 48 80 120 30

480 192 1920 960 240 640



Explanation



Test-Case 1

The product of all elements of the array except for the element at index 0 is 5 * 3 * 2 * 8 = 240

The product of all elements of the array except for the element at index 1 is 1 * 3 * 2 * 8 = 48

The product of all elements of the array except for the element at index 2 is 1 * 5 * 2 * 8 = 80

The product of all elements of the array except for the element at index 3 is 1 * 5 * 3 * 8 = 120

The product of all elements of the array except for the element at index 4 is 1 * 5 * 3 * 2 = 30


for _ in range(int(input())):
    mod=10**9+7
    n=int(input())
    arr=list(map(int,input().split()))
    pre=[1]*(n)
    suf=[1]*(n)
    pre[0]=arr[0]%mod
    suf[n-1]=arr[n-1]%mod
    for i in range(1,n):
        pre[i]=(pre[i-1]*arr[i])%mod 
    for i in range(n-2,-1,-1):
        suf[i]=(suf[i+1]*arr[i])%mod
    arr[0]=suf[1]%mod
    arr[n-1]=pre[n-2]%mod
    for i in range(1,n-1):
        arr[i]=pre[i-1]*suf[i+1]%mod
    for i in arr:
        print(i , end=" ")
    print()
