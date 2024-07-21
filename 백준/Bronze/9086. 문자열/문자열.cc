#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main()
{
	string s, ss;
	int T;
	cin >> T;
	
	vector<string> v;
	for (int i = 0; i < T; i++)
	{
		cin >> s; 

		ss = s.front();
		ss = ss + s.back();
		
		v.push_back(ss);
	}
	
	for(int i = 0; i < T; i++)
	    cout << v[i] << "\n";

	return 0;
}