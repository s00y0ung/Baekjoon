#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Join {
	int age;
	char name[101];
}Join;


void merge(Join* arr, int left, int mid, int right)
{
	int i = left;
	int j = mid+1;
	int k = left;

	Join tmp[100000];

	while (i <= mid && j <= right)
	{
		if (arr[i].age <= arr[j].age)
		{
			tmp[k++] = arr[i++];
		}
		else
		{
			tmp[k++] = arr[j++];
		}
	}

	if (i > mid)
	{
		while (j <= right)
		{
			tmp[k++] = arr[j++];
		}
	}
	else
	{
		while (i <= mid)
		{
			tmp[k++] = arr[i++];
		}
	}

	for (int w = left; w <= right; w++)
	{
		arr[w] = tmp[w];
	}
}
void mergeSort(Join * arr, int left, int right)
{
	if (left < right)
	{
		int mid = (left + right) / 2;
		mergeSort(arr, left, mid);
		mergeSort(arr, mid + 1, right);
		merge(arr, left, mid, right);
	}
}

int main()
{
	int N;
	scanf("%d", &N);

	Join* j = (Join*)malloc(sizeof(Join) * N);

	for (int i = 0; i < N; i++)
		scanf("%d %s", &j[i].age, j[i].name);

	mergeSort(j, 0, N - 1);

	for (int i = 0; i < N; i++)
		printf("%d %s\n", j[i].age, j[i].name);


	free(j);

	return 0;
}