#include <iostream>
using namespace std;

int main()
{
	int num1, num2;

	cin >> num1;
	cin >> num2;

	cout << num1 * (num2 % 10) << "\n";
	cout << num1 * (num2 / 10 % 10)  << "\n";
	cout << num1 * (num2 /100) << "\n";
	cout << num1 * (num2) << "\n";

	return 0;
}