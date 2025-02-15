#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

int main()
{
	int N, tmp;
	scanf("%d", &N);
	
	int numArr[10001] = { 0 };
	for (int i = 0; i < N; i++)
	{
		scanf("%d", &tmp);
		numArr[tmp] += 1;
	}

	int cnt;
	for (int i = 1; i <= 10000; i++)
	{
		cnt = numArr[i];
		for (int j = 0; j < cnt; j++)
			printf("%d\n", i);
	}
    
	return 0;
}