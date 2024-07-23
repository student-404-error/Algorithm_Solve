#include <iostream>

int	main(void)
{
	int a, b;
	std::cin >> a >> b;

	a *= a;
	b *= b;
	std::cout << a - b << '\n';
	return (0);
}
