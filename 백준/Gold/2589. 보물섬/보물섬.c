#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define  MAX(x,y) ((x) >(y) ? (x) : (y))

typedef struct GraphNode {
	int vertex;
	struct GraphNode* link;
}GraphNode;
typedef struct GraphType {
	int n;
	GraphNode* node[2500];
}GraphType;

void init(GraphType* g)
{
	g->n = 0;
	for (int i = 0;i < 2500; i++) {
		g->node[i] = NULL;
	}
}
void insert_edge(GraphType* g, int u, int v)
{
	GraphNode* gn = (GraphNode*)malloc(sizeof(GraphNode));
	gn->vertex = v;
	gn->link = g->node[u];
	g->node[u] = gn;
}

typedef struct QueueType {
	int queue[2500];
	int rear;
	int front;
}QueueType;

void push(QueueType* q, int n)
{
	q->queue[++(q->rear)] = n;
}
int pop(QueueType* q)
{
	return q->queue[++(q->front)];
}

int bfs(GraphType* g, int* visited, int start, int size)
{
	QueueType* q = (QueueType*)malloc(sizeof(QueueType));
	q->rear = -1;
	q->front = -1;

	int tmpList[2500];
	push(q, start);
	visited[start] = 1;

	int v;
	int level = 0;

	int cnt = -1;

	while (cnt != 0)
	{
		cnt = 0;
		while (q->rear != q->front)
		{
			v = pop(q);

			for (GraphNode* w = g->node[v];w;w = w->link)
			{
				if (visited[w->vertex] == 0)
				{
					visited[w->vertex] = 1;
					tmpList[cnt++] = w->vertex;
				}
			}
		}

		for (int i = 0; i < cnt; i++) {
			push(q, tmpList[i]);
		}
		level++;
	}
	return --level;
}

int main()
{
	int N, M;
	scanf("%d %d", &N, &M);

	char map[50][50];
	char tmp;
	scanf("%c", &tmp);
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			scanf(" %c", &map[i][j]);
		}
		scanf("%c", &tmp);
	}


	GraphType* g = (GraphType*)malloc(sizeof(GraphType));
	init(g);

	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			if (map[i][j] == 'L')
			{

				if (i != N - 1 && map[i + 1][j] == 'L')
				{
					insert_edge(g, ((i + 1) * M + j), (i * M + j));
					insert_edge(g, (i * M + j), ((i + 1) * M + j));
				}
				if (j != M - 1 && map[i][j + 1] == 'L')
				{
					insert_edge(g, (i * M + (j + 1)), (i * M + j));
					insert_edge(g, (i * M + j), (i * M + (j + 1)));
				}
			}
		}
	}

	int visited[2500] = { 0 };

	int t;
	int maxNum = -1;
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			if (map[i][j] == 'L' && visited[i * M + j] == 0) {
				t = bfs(g, visited, i * M + j, N * M);
				memset(visited, 0, sizeof(int) * 2500);
				if (t > maxNum)
					maxNum = t;
			}
		}
	}
	printf("%d\n", maxNum);


	free(g);

	return 0;
}
