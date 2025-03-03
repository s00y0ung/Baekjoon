#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>


int find_root(int *numArr, int n)
{
	if(numArr[n] == n)
        return n;
    return (numArr[n] = find_root(numArr, numArr[n]));
}

int main()
{
	int N, M;
	scanf("%d %d", &N, &M);

	int* numArr = (int*)malloc(sizeof(int) * (N+1));

	for (int i = 0; i <= N; i++) 
		numArr[i] = i;

	int check, a, b;
	int root_a, root_b;
	for (int i = 0; i < M; i++)
	{
		scanf("%d %d %d", &check, &a, &b);
		if (check == 1)
		{
			if (find_root(numArr, a) == find_root(numArr, b))
				printf("YES\n");
			else
				printf("NO\n");
		}
		else {
			root_a = find_root(numArr, a);
			root_b = find_root(numArr, b);
			if (root_a != root_b)
			{	
				numArr[root_a] = root_b;
			}
		}
	}

	free(numArr);

	return 0;
}