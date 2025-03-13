#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>

int heap[100001] = { 0 };
int heap_size = 0;

void insert_min_heap(int item)
{
	int i = ++(heap_size);
	
	while ((i != 1) && (abs(item) <= abs(heap[i / 2])))
	{
		if (abs(item) == abs(heap[i / 2]) && item > heap[i / 2])
		{
			break;
		}
		heap[i] = heap[i/2];
		i = i / 2;
	}

	heap[i] = item;
}
int delete_min_heap()
{
	int item = heap[1];
	int tmp = heap[heap_size--];
	int parent = 1;
	int child = 2;


	while (child <= heap_size)
	{
		if (child < heap_size && abs(heap[child]) == abs(heap[child + 1]))
		{
			if (heap[child] > heap[child + 1])
				child = child + 1;
		}
		else if (child < heap_size && abs(heap[child]) > abs(heap[child + 1]))
			child = child + 1;

		if (abs(tmp) < abs(heap[child]))
			break;
		else if (abs(tmp) == abs(heap[child]) && tmp < heap[child])
			break;

		heap[parent] = heap[child];
		parent = child;
		child = child * 2;
	}
	heap[parent] = tmp;
	
	return item;
}

int main()
{
	int N;
	scanf("%d", &N);

	int T;
	for (int i = 0; i < N; i++)
	{
		scanf("%d", &T);

		if (T == 0)
		{
			if (heap_size == 0)
				printf("0\n");
			else
				printf("%d\n", delete_min_heap());
		}
		else {
			insert_min_heap(T);
		}
	}

	return 0;
}