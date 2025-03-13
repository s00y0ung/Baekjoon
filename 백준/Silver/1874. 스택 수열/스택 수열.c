#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>

typedef struct StackType {
	int top;
	int arr[100000];
}StackType;

char ch[200002] = { '\0' };
int c = 0;

void push(StackType* s, int item)
{
	s->arr[++s->top] = item;
	ch[c++] = '+';
}
int pop(StackType* s)
{
	if (s->top == -1)
		return -1;

	ch[c++] = '-';
	return s->arr[s->top--];
}

int main()
{
	int N;
	scanf("%d", &N);

	StackType* s = (StackType *)malloc(sizeof(StackType));
	s->top = -1;
	
	int cnt = 1, n, start = 1;
	int tmp, flag = 1;
	while (cnt <= N)
	{
		scanf("%d", &n);
		if(start <= n)
		{
			for (start; start <= n; start++)
				push(s, start);
			pop(s);
		}
		else {

			tmp = pop(s);
			
			while (tmp != n)
			{
				if (s->top == -1)
				{
					flag = 0;
					break;
				}
				tmp = pop(s);
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
	
	free(s);

	return 0;
}