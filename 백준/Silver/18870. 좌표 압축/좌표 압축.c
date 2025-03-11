#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>

typedef struct {
	long long x;
	int cnt;
	int order;
}point;

int N;

void merge(point *p, int left, int mid, int right)
{
	int i = left;
	int j = mid + 1;
	int k = left;
	point* sort = (point*)malloc(sizeof(point) * N);

	while (i <= mid && j <= right)
	{
		if (p[i].x <= p[j].x)
		{
			sort[k].x = p[i].x;
			sort[k].cnt = p[i].cnt;
			sort[k++].order = p[i++].order;
		}
		else
		{
			sort[k].x = p[j].x;
			sort[k].cnt = p[j].cnt;
			sort[k++].order = p[j++].order;
		}
	}

	if (i > mid)
	{
		while (j <= right)
		{
			sort[k].x = p[j].x;
			sort[k].cnt = p[j].cnt;
			sort[k++].order = p[j++].order;
		}
	}
	else
	{
		while (i <= mid)
		{
			sort[k].x = p[i].x;
			sort[k].cnt = p[i].cnt;
			sort[k++].order = p[i++].order;
		}
	}

	for (int w = left; w <= right; w++)
	{
		p[w].x = sort[w].x;
		p[w].cnt = sort[w].cnt;
		p[w].order = sort[w].order;
	}

	free(sort);
}

void get_cnt(point* p, int cntArr[])
{
	int prev = 0;
	for (int i = 1; i < N; i++, prev++)
	{
		if (p[prev].x >= p[i].x)
		{
			p[i].cnt = p[prev].cnt;
		}
		else
		{
			p[i].cnt = p[prev].cnt + 1;
		}
	}

	for (int i = 0; i < N; i++)
		cntArr[p[i].order] = p[i].cnt;

	for (int i = 0; i < N; i++)
		printf("%d ", cntArr[i]);
}

void mergeSort(point* p, int left, int right)
{
	if (left < right)
	{
		int mid = (left + right) / 2;
		mergeSort(p, left, mid);
		mergeSort(p, mid + 1, right);
		merge(p, left, mid, right);
	}
}

int main()
{
	scanf("%d", &N);

	int* cntArr = (int*)malloc(sizeof(int) * N);
	point *p = (point *)malloc(sizeof(point) * N);
	for (int i = 0; i < N; i++)
	{
		cntArr[i] = 0;

		p[i].cnt = 0;
		p[i].order = i;
		scanf("%lld", &(p[i].x));
	}
	
	mergeSort(p, 0, N - 1);
	get_cnt(p, cntArr);

	free(cntArr);
	free(p);

	return 0;
}