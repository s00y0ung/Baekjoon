#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>

#define INF 1000001

int parent[10001];

void set_init(int n)
{
	for (int i = 0; i < n; i++)
		parent[i] = i;
}
int set_find(int curr)
{
	if (parent[curr] == curr)
		return curr;

	return (parent[curr] = set_find(parent[curr]));
}
void set_union(int a, int b)
{
	int root_a = set_find(a);
	int root_b = set_find(b);

	if (root_a > root_b)
		parent[root_a] = root_b;
	else if(root_b > root_a)
		parent[root_b] = root_a;
}

struct Edge {
	int start, end, weight;
};

typedef struct GraphType {
	int n;
	struct Edge edges[100001];
}GraphType;

void graph_init(GraphType* g)
{
	g->n = 0;
	for (int i = 0; i < 100001; i++)
	{
		g->edges[i].start = 0;
		g->edges[i].end = 0;
		g->edges[i].weight = INF;
	}
}
void insert_edge(GraphType* g, int start, int end, int w)
{
	g->edges[g->n].start = start;
	g->edges[g->n].end = end;
	g->edges[g->n].weight = w;
	g->n++;
}

int compare(const void* a, const void* b)
{
	struct Edge* x = (struct Edge*)a;
	struct Edge* y = (struct Edge*)b;
	return (x->weight - y->weight);
}

int kruskal(GraphType* g, int V)
{
	int edge_accepted = 0;
	int uset, vset;
	struct Edge e;

	set_init(V);
	qsort(g->edges, g->n, sizeof(struct Edge), compare);

	int i = 0;
	int value = 0;
	while (edge_accepted < V-1)
	{
		e = g->edges[i];
		uset = set_find(e.start);
		vset = set_find(e.end);

		if (uset != vset)
		{
			edge_accepted++;
			value += e.weight;
			set_union(uset, vset);
		}
		i++;
	}

	return value;
}


int main()
{
	int V, E;
	scanf("%d %d", &V, &E);

	GraphType* g = (GraphType*)malloc(sizeof(GraphType));
	graph_init(g);

	int s, e, w;
	for (int i = 0; i < E; i++)
	{
		scanf("%d %d %d", &s, &e, &w);
		insert_edge(g, s, e, w);
	}

	printf("%d\n", kruskal(g,V));

	free(g);

	return 0;
}