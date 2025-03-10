#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

#define MAX_SIZE 500

#define MAX(x,y) ((x) > (y) ? (x) : (y))

int map[MAX_SIZE][MAX_SIZE];
int path[MAX_SIZE][MAX_SIZE];
int N, M;

int find_path(int y, int x)
{

	if (y == N - 1 && x == M - 1)
		return 1;

	if (path[y][x] != -1)
		return path[y][x];
	
	int cnt = 0;

	if (y - 1 >= 0 && map[y][x] > map[y - 1][x])
		cnt += find_path(y - 1, x);
	if (y + 1 < N && map[y][x] > map[y + 1][x])
		cnt += find_path(y + 1, x);
	if (x - 1 >= 0 && map[y][x] > map[y][x - 1])
		cnt += find_path(y, x - 1);
	if (x + 1 < M && map[y][x] > map[y][x + 1])
		cnt += find_path(y, x + 1);
	
	path[y][x] = cnt;

	return path[y][x];
}

int main()
{
	scanf("%d %d", &N, &M);
	
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			scanf("%d", &map[i][j]);
			path[i][j] = -1;
		}
	}

	printf("%d\n",find_path(0, 0));
	

	return 0;
}