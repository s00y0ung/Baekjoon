#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX(X,Y) ((X) > (Y) ? (X) : (Y))

int main()
{
	int N, K;
	scanf("%d %d", &N, &K);

	int** item = (int**)malloc(sizeof(int*) * (N+1));
	for (int i = 0; i <= N; i++)
		item[i] = (int*)malloc(sizeof(int) * 2);
	for (int i = 1; i <= N; i++)
	{
		scanf("%d %d", &item[i][0], &item[i][1]);
	}


	int value[100001][101];
	memset(value, 0, sizeof(value));

	for (int i = 1; i <= K; i++)
	{
		for (int j = 1; j <= N; j++)
		{
			if (item[j][0] > i) 
				value[i][j] = value[i][j-1];
			else {
				value[i][j] = MAX(value[i][j - 1], value[i - item[j][0]][j - 1] + item[j][1]);
			}
		}
	}
	printf("%d\n", value[K][N]);

	for (int i = 0; i < N; i++)
		free(item[i]);
	free(item);

	return 0;
}