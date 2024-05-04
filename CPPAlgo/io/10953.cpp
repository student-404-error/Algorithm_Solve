#include <iostream>
#include <string>

using namespace std;

int	main(void)
{
	int	n;
	string str;

	cin >> n;
	while (n--)
	{
		cin >> str;
		cout << (int) str[0] + (int) str[2] - 96 << endl;
	}
	return 0;
}
