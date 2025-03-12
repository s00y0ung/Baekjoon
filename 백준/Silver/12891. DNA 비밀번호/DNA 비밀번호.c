#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

int check_dna(int password[], int an, int cn, int gn, int tn)
{
	if (password[0] < an) return -1;
	if (password[1] < cn) return -1;
	if (password[2] < gn) return -1;
	if (password[3] < tn) return -1;

	return 1;
}

int main()
{
	int P, S;
	char c;
	int dna[1000001] = { 0 };

	scanf("%d %d", &S, &P);

	for (int i = 0; i < S; i++) {
		scanf(" %c", &c);

		if (c == 'A') dna[i] = 0;
		else if (c == 'C') dna[i] = 1;
		else if (c == 'G') dna[i] = 2;
		else if (c == 'T') dna[i] = 3;
	}

	int an, cn, gn, tn;
	scanf("%d %d %d %d", &an, &cn, &gn, &tn);


	int s = 0, e = P - 1;
	int password[4] = { 0,0,0,0 };

	for (int i = 0; i < P; i++)
		password[dna[i]] += 1;

	int cnt = 0;
	while (e < S)
	{
		if (check_dna(password, an, cn, gn, tn) == 1)
			cnt++;

		password[dna[s]] -= 1;
		s++;

		e++;
		password[dna[e]] += 1;
	}

	printf("%d\n", cnt);

	return 0;
}