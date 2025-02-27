#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

#define MIN(X,Y) ((X)>(Y)?(Y):(X))

int main()
{
	int r, g, b;
	int rgb[1001][3] = { 0 };

	int N;
	scanf("%d", &N);

	for (int i = 1; i <= N; i++)
	{
		scanf("%d %d %d", &r, &g, &b);

		rgb[i][0] = MIN(rgb[i - 1][1], rgb[i - 1][2]) + r;
		rgb[i][1] = MIN(rgb[i - 1][0], rgb[i - 1][2]) + g;
		rgb[i][2] = MIN(rgb[i - 1][0], rgb[i - 1][1]) + b;
	}

	int minCost = rgb[N][0];
	if (rgb[N][1] < minCost)
		minCost = rgb[N][1];
	if (rgb[N][2] < minCost)
		minCost = rgb[N][2]; 

	printf("%d\n", minCost);

	return 0;
}