#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

void merge(int* list, int left, int mid, int right)
{
	int i = left;
	int j = mid + 1;
	int k = left;

	int sort[10];

	while (i <= mid && j <= right)
	{
		if (list[i] >= list[j])
			sort[k++] = list[i++];
		else
			sort[k++] = list[j++];
	}

	if (i > mid)
	{
		while (j <= right)
			sort[k++] = list[j++];
	}
	else
	{
		while (i <= mid)
			sort[k++] = list[i++];
	}

	for (int w = left; w <= right; w++)
		list[w] = sort[w];

}
void mergeSort(int* list, int left, int right)
{
	if (left < right)
	{
		int mid = (left + right) / 2;
		mergeSort(list, left, mid);
		mergeSort(list, mid + 1, right);
		merge(list, left, mid, right);
	}
}

int main()
{
	int N;
	scanf("%d", &N);

	int arr[10] = { 0 };
	int cnt = 0;
	while (N > 0)
	{
		arr[cnt++] = N % 10;
		N /= 10;
	}
	mergeSort(arr, 0, cnt - 1);

	for (int i = 0; i < cnt; i++)
		printf("%d", arr[i]);
	printf("\n");
	
	return 0;
}