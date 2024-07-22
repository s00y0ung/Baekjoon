#include <iostream>
#include <string>
using std::cin;
using std::cout;

int main()
{
	char arr[5][15] = { NULL, };
	std::string s;
	for (int i = 0; i < 5; i++)
	{
		std::getline(cin, s);
		for (int j = 0; j < s.size(); j++)
			arr[i][j] = s[j];
	}

	for (int i = 0; i < 15; i++)
	{
		for (int j = 0; j < 5; j++)
		{
			if(arr[j][i] != NULL)
				cout << arr[j][i];
		}
	}
}
