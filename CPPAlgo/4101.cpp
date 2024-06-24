#include <iostream>
#define MAX(f, s) (f > s ? "Yes\n" : "No\n")

using namespace std;
int main (int argc, char *argv[]) {
	int	a, b;

	while (1)
	{
		cin >> a >> b;
		if (a + b == 0)
			break;
		cout << MAX(a, b);
	}
	return 0;
}
