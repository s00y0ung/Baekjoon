#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>

int N, M;
int tmp[10] = { 0 };

typedef struct stack {
	int arr[10];
	int top;
}stack;

void push(stack* s, int n)
{
	s->arr[++(s->top)] = n;
}
int pop(stack* s)
{
	return s->arr[(s->top)--];
}

int merge(int* list, int left, int mid, int right)
{
	int i = left;
	int j = mid+1;
	int k = left;

	while (i <= mid && j <= right)
	{
		if (list[i] <= list[j])
			tmp[k++] = list[i++];
		else
			tmp[k++] = list[j++];
	}

	if (i > mid)
	{
		while (j <= right)
			tmp[k++] = list[j++];
	}
	else
	{
		while (i <= mid)
			tmp[k++] = list[i++];
	}

	for (int cnt = left; cnt <= right; cnt++)
		list[cnt] = tmp[cnt];
}
void mergeSort(int* list, int left, int right)
{
	if (left >= right)
		return;

	int mid = (left + right) / 2;
	mergeSort(list, left, mid);
	mergeSort(list, mid + 1, right);
	merge(list, left, mid, right);
}

void backTracking(stack* s, int numArr[])
{
	if (s->top == M - 1)
	{
		for (int i = 0; i < M; i++)
			printf("%d ", s->arr[i]);
		printf("\n");
		return;
	}

	for (int i = 0; i < N; i++)
	{
		push(s, numArr[i]);
		backTracking(s, numArr);
		pop(s);
	}
}

int main()
{
	scanf("%d %d", &N, &M);

	int* numArr = (int*)malloc(sizeof(int) * N);
	for (int i = 0; i < N; i++)
		scanf("%d", numArr + i);

	mergeSort(numArr, 0, N - 1);

	stack* s = (stack*)malloc(sizeof(stack));
	s->top = -1;

	backTracking(s, numArr);

	free(numArr);
	free(s);

	return 0;
}