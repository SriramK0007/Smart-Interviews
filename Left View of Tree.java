Left View of Tree

Max Score: 100

Given an array of unique elements, construct a Binary Search Tree and print the left-view of the tree. The left view of a tree is the set of nodes visible when the tree is viewed from the left side.



Input Format

The first line of input contains T - the number of test cases. It's followed by 2T lines. The first line of each test case contains N - the number of nodes in the BST. The next line contains N unique integers - value of the nodes.



Output Format

For each test case, print the left-view of the Binary Search Tree, separated by a newline.



Constraints

1 <= T <= 1000

1 <= N <= 1000

0 <= ar[i] <= 10000



Example

Input

3

5

1 2 3 4 5

5

3 2 4 1 5

7

4 5 15 0 1 7 17



Output

1 2 3 4 5

3 2 1

4 0 1 7



Explanation



Self Explanatory


  


import java.io.*;
import java.util.*;

public class Main {

public static void main(String[] args) {
Scanner sc = new Scanner(System.in);
int t = sc.nextInt();
while (t--> 0) {
int n = sc.nextInt();
Node root = null;
for(int i=0;i<n;i++){
root=insert(root,sc.nextInt());
}
ArrayList<Integer> list=new ArrayList<>();
list=leftView(root,0,list);
for(int i=0;i<list.size();i++){
System.out.print(list.get(i)+" ");
}
System.out.println();
}
}

public static ArrayList<Integer> leftView(Node root,int level,ArrayList<Integer> list){
if(root==null)return new ArrayList<>();
if(level==list.size()){
list.add(root.data);
}
leftView(root.left,level+1,list);
leftView(root.right,level+1,list);
return list;
}
public static Node insert(Node root, int data) {
if (root == null) {
root=new Node(data);
} else {
Node cur;
if (data <= root.data) {
root.left = insert(root.left, data);

} else {
root.right = insert(root.right, data);

}
}
return root;
}
static class Node {
Node left;
Node right;
int data;

Node(int data) {
this.data = data;
left = null;
right = null;
}
}
}
