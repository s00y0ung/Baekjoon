#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 5000000

int compare(const void *a, const void *b)
{
	if (*(long long*)a > *(long long*)b) return 1;
	if (*(long long*)a == *(long long*)b) return 0;
	return -1;
}

int main()
{
	int N, K;
	scanf("%d %d", &N, &K);

	long long arr[MAX_SIZE];
	for (int i = 0; i < N; i++)
		scanf("%lld", arr + i);

	qsort(arr, N, sizeof(long long), compare);

	printf("%lld\n", arr[K - 1]);

	return 0;
}