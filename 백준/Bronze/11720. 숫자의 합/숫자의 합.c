#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

int main()
{
	int N;
	scanf("%d", & N);

	int t;
	int sum = 0;
	for (int i = 0; i < N; i++)
	{
		scanf("%1d", &t);
		sum += t;
	}
	printf("%d\n", sum);

	return 0;
}
