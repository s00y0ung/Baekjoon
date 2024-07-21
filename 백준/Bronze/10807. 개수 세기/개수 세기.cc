#include <iostream>
using namespace std;

int main()
{
    int N, v;
    int count = 0;
    cin >> N;

    int* arr = new int[N];
    for (int i = 0; i < N; i++)
    {
        cin >> arr[i];
    }

    cin >> v;
    for (int i = 0; i < N; i++)
    {
        if (arr[i] == v)
            count += 1;
    }
    cout << count;

    return 0;
}