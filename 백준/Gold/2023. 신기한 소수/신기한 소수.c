#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <math.h>

int N;
int is_prime(int prime)
{
	if (prime <= 1)
		return -1;
	for (int i = 2; i*i <= prime; i++)
	{
		if (prime % i == 0)
			return -1;
	}
	return 1;
}

void backTracking(int num, int size)
{
	if (size >= N)
	{
		printf("%d\n", num);
		return;
	}

	for (int i = 1; i < 10; i++)
	{
		int n = num * 10 + i;
		if (is_prime(n) == 1)
			backTracking(n, size + 1);
	}
}

int main()
{
	scanf("%d", &N);

	backTracking(0, 0);

	return 0;
}