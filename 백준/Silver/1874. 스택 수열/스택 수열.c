#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

int arr[100001];
int top = -1;

char ch[200002] = { '\0' };
int c = 0;

void push(int item)
{
	arr[++top] = item;
	ch[c++] = '+';
}
int pop()
{
	if (top == -1)
		return -1;

	ch[c++] = '-';
	return arr[top--];
}

int main()
{
	int N;
	scanf("%d", &N);

	int cnt = 1, n, start = 1;
	int tmp, flag = 1;
	while (cnt <= N)
	{
		scanf("%d", &n);
		if(start <= n)
		{
			for (start; start <= n; start++)
				push(start);
			pop();
		}
		else {

			tmp = pop();
			
			while (tmp != n)
			{
				if (top == -1)
				{
					flag = 0;
					break;
				}
				tmp = pop();
			}
		}
		cnt++;
	}

	if (flag)
	{
		for (int i = 0; i < c; i++)
			printf("%c\n", ch[i]);
	}
	else {
		printf("NO\n");
	}
	

	return 0;
}