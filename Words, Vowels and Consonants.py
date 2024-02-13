Words, Vowels and Consonants

Max Score: 50

Given a sentence containing only uppercase/lowercase english alphabets and spaces, you have to count the number of words, vowels and consonants.



Input Format

The first line of input contains T - number of test cases. It's followed by T lines, each line contains a single sentence.



Output Format

For each test case, print the number of words, vowels and consonants, separated by newline.



Constraints

1 <= T <= 1000

1 <= len(sentence) <= 104



Example

Input

4

Hi

Hello World

  Exception  

Hi there



Output

1 1 1

2 3 7

1 4 5

2 3 4



Explanation



Self Explanatory


for _ in range(int(input())):
    vowels="aeiou"
    a={'w':0,'v':0,'c':0}
    st=input().strip().split()
    a['w']=len(st)
    for word in st:
        for j in word:
            if j.lower() in vowels:
                a['v']+=1
            else:
                a['c']+=1
    print(a['w'],a['v'],a['c'])
