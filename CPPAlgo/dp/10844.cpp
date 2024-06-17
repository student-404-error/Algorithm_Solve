#include <iostream>
#define MOD 1000000000
using namespace std;

int main (int argc, char *argv[]) {
	int	n;
	cin >> n;
	unsigned long long	dp[n][10];

	for (int i = 0; i < 10; i++) {
		dp[0][i] = 1;
	}
	dp[0][0] = 0;
	for (int i = 1; i < n; i++) {
		for (int j = 0; j < 10; j++) {
			if (j == 0)
				dp[i][0] = dp[i - 1][1];	
			else if (j == 9)
				dp[i][9] = dp[i - 1][8];
			else
				dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1];
			dp[i][j] %= MOD;
		}
	}
	int	s = 0;
	for (int i = 0; i < 10; i++) {
		s = (s + dp[n - 1][i]) % MOD;
	}
	cout << s << "\n";
	return 0;
}
