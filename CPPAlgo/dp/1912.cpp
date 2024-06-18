#include <iostream>
#include <algorithm>

using namespace std;

int main (int argc, char *argv[]) {
	int	n;
	cin >> n;
	long long	dp[n];
	long long	arr[n];
	for (int i = 0; i < n; i++)
		cin >> dp[i];
	for (int i = 0; i < n; i++)
		arr[i] = 0;
	arr[0] = dp[0];
	for (int j = 1; j < n; j++) {
		arr[j] = max(dp[j], arr[j - 1] + dp[j]);
	}
	int	m = arr[0];
	for (int i = 1; i < n; i++)
		m = max(arr[i], (long long)m);
	cout << m << "\n";
	return 0;
}
