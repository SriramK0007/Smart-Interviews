Number of Valid Subarrays

Max Score: 100

You are given an array containing only 0s and 1s. You have to find the number of subarrays which has equal number of 0s and 1s.



Input Format

The first line of input contains T - the number of test cases. It is followed by 2T lines - the first line contains N - the size of the array. The second line contains the elements of the array.



Output Format

For each test case, output the number of subarrays having equal number of 0s and 1s, separated by a newline.



Constraints

10 points

1 <= T <= 100

1 <= N <= 100



20 points

1 <= T <= 100

1 <= N <= 1000



70 points

1 <= T <= 100

1 <= N <= 50000



Example

Input

3

4

1 0 1 0

10

1 0 1 0 0 1 0 0 1 1

4

1 1 1 1



Output

4

14

0



Explanation



Self Explanatory




def valids(arr):
    mp={}
    sumv=0
    c=0
    for num in arr:
        if num==0:
            num=-1
        sumv+=num
        if sumv==0:
            c+=1
        if sumv in mp:
            c+=mp[sumv]
        mp[sumv]=mp.get(sumv,0)+1
    return c
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    print(valids(arr))
