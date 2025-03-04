#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

void merge(int* score, int left, int mid, int right)
{
	int i = left;
	int j = mid + 1;
	int k = left;
	int sort[1000];

	while (i <= mid && j <= right)
	{
		if (score[i] >= score[j])
			sort[k++] = score[i++];
		else
			sort[k++] = score[j++];
	}
	
	if (i > mid)
	{
		while (j <= right)
			sort[k++] = score[j++];
	}
	else
	{
		while (i <= mid)
			sort[k++] = score[i++];
	}

	for (int w = left; w <= right; w++)
		score[w] = sort[w];
}
void mergeSort(int* score, int left, int right)
{
	if (left < right)
	{
		int mid = (left + right) / 2;
		mergeSort(score, left, mid);
		mergeSort(score, mid + 1, right);
		merge(score, left, mid, right);
	}
}

int main()
{
	int N, K;
	scanf("%d %d", &N, &K);

	int score[1000];
	for (int i = 0; i < N; i++)
		scanf("%d", score + i);

	mergeSort(score, 0, N - 1);
	
	printf("%d", score[K - 1]);

	return 0;
}