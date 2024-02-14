Collecting Water

Max Score: 100

You are given the heights of N buildings. All the buildings are of width 1 and are adjacent to each other with no empty space in between. Assume that it is raining heavily, and as such water will be accumulated on top of certain buildings. Your task is to find the total amount of water accumulated.



Input Format

The first line of input contains T - the number of test cases. It's followed by 2T lines, the first line contains N - the number of buildings. The second line contains N elements denoting the height of the buildings.



Output Format

For each test case, print the units of water accumulated, separated by a new line.



Constraints

30 points

1 <= T <= 1000

1 <= N <= 1000

1 <= a[i] <= 1000



70 points

1 <= T <= 1000

1 <= N <= 100000

1 <= a[i] <= 1000



Example

Input

2

7

1 6 2 4 5 7 9 

5

3 2 7 4 7 



Output

7

4



Explanation



Test-Case 1

Water accumulated on top of Building-1 : 0

Water accumulated on top of Building-2 : 0

Water accumulated on top of Building-3 : 4

Water accumulated on top of Building-4 : 2

Water accumulated on top of Building-5 : 1

Water accumulated on top of Building-6 : 0

Water accumulated on top of Building-7 : 0

Total = 0 + 0 + 4 + 2 + 1 + 0 + 0 = 7



Test-Case 2

Water accumulated on top of Building-1 : 0

Water accumulated on top of Building-2 : 1

Water accumulated on top of Building-3 : 0

Water accumulated on top of Building-4 : 3

Water accumulated on top of Building-5 : 0

Total = 0 + 1 + 0 + 3 + 0 = 4



def getwater(arr,n,left,right):
    ans=0
    for i in range(1,n-1):
        if min(left[i-1],right[i+1])-arr[i]>0:
            ans+=min(left[i-1],right[i+1])-arr[i]
    return ans
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    left=[arr[0]]
    right=[]
    m=arr[0]
    for i in range(1,n):
        m=max(arr[i],m)
        left.append(m)
    m=arr[-1]
    for i in range(n-1,-1,-1):
        m=max(arr[i],m)
        right.append(m)
    print(getwater(arr,n,left,list(reversed(right))))
