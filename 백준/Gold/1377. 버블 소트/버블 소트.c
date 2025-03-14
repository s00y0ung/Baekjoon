#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 500001

typedef struct Point {
	int num;
	int idx;
}Point;

int compare(const void* a, const void* b)
{
	return ((Point*)a)->num - ((Point*)b)->num;
}

int main()
{
	int N;
	scanf("%d", &N);

	Point* p = (Point *)malloc(sizeof(Point) * N);

	int tmp;
	for (int i = 0; i < N; i++)
	{
		scanf("%d", &tmp);
		p[i].num = tmp;
		p[i].idx = i;
	}

	int maxTurn = 0;
	qsort(p, N, sizeof(Point), compare);

	for (int i = 0; i < N; i++)
	{
		if (maxTurn < p[i].idx - i)
			maxTurn = p[i].idx - i;
	}
	printf("%d\n", maxTurn+1);


	free(p);

	return 0;
}