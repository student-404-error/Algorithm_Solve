include <iostream>

using namespace std;

int	main(void)
{
	int	n, i;
	int	a, b;

	cin >> n;
	i = 1;
	while (i <= n)
	{
		cin >> a >> b;
		cout << "Case #" << i++ << ": " << a << " + " << b << " = " << a + b << endl;
	}

	return 0;
}
