#include <iostream>
#include <string>

using namespace std;

int	main(void)
{
	string	str;
	int		i;

	cin >> str;
	i = 0;
	while (str[i])
	{
		cout << str[i];
		i++;
		if (i % 10 == 0)
			cout << endl;
	}
	cout << endl;
	return 0;
}
