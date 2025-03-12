#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <string.h>

#define MAX_N 1025

int main()
{
	int N, M;
	scanf("%d %d", &N, &M);

	int table[MAX_N][MAX_N];
	int sum[MAX_N][MAX_N];
	memset(sum, 0, sizeof(int) * (MAX_N) * (MAX_N));
	
	for (int i = 1; i <= N; i++)
	{
		for (int j = 1; j <= N; j++)
		{
			scanf("%d", &table[i-1][j-1]);

			sum[i][j] = sum[i - 1][j] + sum[i][j - 1] - sum[i - 1][j - 1] + table[i-1][j-1];
		}
	}

	int x1,x2,y1,y2;
	for (int i = 0; i < M; i++)
	{
		scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
		printf("%d\n", sum[x2][y2] - sum[x2][y1-1] - sum[x1-1][y2] + sum[x1-1][y1-1]);
	}

	return 0;
}