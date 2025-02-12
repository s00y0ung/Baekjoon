#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
	int N, M, tmp;
	scanf("%d %d", &N, &M);

	int* prefix_sum = (int*)malloc(sizeof(int) * (N + 1));
	memset(prefix_sum, 0, sizeof(int) * (N + 1));

	for (int i = 1; i <= N; i++) {
		scanf("%d", &tmp);
		prefix_sum[i] = prefix_sum[i - 1] + tmp;
	}

	int start, end;
	for (int i = 0; i < M; i++)
	{
		scanf("%d %d", &start, &end);
		printf("%d\n", prefix_sum[end] - prefix_sum[start - 1]);
	}

    free(prefix_sum);

	return 0;
}