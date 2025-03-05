#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

void merge(int* sort, int* change, int left, int mid, int right)
{
	int tmpSort[100000];
	int tmpChange[100000];

	int i = left;
	int j = mid + 1;
	int k = left;

	while (i <= mid && j <= right)
	{
		if (sort[i] <= sort[j])
		{
			tmpSort[k] = sort[i];
			tmpChange[k++] = change[i++];
		}
		else
		{
			tmpSort[k] = sort[j];
			tmpChange[k++] = change[j++];
		}
	}

	if (i > mid)
	{
		while (j <= right)
		{
			tmpSort[k] = sort[j];
			tmpChange[k++] = change[j++];
		}
	}
	else
	{
		while (i <= mid)
		{
			tmpSort[k] = sort[i];
			tmpChange[k++] = change[i++];
		}
	}

	for (int z = left; z <= right; z++)
	{
		sort[z] = tmpSort[z];
		change[z] = tmpChange[z];
	}

}
void mergeSort(int* sort, int* change, int left, int right)
{
	if (left < right)
	{
		int mid = (left + right) / 2;
		mergeSort(sort, change, left, mid);
		mergeSort(sort, change, mid + 1, right);
 
		merge(sort, change, left, mid, right);
	}
}

int main()
{
	int N;
	scanf("%d", &N);

	int x[100000] = { 0 };
	int y[100000] = { 0 };

	for (int i = 0; i < N; i++)
		scanf("%d %d", x + i, y + i);

	mergeSort(y, x, 0, N - 1);
	mergeSort(x, y, 0, N - 1);

	for (int i = 0; i < N; i++)
		printf("%d %d\n",x[i], y[i]);


	return 0;
}
