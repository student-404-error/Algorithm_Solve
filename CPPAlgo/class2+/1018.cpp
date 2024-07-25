// 체스판 다시 칠하기 S4

#include <iostream>
#include <string>

using namespace std;

int	main(void)
{
	int n, m;

	cin >> n >> m;
	string map[n];
	for (int i = 0; i < n; i++)
		cin >> map[i];
	for (int l = 0; l < n - 7; l++)
	{
		cout << "============\n";
		for (int k = 0; k < m - 7; k++)
		{
			cout << "------------\n";
			for (int i = 0; i < 8; i++)
			{
				for (int j = 0; j < 8; j++)
				{
					cout << map[i + l][j + k];
				}
				cout << '\n';
			}
		}
	}
}


/*
	브루트포스 알고리즘인데 그걸 어떻게 여기에 쓰지

	검사를 어떻게 하지?



*/
