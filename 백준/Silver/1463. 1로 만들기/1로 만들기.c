#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
	int N;
	scanf("%d", &N);
	
	int* s_list = (int*)malloc(sizeof(int) * (N+1));
	memset(s_list, 0, sizeof(int) * (N + 1));
	s_list[2] = 1;
	s_list[3] = 1;
	
	int tmp1, tmp2, tmp3;
	int min_value;

	for (int i = 4; i <= N; i++)
	{	
		if (i % 3 == 0) {
			tmp1 = 1 + s_list[i / 3];
		}
		else {
			tmp1 = i;
		}

		if (i % 2 == 0) {
			tmp2 = 1 + s_list[i / 2];
		}
		else {
			tmp2 = i;
		}

		tmp3 = 1 + s_list[i - 1];

		//min value
		min_value = tmp1 > tmp2 ? tmp2 : tmp1;
		min_value = min_value > tmp3 ? tmp3 : min_value;
		s_list[i] = min_value;
	}
	printf("%d\n", s_list[N]);
	return 0;
}