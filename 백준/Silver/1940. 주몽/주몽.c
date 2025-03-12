#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

int main()
{
	int N, M;
	scanf("%d %d", &N, &M);

	int num[15000];
	for (int i = 0; i < N; i++)
	{
		scanf("%d", num + i);
	}

	int cnt = 0;
	for (int i = 0; i < N-1; i++)
	{
		for (int j = i + 1; j < N; j++)
		{
			if (num[i] + num[j] == M)
			{
				cnt += 1;
				break;
			}
		}
	}

	printf("%d", cnt);

	return 0;
}