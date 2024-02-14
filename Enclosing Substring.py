Enclosing Substring

Max Score: 200

Given 2 strings A and B, find the smallest substring of B having all the characters of A, in any order.



Input Format

The first line of input contains T - the number of test cases. It's followed by T lines, each line containing 2 space-separated strings - A and B.



Output Format

For each test case, print the length of the smallest substring of B having all the characters of A, separated by newline. If no such substring is found, print -1.



Constraints

20 points

1 <= T <= 100

1 <= size(A), size(B) <= 100



60 points

1 <= T <= 100

1 <= size(A), size(B) <= 1000



120 points

1 <= T <= 100

1 <= size(A), size(B) <= 10000



General Constraints

'a' <= A[i], B[i] <= 'z'



Example

Input

4

fkqyu frqkzkruqmfqyuzlkyg

onmwvytbytn uqhmfjaqtgngcwkuzyamnerphfmw

bloets lwbcrsfothplxseplrtbshbtstjloxsf

dzpd dclzztpjldkndgbdqqzmbp



Output

7

-1

13

9



Explanation



Self Explanatory



from collections import Counter
def isMapset(A,B):
    for i in A:
        try:
            if A[i]>B[i]:
                return False
        except:
            return False
    return True
for _ in range(int(input())):
    a,b=input().split()
    A=dict(Counter(a))
    B=dict(Counter(b))
    if (isMapset(A,B)==False):
        print(-1)
        continue
    B=dict()
    i=0
    j=0
    ans=(1 << 31)-1
    while (i<len(b) and j< len(b)):
        while(not isMapset(A,B) and j< len(b)):
            try:
                B[b[j]]+=1
            except:
                B[b[j]]=1
            j+=1
        if j==len(b) and isMapset(A,B)==False:
            break
        ans=min(j-i,ans)
        while(isMapset(A,B) and i<len(b)-len(a)+1):
            B[b[i]]-=1
            if B[b[i]]==0:
                del B[b[i]]
            i+=1
        ans=min(ans,j-i+1)
    print(ans)
