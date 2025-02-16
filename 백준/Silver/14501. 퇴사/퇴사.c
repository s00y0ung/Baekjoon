#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int N, maxPrice;
int* P, *T;
int visited[16] = { 0 };

typedef struct stack {
	int arr[20];
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
	if (start > N+1) return;
	if (s->top > -1)
	{
		int tmp = 0;
		for (int i = 0; i <= s->top; i++)
			tmp += P[s->arr[i]];
		if (tmp > maxPrice)
			maxPrice = tmp;
	}
	for (int i = start; i <= N; i++)
	{
		if (visited[i])
			continue;
		visited[i] = 1;
		push(s, i);
		
		backTracking(s, i + T[i]);
		
		pop(s);
		visited[i] = 0;
	}
}

int main()
{
	N;
	scanf("%d", &N);

	T = (int*)malloc(sizeof(int) * (N+1));
	P = (int*)malloc(sizeof(int) * (N+1));
	for (int i = 1; i <= N; i++)
		scanf("%d %d", &T[i], &P[i]);

	stack* s = (stack*)malloc(sizeof(stack));
	s->top = -1;

	maxPrice = 0;
	backTracking(s, 1);
	printf("%d\n", maxPrice);

	free(T);
	free(P);
	free(s);

	return 0;
}