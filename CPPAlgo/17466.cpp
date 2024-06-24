#include <iostream>

using namespace std;

int	main(void)
{
	unsigned long long	N, P;

	cin >> N >> P;
	unsigned long long	s = 1;
	for (int i = N; i > 1; i--)
	{
		s = (s * (i % P)) % P;
	}
	cout << s << '\n';
}
