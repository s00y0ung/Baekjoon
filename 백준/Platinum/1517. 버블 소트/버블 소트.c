#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 500001

long long arr[MAX_SIZE];
long long swap_cnt = 0;

void merge(int left, int mid, int right)
{
	int i = left;
	int j = mid+1;
	int k = left;

	int first_cnt = mid-left +1;
	long long sort[MAX_SIZE];

	while (i <= mid && j <= right)
	{
		if (arr[i] <= arr[j])
		{
			sort[k++] = arr[i++];
			first_cnt--;
		}
		else
		{
			sort[k++] = arr[j++];
			swap_cnt += first_cnt;
		}
	}

	if (i > mid)
	{
		while (j <= right)
			sort[k++] = arr[j++];
	}
	else
	{
		while (i <= mid)
			sort[k++] = arr[i++];
	}

	for (int w = left; w <= right; w++)
		arr[w] = sort[w];
}

void mergeSort(int left, int right)
{
	if (left < right)
	{
		int mid = (left + right) / 2;
		mergeSort(left, mid);
		mergeSort(mid + 1, right);
		merge(left, mid, right);
	}
}

int main()
{
	int N;
	scanf("%d", &N);
	
	for (int i = 0; i < N; i++)
		scanf("%lld", arr + i);

	mergeSort(0, N - 1);

	printf("%lld\n", swap_cnt);

	return 0;
}