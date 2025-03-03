#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

int card[500000] = { 0 };
int check[500000] = { 0 };
int tmp[500000] = { 0 };

void merge(int left, int mid, int right)
{
	int i = left;
	int j = mid+1;
	int k = left;

	while (i <= mid && j <= right)
	{
		if (card[i] <= card[j])
			tmp[k++] = card[i++];
		else
			tmp[k++] = card[j++];
	}

	if (j>right)
	{
		while (i <= mid)
			tmp[k++] = card[i++];
	}
	else
	{
		while (j <= right)
			tmp[k++] = card[j++];
	}

	for (int z = left; z <= right; z++)
	{
		card[z] = tmp[z];
	}
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

int binarySearch(int search, int end)
{
	int left = 0;
	int right = end;
	int n;
	while (left <= right)
	{
		n = (left + right) / 2;
		
		if (card[n] == search)
			return 1;
		if (card[n] < search)
			left = n + 1;
		else if (card[n] > search)
			right = n - 1;
	}
	return 0;
}
int main()
{
	int N;
	scanf("%d", &N);
	for (int i = 0; i < N; i++)
	{
		scanf("%d", card + i);
	}

	int M;
	scanf("%d", &M);
	for (int i = 0; i < M; i++)
	{
		scanf("%d", check + i);
	}
	// card 배열을 정렬
	mergeSort(0, N-1);
	
	// check 배열 원소에 대해 card 배열 이분탐색
	for (int i = 0; i < M; i++)
		printf("%d ",binarySearch(check[i], N-1));
	printf("\n");
	

	return 0;
}