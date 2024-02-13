Interleavings

Max Score: 100

Given 2 strings A and B, print all the interleavings of the 2 strings. An interleaved string of given two strings preserves the order of characters in individual strings and uses all the characters of both the strings. For simplicity, you can assume that the strings have unique characters.



Input Format

The first line of input contains T - the number of test cases. It's followed by T lines, each containing 2 space-separated strings A and B.



Output Format

For each test case, print the test case number, followed by the interleavings of the 2 strings in a sorted order, separated by a new line.



Constraints

1 <= T <= 100

'a' <= A[i], B[i] <= 'z'

1 <= len(A), len(B) <= 10



Example

Input

2

nkb gl

bn zh



Output

Case #1:

glnkb

gnkbl

gnklb

gnlkb

ngkbl

ngklb

nglkb

nkbgl

nkgbl

nkglb

Case #2:

bnzh

bzhn

bznh

zbhn

zbnh

zhbn



Explanation



Self Explanatory


def interleaving(a,b,prefix,result):
    if not a and not b:
        result.append(prefix)
        return 
    if a:
        interleaving(a[1:],b,prefix+a[0],result)
    if b:
        interleaving(a,b[1:],prefix +b[0],result)
def print_inter(test_case,a,b):
    result=[]
    interleaving(a,b,"",result)
    result.sort()
    print(f"Case #{test_case}:")
    for interleave in result:
        print(interleave)
for test_case in range(1,int(input().strip())+1):
    a,b=input().strip().split()
    print_inter(test_case,a,b)
