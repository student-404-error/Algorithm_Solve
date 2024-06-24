#include <iostream>
#include <string>

using namespace std;

int	main(void)
{
	int	n, cnt = 666;
	string str;

	cin >> n;
	while (1)
	{
		str = to_string(cnt);
		if (str.find("666") != string::npos)
			n--;
		if (!n)
			break;
		cnt++;
	}
	cout << str << '\n';
}
