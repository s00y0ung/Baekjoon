#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

#define MAX_NUM 1000001

int main()
{
	int N, M;
	scanf("%d %d", &N, &M);

	long long tmp;
	long long prefix[MAX_NUM] = { 0 };
	long long cnt[1000] = { 0 };

	long long result = 0;

	for (int i = 1; i <= N; i++)
	{
		scanf("%lld", &tmp);
		prefix[i] = prefix[i - 1] + tmp;
		prefix[i] = prefix[i] % M;

		if (prefix[i] == 0)
			result += 1;

		cnt[prefix[i]] += 1;
	}
	
	for (int i = 0; i < M; i++)
	{
		if (cnt[i] > 1)
		{
			result += ((cnt[i] * (cnt[i] - 1)) / 2);   
		}
	}
	printf("%lld\n", result);

	return 0;
}