#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>

#define MAX(x,y) ((x) > (y) ? (x) : (y))

int stack[1000000][2]; //NUM, NGE
int top;

void push(int item, int nge)
{
	stack[++top][0] = item;
	stack[top][1] = nge;
}
int pop()
{
	return stack[top--][1]; //NGE 반환
}
int peek() // NUM 확인
{
	return stack[top][0];
}

int main()
{
	int N;
	scanf("%d", &N);

	int* A = (int*)malloc(sizeof(int) * N);
	int* NGE = (int*)malloc(sizeof(int) * N);

	top = -1;
	
	for(int i = 0; i < N; i++)
	{
		scanf("%d", &A[i]);
		NGE[i] = -1;
	}

	int cnt = N - 1, nge;
	stack[++top][0] = A[N - 1];
	stack[top][1] = -1;

	while(cnt > 0){

		cnt--;

		if (A[cnt] < peek()) 
		{
			NGE[cnt] = stack[top][0];

			push(A[cnt], NGE[cnt]);
		}
		else {
			
			while (A[cnt] >= peek() && top != -1)
			{
				nge = pop();
			}

			if (top == -1)
				NGE[cnt] = -1;
			else
				NGE[cnt] = stack[top][0];

			push(A[cnt], NGE[cnt]);
		}
	}

	for (int i = 0; i < N; i++)
	{
		printf("%d ", NGE[i]);
	}
	printf("\n");

	free(A);
	free(NGE);

	return 0;
}