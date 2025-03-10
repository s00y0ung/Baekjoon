#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>

#define MAX_TREE 500
#define MAX(x,y) ((x) > (y) ? (x) : (y))

int tree[MAX_TREE][MAX_TREE];
int path[MAX_TREE][MAX_TREE];

int N;

int find_path(int y, int x)
{
	if (path[y][x] != 0)
		return path[y][x];

	int point = 0;
	if (N > y + 1 && tree[y+1][x] > tree[y][x])
		path[y][x] = MAX(path[y][x], find_path(y + 1, x) + 1);
	
	if (0 <= y - 1 && tree[y-1][x] > tree[y][x])
		path[y][x] = MAX(path[y][x], find_path(y - 1, x) + 1);
	
	if (N > x + 1 && tree[y][x+1] > tree[y][x])
		path[y][x] = MAX(path[y][x], find_path(y, x + 1) + 1);

	if (0 <= x - 1 && tree[y][x-1] > tree[y][x])
		path[y][x] = MAX(path[y][x], find_path(y, x - 1) + 1);


	return path[y][x];
}

int main()
{
	scanf("%d", &N);

	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			scanf("%d", &tree[i][j]);
			path[i][j] = 0;
		}
	}

	for (int y = 0; y < N; y++)
	{
		for (int x = 0; x < N; x++)
			find_path(y, x);
	}

	int max_num = 0;
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			if (max_num < path[i][j])
				max_num = path[i][j];
		}
	}
	printf("%d\n", ++max_num);

	return 0;
}