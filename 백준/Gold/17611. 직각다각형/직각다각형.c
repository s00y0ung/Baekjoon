#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_SIZE 1000001

#define MAX(x,y) ((x) > (y) ? (x) : (y))
#define MIN(x,y) ((x) < (y) ? (x) : (y))

int main()
{
	int N;
	scanf("%d", &N);

	//memory allocation
	int* x_high = (int*)malloc(sizeof(int) * MAX_SIZE);
	int* x_low = (int*)malloc(sizeof(int) * MAX_SIZE);
	int* y_high = (int*)malloc(sizeof(int) * MAX_SIZE);
	int* y_low = (int*)malloc(sizeof(int) * MAX_SIZE);
	int* prefix_sum_x_high = (int*)malloc(sizeof(int) * MAX_SIZE);
	int* prefix_sum_x_low = (int*)malloc(sizeof(int) * MAX_SIZE);
	int* prefix_sum_y_high = (int*)malloc(sizeof(int) * MAX_SIZE);
	int* prefix_sum_y_low = (int*)malloc(sizeof(int) * MAX_SIZE);

	memset(x_high, 0, sizeof(int) * MAX_SIZE);
	memset(x_low, 0, sizeof(int) * MAX_SIZE);
	memset(y_high, 0, sizeof(int) * MAX_SIZE);
	memset(y_low, 0, sizeof(int) * MAX_SIZE);
	memset(prefix_sum_x_high, 0, sizeof(int) * MAX_SIZE);
	memset(prefix_sum_x_low, 0, sizeof(int) * MAX_SIZE);
	memset(prefix_sum_y_high, 0, sizeof(int) * MAX_SIZE);
	memset(prefix_sum_y_low, 0, sizeof(int) * MAX_SIZE);

	int x, y, prex, prey;
	int x_max = -500000;
	int y_max = -500000;
	int x_min = 500000;
	int y_min = 500000;

	scanf("%d %d", &prex, &prey);
	prex += 500000;
	prey += 500000;

	int tmpx = prex;
	int tmpy = prey;

	for (int i = 0; i < N; i++)
	{
		if (i != N - 1) {
			scanf("%d %d", &x, &y);
			x += 500000;
			y += 500000;
		}
		else {
			x = tmpx;
			y = tmpy;
		}

		//max, min number
		if (x_max < x) x_max = x;
		if (x_min > x) x_min = x;
		if (y_max < y) y_max = y;
		if (y_min > y) y_min = y;

		if (prey == y) {
			x_high[MAX(prex, x)] += 1;
			x_low[MIN(prex, x)] += 1;
		}
		else {
			y_high[MAX(prey, y)] += 1;
			y_low[MIN(prey, y)] += 1;
		}
		prex = x;
		prey = y;
	}
	
	prefix_sum_x_high[x_max] = x_high[x_max];
	prefix_sum_x_low[x_max] = x_low[x_max];
	for (int i = x_max - 1; i >= x_min; i--)
	{
		prefix_sum_x_high[i] = prefix_sum_x_high[i + 1] + x_high[i];
		prefix_sum_x_low[i] = prefix_sum_x_low[i + 1] + x_low[i];
	}

	prefix_sum_y_high[y_max] = y_high[y_max];
	prefix_sum_y_low[y_max] = y_low[y_max];
	for (int i = y_max-1; i >= y_min; i--)
	{
		prefix_sum_y_high[i] = prefix_sum_y_high[i + 1] + y_high[i];
		prefix_sum_y_low[i] = prefix_sum_y_low[i + 1] + y_low[i];
    }

	//get Max
	int prefix_x_max = -1;
	int prefix_y_max = -1;

	for (int i = x_min; i <= x_max; i++)
	{
		if (prefix_x_max < (prefix_sum_x_high[i] - prefix_sum_x_low[i]))
			prefix_x_max = (prefix_sum_x_high[i] - prefix_sum_x_low[i]);
	}
	for (int i = y_min; i <= y_max; i++)
	{
		if (prefix_y_max < (prefix_sum_y_high[i] - prefix_sum_y_low[i]))
			prefix_y_max = (prefix_sum_y_high[i] - prefix_sum_y_low[i]);
	}
	printf("%d\n", MAX(prefix_x_max, prefix_y_max));


	//free memory
	free(x_high);
	free(x_low);
	free(y_high);
	free(y_low);
	free(prefix_sum_x_high);
	free(prefix_sum_x_low);
	free(prefix_sum_y_high);
	free(prefix_sum_y_low);

	return 0;
}

