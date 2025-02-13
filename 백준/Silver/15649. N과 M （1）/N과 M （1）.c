#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>

// 1 2 3 4 5 6 7 8
// a b c d e f g h
int main()
{
	int N, M;
	scanf("%d %d", &N, &M);

	for (int a = 1; a <= N; a++)
	{
		if (M == 1)
		{
			printf("%d\n", a);
			continue;
		}
		for (int b = 1; b <= N; b++)
		{
			if (a == b)
				continue;

			if (M == 2)
			{
				printf("%d %d\n", a, b);
				continue;
			}
			for (int c = 1; c <= N; c++)
			{
				if (a == c || b == c)
					continue;

				if (M == 3)
				{
					printf("%d %d %d\n",a,b,c);
					continue;
				}

				for (int d = 1; d <= N; d++)
				{
					if (a == d || b == d || c == d)
						continue;

					if (M == 4)
					{
						printf("%d %d %d %d\n",a ,b, c, d);
						continue;
					}

					for (int e = 1; e <= N; e++)
					{
						if (a == e || b == e || c == e || d == e)
							continue;

						if (M == 5)
						{
							printf("%d %d %d %d %d\n",a,b,c,d,e);
							continue;
						}
						for (int f = 1; f <= N; f++)
						{
							if (a == f || b == f || c == f || d == f || e == f)
								continue;

							if (M == 6)
							{
								printf("%d %d %d %d %d %d\n", a, b, c, d, e,f);
								continue;
							}
							for (int g = 1; g <= N; g++)
							{
								if (a == g || b == g || c == g || d == g || e == g || f == g)
									continue;

								if (M == 7)
								{
									printf("%d %d %d %d %d %d %d\n", a, b, c, d, e, f, g);
									continue;
								}
								for (int h = 1; h <= N; h++)
								{
									if (a == h || b == h || c == h || d == h || e == h || f == h || g == h)
										continue;
									printf("%d %d %d %d %d %d %d %d\n", a, b, c, d, e, f, g,h);
								}
							}
						}
					}
				}
			}
		}
	}
}