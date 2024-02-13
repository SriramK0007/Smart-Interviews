Express as Power Sum

Max Score: 100

Given an integer N, find the number of ways it can be expressed as the sum of the Kth powers of unique natural numbers.



Input Format

The first line of input contains T - the number of test cases. It's followed by T lines, each line containing 2 space-separated integers - N and K.



Output Format

Print the number of ways for each test case, separated by a new line.



Constraints

1 <= T <= 100

1 <= N <= 1000

2 <= K <= 10



Examples

Input

3

10 2

100 2

100 3



Output

1

3

1



Explanation



Test-Case 1

There is only 1 way to express 10 as the sum of squares of unique natural numbers: 12 + 32 = 10



Test-Case 2

There are 3 ways to express 100 as the sum of squares of unique natural numbers: 102 = 62 + 82 = 12 + 32 + 42 + 52 + 72 = 100



Test-Case 3

There is only 1 way to express 100 as the sum of 3rd power of unique natural numbers: 13 + 23 + 33 + 43 = 100



def power_sum(N,K):
    dp=[0] * (N+1)
    dp[0]=1
    for i in range(1,int(N**(1/K))+1):
        power=i**K
        for j in range(N,power-1,-1):
            dp[j]+=dp[j-power]
    return dp[N]
def find_power(T,test_cases):
    results=[]
    for i in range(T):
        N,K=test_cases[i]
        result=power_sum(N,K)
        results.append(result)
    return results
T=int(input())
test_cases=[]
for _ in range(T):
    N,K=map(int,input().split())
    test_cases.append((N,K))
results=find_power(T,test_cases)
for result in results:
    print(result)
