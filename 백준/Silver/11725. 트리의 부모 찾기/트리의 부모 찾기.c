#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>

#define MAX_VERTICES 100001

int visited[MAX_VERTICES] = { 0 };
int parent[MAX_VERTICES] = { 0 };

typedef struct GraphNode {
	int vertex;
	struct GraphNode* link;
}GraphNode;

typedef struct GraphType {
	int n;
	GraphNode* adj_list[MAX_VERTICES];
}GraphType;

void init(GraphType* g)
{
	g->n = 0;
	for (int i = 0; i < MAX_VERTICES; i++)
		g->adj_list[i] = NULL;
}

void insert_edge(GraphType* g, int u, int v)
{
	GraphNode* node = (GraphNode*)malloc(sizeof(GraphNode));
	node->vertex = v;
	node->link = g->adj_list[u];
	g->adj_list[u] = node;
}

void dfs(GraphType* g, int n)
{
	visited[n] = 1;
	for (GraphNode* w = g->adj_list[n]; w; w = w->link)
	{
		if (!visited[w->vertex]) 
		{
			parent[w->vertex] = n;
			dfs(g, w->vertex);
		}
	}
}

int main()
{
	int N;
	scanf("%d", &N);

	GraphType* g = (GraphType*)malloc(sizeof(GraphType));
	init(g);

	int u, v;
	for (int i = 1; i < N; i++)
	{
		scanf("%d %d", &u, &v);
		insert_edge(g, u, v);
		insert_edge(g, v, u);
	}

	dfs(g,1);

	for (int i = 2; i <= N; i++)
		printf("%d\n", parent[i]);

	free(g);

	return 0;
}