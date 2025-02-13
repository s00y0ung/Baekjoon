#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>

int visited[10] = { 0 };
int N, M;

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

void backTracking(stack* s, int start)
{
	if (s->top == M - 1)
	{
		for (int cnt = 0; cnt < M; cnt++)
		{
			printf("%d ", s->arr[cnt]);
		}
		printf("\n");
		return;
	}


	for (int i = start+1; i <= N; i++)
	{
		push(s, i);
		backTracking(s, i);
		pop(s);
	}
}

int main()
{
	scanf("%d %d", &N, &M);

	stack* s = (stack*)malloc(sizeof(stack));
	s->top = -1;

	backTracking(s,0);

	free(s);

	return 0;
}