#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int N;
int mp, mf, ms, mv;
int minCost;
int *visited;
int* nuNo;
int** nutrition;

typedef struct stack {
	int arr[16];
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
	if (s->top > -1)
	{
		int sumP = 0, sumF = 0, sumS = 0, sumV = 0, sumC = 0;
		for (int i = 0; i <= s->top; i++)
		{
			sumP += nutrition[s->arr[i]][0];
			sumF += nutrition[s->arr[i]][1];
			sumS += nutrition[s->arr[i]][2];
			sumV += nutrition[s->arr[i]][3];
			sumC += nutrition[s->arr[i]][4];
		}
		if (sumP >= mp && sumF >= mf && sumS >= ms && sumV >= mv)
		{
			if (sumC < minCost)
			{
				minCost = sumC;
				for (int i = 0; i < N; i++)
					nuNo[i] = -1;
				for (int i = 0; i <= s->top; i++)
					nuNo[i] = (s->arr[i]+1);
			}
		}
	}
	for (int i = start; i < N; i++)
	{
		if (visited[i] == 1)
			continue;
		visited[i] = 1;

		push(s, i);
		backTracking(s, i + 1);
		pop(s);

		visited[i] = 0;
	}
}

int main()
{
	scanf("%d", &N);
	scanf("%d %d %d %d", &mp, &mf, &ms, &mv);

	nutrition = (int**)malloc(sizeof(int*) * N);
	for (int i = 0; i < N; i++)
	{
		nutrition[i] = (int*)malloc(sizeof(int) * 5);
		scanf("%d %d %d %d %d", &nutrition[i][0], &nutrition[i][1], &nutrition[i][2], &nutrition[i][3], &nutrition[i][4]);
	}
	visited = (int*)malloc(sizeof(int) * N);
	memset(visited, 0, sizeof(int) * N);
	
	nuNo = (int*)malloc(sizeof(int) * N);
	memset(nuNo, -1, sizeof(int) * N);
	minCost = 10000;

	stack* s = (stack*)malloc(sizeof(stack));
	s->top = -1;

	backTracking(s, 0);
	if (nuNo[0] == -1)
		printf("-1\n");
	else
	{
		printf("%d\n", minCost);
		for (int i = 0; i < N; i++)
		{
			if (nuNo[i] == -1)
				break;
			printf("%d ", nuNo[i]);
		}
		printf("\n");
	}
	

	for (int i = 0;i < N; i++)
		free(nutrition[i]);
	free(nutrition);
	free(visited);
	free(s);

	return 0;
}