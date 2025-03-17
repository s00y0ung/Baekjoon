#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <string.h>

int find_root(int *arr, int a)
{
	while (arr[a] != -1)
		a = arr[a];

	return a;
}
void union_vertex(int *arr, int a, int b)
{
	int roota = find_root(arr, a);
	int rootb = find_root(arr, b);

	if (roota != rootb)
		arr[roota] = rootb;
}

int main()
{
	int N, M;
	scanf("%d %d", &N, &M);

	int rootVertex[1001];
	memset(rootVertex, -1, sizeof(int) * 1001);
	int v1, v2;
	for (int i = 0; i < M;i++)
	{
		scanf("%d %d", &v1, &v2);
		union_vertex(rootVertex, v1, v2);
	}

	int cnt = 0;
	for (int i = 1; i <= N; i++)
	{
		if (rootVertex[i] == -1)
			cnt += 1;
	}
	printf("%d\n", cnt);

	return 0;
}