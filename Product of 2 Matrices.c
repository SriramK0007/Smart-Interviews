Product of 2 Matrices

Max Score: 50

Given 2 matrices, find their product.



Input Format

The first line of input contains T - the number of test cases. The first line of each test case contains N1, M1 - the size of the 1st matrix. It is followed by N1 lines each containing M1 integers - elements of the 1st matrix. The next line contains N2, M2 - the size of the 2nd matrix. It is followed by N2 lines each containing M2 integers - elements of the 2nd matrix. Note that M1 = N2.



Output Format

For each test case, print the resultant product matrix, separated by a new line.



Constraints

1 <= T <= 100

1 <= N1,M1,N2,M2 <= 50

-100 <= mat[i][j] <= 100



Example

Input

2

2 2

1 2

3 -1

2 3

1 -2 3

2 3 -1

2 3

27 29 53

-28 49 -24

3 4

23 52 -38 72

-64 15 -59 -10

-75 43 10 25



Output

5 4 1

1 -9 10

-5210 4118 -2207 2979

-1980 -1753 -2067 -3106



Explanation



Self Explanatory


#include <stdio.h>
#include <stdlib.h>
int main() {
    int t;
    scanf("%d",&t);
    for (int p=0;p<t;p++){
        int n1,m1,n2,m2;
        scanf("%d%d",&n1,&m1); 
        int mat1[n1][m1];
        for (int i=0;i<n1;i++){
            for (int j=0;j<m1;j++){
                scanf("%d",&mat1[i][j]);
            }
        }
        scanf("%d%d",&n2,&m2); 
        int mat2[n2][m2];
        for (int i=0;i<n2;i++){
            for (int j=0;j<m2;j++){
                scanf("%d",&mat2[i][j]);
            }
        }
        int c[n1][m2];
        for (int i=0;i<n1;i++){
            for (int j=0;j<m2;j++){
                c[i][j]=0;
                for (int k=0;k<n2;k++){
                    c[i][j] += mat1[i][k] * mat2[k][j];
                }
                printf("%d ",c[i][j]);
            }
            printf("\n");
        }
    }               
    return 0;
}
