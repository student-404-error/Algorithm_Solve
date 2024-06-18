#include <iostream>

using namespace std;

int main (int argc, char *argv[]) {
	int	n;

	cin >> n;

	unsigned long long	arr[n][2];
	arr[0][0] = 0;
	arr[0][1] = 1;
	for (int i = 1; i < n; i++) {
		arr[i][0] = arr[i - 1][0] + arr[i - 1][1];
		arr[i][1] = arr[i - 1][0];
	}
	cout << arr[n - 1][0] + arr[n - 1][1] << "\n";
	return 0;
}
