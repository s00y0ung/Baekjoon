#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

#define SWAP(x,y,t) ((t) = (x), (x) = (y), (y) = (t))

int main()
{
	int numArr[5];
	int sum = 0;
	for (int i = 0; i < 5; i++)
	{
		scanf("%d", numArr + i);
		sum += numArr[i];
	}

	int num;
	int cnt;
	for (int i = 0; i < 4; i++)
	{
		num = numArr[i];
		cnt = i;
		for (int j = i + 1; j < 5; j++)
		{
			if (num > numArr[j]) {
				cnt = j;
				num = numArr[j];
			}
		}
		SWAP(numArr[i], numArr[cnt], num);
	}


	printf("%d\n", sum / 5);
	printf("%d\n", numArr[2]);

	return 0;
}