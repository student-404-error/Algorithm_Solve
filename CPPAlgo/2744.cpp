#include <iostream>
#include <string>

int	main(void)
{
	std::string	str;

	std::cin >> str;
	int	i = 0;
	while (str[i])
	{
		if (str[i] >= 97 && str[i] <= 122)
			std::cout << (char) (str[i] - 32);
		else
			std::cout << (char) (str[i] + 32);
		i++;
	}
	return (0);
}
