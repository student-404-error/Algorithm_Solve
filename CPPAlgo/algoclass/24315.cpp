#include <iostream>

using namespace std;

int main (int argc, char *argv[]) {
	int	a1, a0, c1, c2, n0;
	int	flag;

	cin >> a1 >> a0;
	cin >> c1 >> c2;
	cin >> n0;

	if (a1 * n0 + a0 >= c1 * n0 && a1 >= c1)
		flag = 1;
	else
		flag = 0;
	if (a1 * n0 + a0 <= c2 * n0 && a1 <= c2 && flag == 1)
		flag = 1;
	else {
		flag = 0;
	}
	cout << flag << '\n';
	return 0;
}
