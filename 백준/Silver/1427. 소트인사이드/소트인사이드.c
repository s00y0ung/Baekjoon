#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

#define SWAP(x,y,t) ((t)=(x), (x)=(y), (y)=(t))
#define MAX_SIZE 10

void insertionSort(int *arr, int N)
{
	int minPos = 0;
	int tmp;
	for (int i = 0; i < N-1; i++)
	{
		minPos = i;
		for (int j = i+1; j < N; j++)
		{
			if (arr[minPos] < arr[j])
				minPos = j;
		}
		SWAP(arr[i], arr[minPos], tmp);
	}
}

int main()
{
	int N;
	scanf("%d", &N);

	int arr[MAX_SIZE];
	int size = 0;
	for (size = 0; size < 10; size++)
	{
		arr[size] = N % 10;

		N = N / 10;
		if (N == 0)
			break;
	}

	insertionSort(arr, size+1);
	for (int i = 0; i <= size; i++)
		printf("%d", arr[i]);
	printf("\n");

	return 0;
}