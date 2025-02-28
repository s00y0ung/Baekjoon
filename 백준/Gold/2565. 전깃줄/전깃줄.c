#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

#define MAX(x,y) ((x) > (y) ? (x) : (y))

int main()
{
	int Btmp[501] = { 0 };
	int B[101] = { 0 };
	int dp[101];
	for (int i = 0; i < 101; i++)
		dp[i] = 1;

	int N, a,b;
	scanf("%d", &N);

	for (int i = 0; i < N; i++) {
		scanf("%d %d", &a, &b);
		Btmp[b] = a;
	}
	int t = 0;
	for (int i = 0; i < N; i++)
	{
		while (Btmp[t] == 0)
			t++;
		B[i] = Btmp[t++];
	}

	int tmp;
	int leng = -1;
	for (int i = N - 1; i >= 0; i--)
	{
		tmp = B[i];
		for (int j = i+1; j < N; j++)
		{
			if (tmp < B[j])
			{
				dp[i] = MAX(dp[i], dp[j] + 1);
			}
		}
	}

	for (int i = 0; i < N; i++)
	{
		if (leng < dp[i])
			leng = dp[i];
	}

	printf("%d\n", N - leng);

	return 0;
}