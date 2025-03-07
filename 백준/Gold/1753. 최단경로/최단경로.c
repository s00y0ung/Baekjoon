#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>

#define MAX_V 50000
#define MAX_E 500000
#define INF 10000000

typedef struct Edge {
	int end, weight;
	struct Edge* link;
}Edge;

typedef struct HeapType {
	Edge* heap[MAX_E];
	int heap_size;
}HeapType;

int distance[MAX_V];
int visited[MAX_V];


Edge* insert(Edge* head, int end, int weight)
{
	Edge* e = (Edge*)malloc(sizeof(Edge));
	e->end = end;
	e->weight = weight;
	e->link = head;
	head = e;

	return head;
}

void insert_min_heap(HeapType* h, Edge* e)
{
	int i = ++(h->heap_size);

	while ((i != 1) && e->weight < h->heap[i / 2]->weight)
	{
		h->heap[i] = h->heap[i / 2];
		i /= 2;
	}
	h->heap[i] = e;
}
Edge* delete_min_heap(HeapType* h)
{
	int child, parent;
	Edge* item, * tmp;

	item = h->heap[1];
	tmp = h->heap[(h->heap_size)--];
	child = 2;
	parent = 1;

	while (child <= h->heap_size)
	{
		if ((child < h->heap_size) && (h->heap[child]->weight > h->heap[child + 1]->weight))
			child++;
		if (tmp->weight <= h->heap[child]->weight)
			break;

		h->heap[parent] = h->heap[child];
		parent = child;
		child *= 2;
	}

	h->heap[parent] = tmp;
	return item;
}

void dijkstra(int startNum, int N, Edge** edgeHead, HeapType* h)
{
	for (int i = 0; i <= N; i++)
	{
		distance[i] = INF;
		visited[i] = 0;
	}
	distance[startNum] = 0;
	
	Edge* e = (Edge *)malloc(sizeof(Edge));
	e->end = startNum;
	e->weight = 0;

	insert_min_heap(h, e);

	Edge* cur;
	while (h->heap_size > 0)
	{
		cur = delete_min_heap(h);

		if (visited[cur->end])
			continue;
		visited[cur->end] = 1;

		for (e = edgeHead[cur->end]; e != NULL; e = e->link)
		{
			if (distance[e->end] > distance[cur->end] + e->weight)
			{
				distance[e->end] = distance[cur->end] + e->weight;
				e->weight = distance[e->end];
				insert_min_heap(h, e);
			}
		}
	}

}

int main()
{
	int N, E;
	scanf("%d %d", &N, &E);
	int startNum;
	scanf("%d", &startNum);

	HeapType* h = (HeapType*)malloc(sizeof(HeapType));
	h->heap_size = 0;

	Edge** edgeHead = (Edge**)malloc(sizeof(Edge*) * (N + 1));
	for (int i = 0; i <= N; i++)
	{
		edgeHead[i] = NULL;
	}

	int s, e, w;
	for (int i = 0; i < E; i++)
	{
		scanf("%d %d %d", &s, &e, &w);
		edgeHead[s] = insert(edgeHead[s], e, w);
	}

	dijkstra(startNum, N, edgeHead, h);
	for (int i = 1; i <= N; i++)
	{
		if (distance[i] >= INF)
			printf("INF\n");
		else
			printf("%d\n", distance[i]);
	}

	free(h);

	return 0;
}