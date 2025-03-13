#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>

typedef struct Deque{
	int rear;
	int front;
	long long deque[5000000][2];
}Deque;

void push(Deque *d, long long item, int idx, int L)
{
	if (d->front != d->rear && idx - d->deque[(d->front + 1)][0] >= L)
		d->deque[++d->front][1];

	while(d->front != d->rear && d->deque[d->rear][1] > item)
	{
		d->rear--;
	}
	d->deque[++d->rear][0] = idx;
	d->deque[d->rear][1] = item;
}

int main()
{
	int L, N;
	scanf("%d %d", &N ,&L);

	long long* arr = (long long*)malloc(sizeof(long long) * (N+1));
	for (int i = 0; i < N; i++)
		scanf("%lld", &arr[i]);

	Deque d;
	d.rear = -1;
	d.front = -1;

	int idx = 0;
	while (idx < N)
	{
		push(&d, arr[idx], idx, L);
		printf("%lld ", d.deque[(d.front+1)][1]);

		idx++;
	}
	printf("\n");

	free(arr);

	return 0;
}