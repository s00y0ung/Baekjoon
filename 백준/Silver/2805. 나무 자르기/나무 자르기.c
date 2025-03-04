#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>

long binarySearch(long* tree, long start, long end, long search, int N)
{
	while (start <= end)
	{
		long mid = (start + end) / 2;
		long height = 0;
		long tmp;

		for (int i = 0; i < N; i++){
			tmp = tree[i] - mid;
			if (tmp > 0)
			{
				height += tmp;
			}
		}
			

		if (height == search)
		{
			return mid;
		}
		else if (height > search)
			start = mid + 1;
		else if (height < search)
			end = mid - 1;
	}

	return end;
}


int main()
{
	int N, M;
	scanf("%d %d", &N, &M);

	long* tree = (long*)malloc(sizeof(long) * N);
	long maxNum = 0;
	for (int i = 0; i < N; i++)
	{
		scanf("%d", tree + i);
		if (maxNum < tree[i])
			maxNum = tree[i];
	}

	printf("%ld\n",binarySearch(tree, 0, maxNum, M, N));

	free(tree);

	return 0;
}