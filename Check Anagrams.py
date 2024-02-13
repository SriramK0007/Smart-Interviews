Check Anagrams

Max Score: 50

Given 2 strings, check if they are anagrams. An anagram is a rearrangement of the letters of one word to form another word. In other words, some permutations of string A must be the same as string B.



Input Format

The first line of input contains T - the number of test cases. It's followed by T lines, each line containing 2 space-separated strings.



Output Format

For each test case, print True/False, separated by a new line.



Constraints

10 points

1 <= T <= 100

1 <= len(S) <= 103

'a' <= S[i] <= 'z'



40 points

1 <= T <= 100

1 <= len(S) <= 105

'a' <= S[i] <= 'z'



Example

Input

4

iamlordvoldemort tommarvoloriddle

b h

stop post

hi hey



Output

True

False

True

False



Explanation



Self Explanatory

n=int(input())
for i in range(n):
    g1,g2=map(str,input().split())
    if sorted(g1)==sorted(g2):
        print("True")
    else:
        print("False")
