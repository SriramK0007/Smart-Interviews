Print Right Angled Triangle Pattern

Max Score: 50

Print a mirror image of a right-angled triangle using '*'. See examples for more details.



Input Format

The First line of input contains T - the number of test cases. It's followed by T lines, each line contains a single integer N - the size of the pattern.



Output Format

For each test case, print the test case number as shown, followed by the pattern, separated by a new line.



Constraints

1 <= T <= 100

1 <= N <= 100



Example

Input

4
2
1
5
10


Output

Case #1:
 *
**
Case #2:
*
Case #3:
    *
   **
  ***
 ****
*****
Case #4:
         *
        **
       ***
      ****
     *****
    ******
   *******
  ********
 *********
**********


Explanation



Self Explanatory




  #include<stdio.h>
void rightTriangle(int n){
    for (int i=1;i<=n;i++){
        for (int j=1;j<n-i+1;j++){
            printf(" ");
        }
        for (int j=n-i+1;j<=n;j++) {
            printf("*");
        }
    printf("\n");
    }
}

int main(){
    int t;
    scanf("%d",&t);
    for (int i=1;i<=t;i++){
        printf("Case #%d:\n",i);
        int n;
        scanf("%d",&n);
        rightTriangle(n);
    }
    return 0;
}
