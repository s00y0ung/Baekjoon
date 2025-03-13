#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>

typedef struct Queue {
	int rear;
	int front;
	int *que;
}Queue;

int main()
{
	int N;
	scanf("%d", &N);

	Queue* q = (Queue*)malloc(sizeof(Queue));
	q->rear = N;
	q->front = 0;
	q->que = (int*)malloc(sizeof(int) * (N+1));
	for (int i = 1;i <= N; i++)
		q->que[i] = i;
	
	int value = 1; // N == 1인 경우
	while (q->rear % (N+1) != (q->front+1) % (N+1))
	{
		value = q->que[(++q->front) % (N+1)];
		
		value = q->que[(++q->front)%(N+1)];
		q->que[(++q->rear) % (N + 1)] = value;
	}
	printf("%d\n", value);

	free(q);

	return 0;
}