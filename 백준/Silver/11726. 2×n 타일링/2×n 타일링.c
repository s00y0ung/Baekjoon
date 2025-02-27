#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

int main()
{
	int s[1001] = { 0 };

	s[1] = 1;
	s[2] = 2;

	int S;
	scanf("%d", &S);

	for (int i = 3; i <= S; i++)
		s[i] = (s[i - 1] + s[i - 2])%10007;

	printf("%d\n", s[S]);

	return 0;
}