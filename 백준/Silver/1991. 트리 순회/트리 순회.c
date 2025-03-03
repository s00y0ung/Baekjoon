#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>

typedef struct TreeNode {
	char data;
	struct TreeNode* left, * right;
}TreeNode;

TreeNode *newNode()
{
	TreeNode* t = (TreeNode*)malloc(sizeof(TreeNode));
	t->left = NULL;
	t->right = NULL;

	return t;
}
void preorder(TreeNode *t)
{
	if (t != NULL) {
		printf("%c", t->data);
		preorder(t->left);
		preorder(t->right);
	}
}
void inorder(TreeNode* t)
{
	if (t != NULL) {
		inorder(t->left);
		printf("%c", t->data);
		inorder(t->right);
	}
}
void postorder(TreeNode* t)
{
	if (t != NULL) {
		postorder(t->left);
		postorder(t->right);
		printf("%c", t->data);
	}
}

int main()
{
	int N;
	scanf("%d", &N);
	
	TreeNode** tree = (TreeNode**)malloc(sizeof(TreeNode*) * 26);
	for (int i = 0; i < 26; i++)
		tree[i] = newNode();

	char Node, leftN, rightN;
	for (int i = 0; i < N; i++)
	{
		scanf(" %c %c %c", &Node, &leftN, &rightN);
		tree[Node-65]->data = Node;
		if (leftN != '.') {
			tree[Node - 65]->left = tree[leftN - 65];
		}
		if(rightN != '.') 
			tree[Node - 65]->right = tree[rightN - 65];
	}

	preorder(tree[0]);
	printf("\n");
	inorder(tree[0]);
	printf("\n");
	postorder(tree[0]);
	printf("\n");

	for (int i = 0; i < 26; i++)
		free(tree[i]);
	free(tree);

	return 0;
}