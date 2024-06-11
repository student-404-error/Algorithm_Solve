#include <iostream>

using namespace std;

int	main(void)
{
	int	h;
	int	w;
	
	int	yard;
	cin >> w >> h;
	yard = w * h;
	int	arce = 4840 * 5;
	if (yard % arce >= 1)
		cout << yard / arce + 1 << "\n";
	else
		cout << yard / arce << "\n";
}
