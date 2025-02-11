#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

typedef struct queue {
	int arr[1000000];
	int front;
	int rear;
}queue;

void queueInit(queue* q)
{
	q->front = -1;
	q->rear = -1;
}
void insertq(queue* q, int n)
{
	q->arr[++(q->rear)] = n;
}
int deleteq(queue* q)
{
	return q->arr[++(q->front)];
}

int radix_sort(int n_list[], int N, int maxNum)
{
	queue **q_list = (queue **)malloc(sizeof(queue*) * 20);

	for (int i = 0; i < 20; i++) {
		q_list[i] = (queue*)malloc(sizeof(queue));
		queueInit(q_list[i]);
	}

	int curr;
	int radix = 1;
	while (radix < maxNum+1)
		radix = radix * 10; //radix 자리수 구하기


	for (int i = 1; i < radix; i = i*10)
	{
		//insert
		for (int j = 0; j < N; j++)
		{
			curr = (n_list[j] / i) % 10;
			if (n_list[j] < 0) //음수
			{
				insertq(q_list[curr*-1], n_list[j]);
			}
			else //양수
				insertq(q_list[curr+10], n_list[j]);
		}
		
		//delete
		int cnt = 0; //음수 먼저 출력
		for (int j = 9; j >=0; j--)
		{
			while (q_list[j]->rear != q_list[j]->front)
			{
				n_list[cnt++] = deleteq(q_list[j]);
			}
		} //양수 다음 출력
		for (int j = 10; j < 20; j++)
		{
			while (q_list[j]->rear != q_list[j]->front)
			{
				n_list[cnt++] = deleteq(q_list[j]);
			}
		}
	}

	for (int j = 0; j < N; j++)
	{
		printf("%d\n", n_list[j]);
	}

	for (int i = 0; i < 20; i++) {
		free(q_list[i]);
	}
	free(q_list);

	return 0;
	
}

int main()
{
	int N, num;
	int maxNum = -1000001;
	scanf("%d", &N);

	int* n_list = (int*)malloc(sizeof(int) * N);
	for (int i = 0; i < N; i++)
	{
		scanf("%d", &num);
		n_list[i] = num;

		if (num < 0)
			num *= -1;

		if (maxNum < num)
			maxNum = num;
	}
	radix_sort(n_list, N, maxNum);

	free(n_list);
	return 0;
}