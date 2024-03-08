Implement Stack

Max Score: 50

Implement the Stack data structure and perform push / pop operations.



Note:

Do not use any inbuilt functions / libraries for the Stack.



Input Format
The first line of input contains T - number of operations. It is followed by T lines, each line contains either "push x" or "pop".



Output Format

For each "pop" operation, print the popped element, separated by a newline. If the stack is empty, print "Empty".



Constraints

1 <= T <= 10000

-100 <= x <= 100



Example

Input

8

push 5

pop

pop

push 10

push -15

pop

push -10

pop



Output

5

Empty

-15

-10



Explanation



Self Explanatory




t = int(input())
st = []
for _ in range(t):
    cmd = input().split()
    if cmd[0] == "pop":
        if len(st) > 0:
            print(st.pop())
        else:
            print("Empty")
    elif cmd[0] == "push":
        st.append(cmd[1])
