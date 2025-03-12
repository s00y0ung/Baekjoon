#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

int main()
{
	int N;
	scanf("%d", &N);
	
	int s = 0;
	int e = 1;

	int cnt = 0;
	int sum = 1;
	while (s <= N)
	{
		if (sum == N)
		{
			cnt += 1;
		}

		if (sum >= N)
		{
			s += 1;
			sum -= s;
		}
		else 
		{
			e += 1;
			sum += e;
		}
	}

	printf("%d\n", cnt);

	return 0;
}