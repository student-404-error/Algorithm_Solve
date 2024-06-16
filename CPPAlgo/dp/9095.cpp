#include <iostream>

using namespace std;

int main (int argc, char *argv[]) {
	int	n;
	int	dp[11];
	int	i;
	int	a;

	cin >> n;
	dp[0] = 1;
	dp[1] = 2;
	dp[2] = 4;
	i = 3;
	while (i < 11) {
		dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1];
		i++;
	}
	i = 0;
	while (i < n) {
		cin >> a;
		cout << dp[a - 1] << "\n";
		i++;
	}
	return 0;
}
