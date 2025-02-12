#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>


int set_find(int *parent, int curr)
{
	if (parent[curr] == -1)
		return curr;

	while (parent[curr] != -1)
		curr = parent[curr];
	
	return curr;
}
void set_union(int *parent , int a, int b)
{
	int root1 = set_find(parent,a);
	int root2 = set_find(parent,b);
	
	if (root1 != root2)
		parent[root1] = root2;
}

int main()
{
	int N, M;
	scanf("%d\n%d", &N,&M);

	int* n_list = (int*)malloc(sizeof(int) * (N+1));
	for (int i = 0; i <= N; i++)
		n_list[i] = -1;

	int start, end;
	for (int i = 0; i < M; i++)
	{
		scanf("%d %d", &start, &end);
		set_union(n_list, start, end);
	}

	int cnt = 0;
	int curr = set_find(n_list, 1);
	int tmp;
	for (int i = 2; i <= N; i++)
	{
		tmp = set_find(n_list, i);
		if (tmp == curr)
			cnt += 1;
	}
	printf("%d\n", cnt);

	free(n_list);

	return 0;
}