#include <iostream>
#include <string>

using namespace std;
int	main(void)
{
	string number;

	cin >> number;
	for (int i = 0; i < 3; i++)
	{
		if (number[i] != '5')
		{
			cout << "NO\n";
			return (1);
		}
	}
	cout << "YES\n";
}
