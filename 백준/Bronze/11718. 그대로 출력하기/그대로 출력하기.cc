#include <string>
#include <iostream>

using namespace std;

int main()
{
	string s;
	while (true)
	{
		getline(cin, s);
		cout << s << "\n";
		if (cin.eof())
			break;
	}

	cout << s;

	return 0;
}