#include <iostream>

using namespace std;

int main()
{
	int** arr = new int* [9];
	for (int i = 0; i < 9; i++)
		arr[i] = new int[9];

	int max = -1;
	int indexI, indexJ;
	for (int i = 0; i < 9; i++)
	{
		for (int j = 0; j < 9; j++)
		{
			cin >> arr[i][j];
			if (max < arr[i][j])
			{
				max = arr[i][j];
				indexI = i;
				indexJ = j;
			}
		}
	}
	
	cout << max <<"\n" << indexI+1 << " " << indexJ+1;


	return 0;
}