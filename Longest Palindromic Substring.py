Longest Palindromic Substring

Max Score: 100

Given a string, find the length of the Longest Palindromic Substring (LPS).



Input Format

The first line of input contains T - the number of test cases. It's followed by 2T lines. The first line has N - the size of the string and the second line contains a string of size N.



Output Format

Print the length of the LPS for each test case, separated by a new line.



Constraints

30 points

1 <= T <= 200

1 <= len(S) <= 100

'a' <= S[i] <= 'z'



70 points

1 <= T <= 200

1 <= len(S) <= 103

'a' <= S[i] <= 'z'



General Constraints

'a' <= S[i] <= 'z'



Example

Input

5

8

pfyafafd

9

sllwffoqq

6

yoogvb

4

hcch

23

mzmqnnrkurfmmfrukrnnqsm



Output

3

2

2

4

18



Explanation



Self Explanatory

def palindrome(s,n1,p1,p2):
    while (p1>=0 and p2<n1 and s[p1]==s[p2]):
        p1-=1
        p2+=1
    return p2-p1-1
for i in range(int(input())):
    n=int(input())
    st=input()
    ans=1
    for p in range(n):
        ans=max(palindrome(st,n,p-1,p+1),ans)
        ans=max(palindrome(st,n,p,p+1),ans)
    print(ans)
