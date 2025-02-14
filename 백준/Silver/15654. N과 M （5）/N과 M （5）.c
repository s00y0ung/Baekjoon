#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define SWAP(x,y,tmp) ((tmp)=(x),(x)=(y),(y)=(tmp))

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

void backTracking(stack* s, int numArr[], int visited[])
{
	if (s->top == M - 1)
	{
		for (int i = 0; i < M; i++)
			printf("%d ", s->arr[i]);
		printf("\n");
	}

	for(int i = 0; i < N; i++)
	{
		if (visited[i])
			continue;
		visited[i] = 1;

		push(s, numArr[i]);
		backTracking(s, numArr, visited);
		pop(s);

		visited[i] = 0;
	}
}

int main()
{
	scanf("%d %d", &N, &M);
	
	int* numArr = (int*)malloc(sizeof(int) * N);
	for (int i = 0; i < N; i++)
		scanf("%d", numArr + i);
	
	//정렬
	int minNum;
	int minIdx = 0;
	int i, j, tmp;
	for (i = 0; i < N-1; i++)
	{
		minNum = 10001;
		for (j = i; j < N; j++)
		{
			if (minNum > numArr[j]) {
				minNum = numArr[j];
				minIdx = j;
			}
		}
		SWAP(numArr[i], numArr[minIdx], tmp);
	}


	int* visited = (int*)malloc(sizeof(int) * N);
	memset(visited, 0, sizeof(int) * N);

	stack* s = (stack*)malloc(sizeof(stack));
	s->top = -1;

	backTracking(s, numArr, visited);

	free(s);
	free(numArr);
	free(visited);
	return 0;
}