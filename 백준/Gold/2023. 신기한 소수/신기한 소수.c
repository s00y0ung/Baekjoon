#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <math.h>

int stack[10];
int top = -1;

void push(int item)
{
	stack[++top] = item;
}
int pop()
{
	return stack[top--];
}

int is_prime(int prime)
{
	if (prime <= 1)
		return -1;
	for (int i = 2; i < prime; i++)
	{
		if (prime % i == 0)
			return -1;
	}
	return 1;
}

void backTracking(int prime, int N, int size)
{
	if (top >= N-1)
	{
		for (int i = 0; i < N; i++)
			printf("%d", stack[i]);
		printf("\n");
		return;
	}
	for (int i = 1; i < 10; i++)
	{
		int cur = i;
		for (int s = top, e = 0; s >= 0; s--, e++)
		{
			cur += (stack[e] * pow(10, s+1));
		}

		if (is_prime(cur) == 1)
			push(i);
		else
			continue;

		backTracking(i, N, size);
		pop();
	}
}

int main()
{
	int N;
	scanf("%d", &N);

	backTracking(2, N, pow(10, N));

	return 0;
}