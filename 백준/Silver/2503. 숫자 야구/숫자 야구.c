#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef struct stack {
	int arr[1000];
	int top;
}stack;

void push(stack *s, int n)
{
	s->arr[++(s->top)] = n;
}
int pop(stack* s)
{
	return s->arr[(s->top)--];
}

int checking(int n, int num, int S, int B)
{
	int tmp1, tmp2, tmp3, tmp4;
	int sCnt = 0, bCnt = 0;

	tmp1 = n / 100;
	tmp2 = num / 100;
	tmp3 = (num / 10) % 10;
	tmp4 = num % 10;

	if (tmp1 == tmp2)
		sCnt += 1;
	else if (tmp1 == tmp3 || tmp1 == tmp4) {
		bCnt += 1;
	}

	tmp1 = (n / 10) % 10;
	if (tmp1 == tmp3)
		sCnt += 1;
	else if (tmp1 == tmp2 || tmp1 == tmp4) {
		bCnt += 1;
	}

	tmp1 = n % 10;
	if (tmp1 == tmp4)
		sCnt += 1;
	else if (tmp1 == tmp2 || tmp1 == tmp3) {
		bCnt += 1;
	}

	if (sCnt == S && bCnt == B)
		return 1;
	return 0;
}

void backTracking(stack* s, int *numArr,int num, int S, int B)
{
	if (s->top == 2)
	{
		int n = 0;
		for (int i = 0; i <= 2; i++) {
			n += (s->arr[2-i] * (pow(10, i)));
		}
		if ( checking(n, num, S, B) == 0) //checking S, B
		{
			numArr[n] = 0;
		}
		return;
	}

	for (int i = 0; i < 10; i++)
	{
		push(s, i);
		backTracking(s, numArr, num, S, B);
		pop(s);
	}
}

int main()
{
	int N;
	scanf("%d", &N);

	stack* s = (stack*)malloc(sizeof(stack));
	s->top = -1;

	int* numArr = (int*)malloc(sizeof(int) * 1000);
	int tmp1, tmp2, tmp3;
	for (int i = 0; i < 1000; i++)
	{
		tmp1 = i / 100;
		tmp2 = (i / 10) % 10;
		tmp3 = i % 10;
		
		if (numArr < 122)
			numArr[i] = 0;
		else if (tmp1 == tmp2 || tmp1 == tmp3 || tmp2 == tmp3)
			numArr[i] = 0;
		else if (tmp1 == 0 || tmp2 == 0 || tmp3 == 0)
			numArr[i] = 0;
		else
			numArr[i] = 1;
	}

	int num, S, B;
	for (int i = 0; i < N; i++)
	{
		scanf("%d %d %d", &num, &S, &B);
		backTracking(s, numArr, num, S, B);
	}

	int cnt = 0;
	for (int i = 0; i < 1000; i++)
	{
		if (numArr[i])
			cnt += 1;
	}
	printf("%d\n", cnt);

	free(s);

	return 0;
}