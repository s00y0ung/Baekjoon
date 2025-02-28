#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

int main()
{
	int N;
	scanf("%d", &N);

	int arr[2000001] = { 0 };
	int tmp;
	for (int i = 0; i < N; i++)
	{
		scanf("%d", &tmp);
		arr[tmp] += 1;
	}
	int X;
	scanf("%d", &X);

	int cnt = 0;

	for (int i = 1; i <= X/2; i++)
	{
		if (i == X - i)
			cnt += (arr[i] / 2);
		if (i >= X - i)
			break;
		else
			cnt += arr[i] * arr[X - i];
	} 
	printf("%d\n", cnt);

	return 0;
}