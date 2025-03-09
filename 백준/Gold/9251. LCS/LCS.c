#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <string.h>

#define MAX(x,y) ((x) > (y) ? (x) : (y))

int main()
{
	char t1[1002];
	char t2[1002];

	int s[1002][1002] = { 0 };

	scanf("%s %s", t1, t2);

	for (int i = 1; i <= strlen(t1); i++)
	{
		for (int j = 1; j <= strlen(t2); j++)
		{
			if (t1[i-1] == t2[j-1])
			{
				s[i][j] = s[i-1][j-1] + 1;
			}
			else
			{
				s[i][j] = MAX(s[i][j - 1], s[i - 1][j]);
			}
		}
	}

	printf("%d", s[strlen(t1)][strlen(t2)]);

	return 0;
}