#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <string.h>

int main()
{
	int N;
	scanf("%d", &N);
	
	char s[100000] = { '\0' };
	scanf("%s", s);
	int strLen = strlen(s);

	char check[27] = { '\0' };
	int cnt = 0;
	int tmp = 0;
	int maxLen = -1;

	int pointer = 0;
	while(pointer < strLen)
	{
		int k;
		for(k = pointer; k < strLen; k++)
		{
			if (tmp >= N)
				break;
			if (strchr(check, s[k]) == '\0')
			{
				check[tmp] = s[k];
				tmp++;
			}
			else if(strlen(check) == 1)
				pointer++;
			cnt++;
		}

		for(int j = k; j < strLen; j++)
		{
			if (strchr(check, s[j]) == NULL)
				break;
			else
				cnt++;
		}

		if (maxLen < cnt)
		{
			maxLen = cnt;
		}
		cnt = 0;
		tmp = 0;
		pointer++;
		
		for(int w = 0; w < 27; w++)
			check[w] = '\0';
	}

	printf("%d\n", maxLen);

	return 0;
}
