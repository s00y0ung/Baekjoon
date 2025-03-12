#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>

int compare(const void* a, const void* b)
{
	int num1 = *(long long*)a;
	int num2 = *(long long*)b;

	if (num1 > num2)
		return 1;
	return -1;;
}

int main()
{
	int N;
	scanf("%d", &N);

	long long arr[2000];
	for (int i = 0; i < N; i++)
		scanf("%lld" , arr + i);

	qsort(arr, N, sizeof(long long), compare);

	int s = 0;
	int e = 1;

	int goodNum = 0;
	for (int i = 0; i < N; i++)
	{
		s = 0;
		e = N-1;

		if (i == 0)
			s = 1;
		if (i == N - 1)
			e = N - 2;

		while (s < e)
		{
			if (arr[s]+arr[e] == arr[i])
			{
				goodNum += 1;
				break;
			}
			
			if (arr[s] + arr[e] < arr[i])
			{
				s++;
				if (s == i)
					s++;
			}
			else
			{
				e--;
				if (e == i)
					e--;
			}

		}
	}
	printf("%d\n", goodNum);
	
	return 0;
}