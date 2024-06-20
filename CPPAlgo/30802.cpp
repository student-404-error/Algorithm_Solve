#include <iostream>

using namespace std;

int main (int argc, char *argv[]) {
	long long	n;
	int	size[6];
	int T, P;
	int	s = 0;
	cin >> n;
	for (int i = 0; i < 6; i++)
		cin >> size[i];
	cin >> T >> P;
	for (int i = 0; i < 6; i++)
	{
		s = s + size[i] / T;
		if (size[i] % T != 0)
			s++;
	}
	cout << s << "\n" << n / P << " " << n % P << "\n";
	return 0;
}
