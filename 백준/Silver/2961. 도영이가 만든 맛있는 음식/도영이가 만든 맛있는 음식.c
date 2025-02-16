#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX(x,y) ((x) > (y) ? (x) : (y))
#define MIN(x,y) ((x) < (y) ? (x) : (y))

int N;
int *visited;
unsigned long long minNum;

void backTracking(int start, int** taste)
{
	if (start != 0) {
		int tmpS = 1;
		int tmpB = 0;
		for (int i = 0; i < N; i++)
		{
			if (visited[i] == 1) {
				tmpS *= taste[i][0];
				tmpB += taste[i][1];
			}
		}
		if (minNum > (MAX(tmpS, tmpB) - MIN(tmpS, tmpB)))
			minNum = MAX(tmpS, tmpB) - MIN(tmpS, tmpB);
	}

	for (int i = start; i < N; i++)
	{
		if (visited[i] == 1)
			continue;
		visited[i] = 1;

		backTracking(i+1,taste);
		visited[i] = 0;
	}
}

int main()
{
	scanf("%d", &N);

	int** taste = (int**)malloc(sizeof(int*) * N);
	for (int i = 0; i < N; i++) {
		taste[i] = (int*)malloc(sizeof(int) * 2);
		scanf("%d %d", &taste[i][0], &taste[i][1]);
	}

	visited = (int*)malloc(sizeof(int) * N);
	memset(visited, 0, sizeof(int) * N);
	minNum = MAX(taste[0][0], taste[0][1]) - MIN(taste[0][0], taste[0][1]);

	backTracking(0, taste);
	printf("%d\n", minNum);

	for (int i = 0; i < N; i++)
		free(taste[i]);
	free(taste);
	free(visited);

	return 0;
}