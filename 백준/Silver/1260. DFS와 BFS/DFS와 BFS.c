#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>

#define TRUE 1
#define FALSE 0
#define MAX_VERTICES 1001

typedef int element;
typedef struct GraphType {
	element n; //정점의 개수
	element adj_mat[MAX_VERTICES][MAX_VERTICES];
}Graph;

void init(Graph* g, int n)
{
	int r, c;
	g->n = 0;
	for (r = 0; r < MAX_VERTICES; r++)
		for (c = 0; c < MAX_VERTICES; c++)
			g->adj_mat[r][c] = 0;
}
void insert_vertex(Graph* g, int v)
{
	if (((g->n) + 1) > MAX_VERTICES)
	{
		fprintf(stderr, "그래프 : 정점의 개수 초과");
		return;
	}
	g->n++;
}
void insert_edge(Graph* g, int start, int end)
{
	if (start >= g->n || end >= g->n) {
		fprintf(stderr, "그래프 : 정점 번호 오류");
		return;
	}
	g->adj_mat[start][end] = 1;
	g->adj_mat[end][start] = 1;
}
////////////////////////////////////////////////
//DFS
typedef struct stack {
	int arr[10001];
	int top;
}StackType;
void push(StackType* s, int n)
{
	s->arr[++(s->top)] = n;
}
int pop(StackType* s)
{
	return s->arr[(s->top)--];
}
void dfs_mat(Graph* g, int start, int N)
{
	StackType* s = (StackType*)malloc(sizeof(StackType));
	int* visited = (int*)malloc(sizeof(int) * (N + 1));
	for (int i = 0; i <= N; i++)
		visited[i] = 0;

	s->top = 0;

	push(s, start);

	int curr;
	while (s->top > 0)
	{
		curr = pop(s);
		if (visited[curr] == 0) {
			visited[curr] = 1;
			printf("%d ", curr);
		}


		for (int i = N; i > 0; i--)
		{
			if (visited[i] == 0 && g->adj_mat[curr][i] == 1) {
				push(s, i);
			}
		}
	}
}

////////////////////////////////////////////////
//BFS
typedef struct queue {
	element que[10001];
	int front;
	int rear;
}queue;

void insert(queue* q, int n)
{
	q->que[++(q->rear)] = n;
}
int delete(queue* q)
{
	return q->que[++(q->front)];
}
void bfs_mat(Graph* g, int start, int N)
{
	queue* q = (queue*)malloc(sizeof(queue));
	q->front = -1;
	q->rear = -1;
	int* visited = (int*)malloc(sizeof(int) * (N + 1));
	for (int i = 0; i <= N; i++)
		visited[i] = 0;

	insert(q, start);

	int curr;
	while (q->front != q->rear)
	{
		curr = delete(q);
		visited[curr] = 1;
		printf("%d ", curr);

		for (int i = 1; i <= N; i++)
		{
			if (g->adj_mat[curr][i] == 1 && visited[i] == 0)
			{
				insert(q, i);
				visited[i] = 1;
			}
		}
	}
}


int main()
{
	Graph* g = (Graph*)malloc(sizeof(Graph));
	int N, M, V;
	int start, end;
	scanf("%d %d %d", &N, &M, &V);

	init(g, N);
	for (int i = 0; i <= N; i++)
		insert_vertex(g, i);
	for (int i = 0; i < M; i++)
	{
		scanf("%d %d", &start, &end);
		insert_edge(g, start, end);
	}

	dfs_mat(g, V, N);
	printf("\n");
	bfs_mat(g, V, N);
	printf("\n");

	return 0;
}