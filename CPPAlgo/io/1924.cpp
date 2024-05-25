#include <iostream>
#include <string>

using namespace std;

int	main(void)
{
	int	m, d;
	int	arr[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
	string date[7] = {"SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"};
	cin >> m >> d;
	for (int i = 0; i < m - 1; i++)
		d += arr[i];
	cout << date[d % 7] << endl;
	return 0;
}
