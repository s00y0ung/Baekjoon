#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

#define MAX_POINT 200005

int point[MAX_POINT][2];

void merge(int left, int mid, int right, int s, int e)
{
	int i = left;
	int j = mid + 1;
	int k = left;

	int sort[MAX_POINT][2];

	while (i <= mid && j <= right)
	{
		if (point[i][s] <= point[j][s])
		{
			sort[k][s] = point[i][s];
			sort[k++][e] = point[i++][e];
		}
		else
		{
			sort[k][s] = point[j][s];
			sort[k++][e] = point[j++][e];
		}
	}

	if (i > mid)
	{
		while (j <= right)
		{
			sort[k][s] = point[j][s];
			sort[k++][e] = point[j++][e];
		}
	}
	else
	{
		while (i <= mid)
		{
			sort[k][s] = point[i][s];
			sort[k++][e] = point[i++][e];
		}
	}

	for (int w = left; w <= right; w++)
	{
		point[w][s] = sort[w][s];
		point[w][e] = sort[w][e];
	}
}
void mergeSort(int left, int right, int s, int e)
{
	int mid;
	if (left < right)
	{
		mid = (left + right) / 2;
		mergeSort(left, mid,s,e);
		mergeSort(mid + 1, right,s,e);
		merge(left, mid, right,s,e);
	}
}

int main()
{
	int N;
	scanf("%d", &N);

	for (int i = 0; i < N; i++)
		scanf("%d %d", &point[i][0], &point[i][1]);

	mergeSort(0, N - 1, 0, 1);
	mergeSort(0, N - 1, 1, 0);

	for (int i = 0; i < N; i++)
	{
		printf("%d %d\n", point[i][0], point[i][1]);
	}

	return 0;
}