#include <iostream>
#include <string>

using namespace std;

int	main(void)
{
	int		n;
	int		i;
	int		sum;
	string	str;

	sum = 0;
	cin >> n;
	cin.ignore();	// cin buffer에 \n이 남아서 지워줘야함
	getline(cin, str);
	while (str[i])
	{
		sum += str[i] - 48;
		i++;
	}
/*
	cin >> str;
	for (char ch : str)
	{
		sum += ch - 48;
	}
*/
	cout << sum << endl;
	return 0;
}
