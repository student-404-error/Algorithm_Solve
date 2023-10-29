#include <iostream>

using namespace std;

int main()
{
	int a, b;
	a = 1;
	b = 2;
	int tmp;
	int c;
	cin >> c;
	if (c == 1)
	{
		cout<<a;
	}
	else if (c == 2)
	{
		cout << b;
	}
	else
	{
		for (int i = 3; i <= c; i++)
		{
			tmp = (a + b)%10007;
			a = b;
			b = tmp;
		}
		cout << tmp;
	}
	return 0;
}

