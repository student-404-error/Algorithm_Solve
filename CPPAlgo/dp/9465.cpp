#include <iostream>
#include <algorithm>

using namespace std;

int main (int argc, char *argv[]) {
	int	T, n;

	cin >> T;
	while (T--)
	{	
		cin >> n;
		unsigned long long	dp[2][n];
		long long	arr[2][n];
		for (int i = 0; i < 2; i++) {
			for (int j = 0; j < n; j++)
			{
				cin >> arr[i][j];
				dp[i][j] = 0;
			}
		}

		dp[0][0] = arr[0][0];
		dp[1][0] = arr[1][0];
		if (n > 1)
		{
			dp[0][1] = dp[1][0] + arr[0][1];
			dp[1][1] = dp[0][0] + arr[1][1];
		}
		for (int i = 2; i < n; i++)
		{
			dp[0][i] = arr[0][i] + max(dp[1][i - 1], dp[1][i - 2]);
			dp[1][i] = arr[1][i] + max(dp[0][i - 1], dp[0][i - 2]);
		}
		cout << max(dp[0][n - 1], dp[1][n - 1]) << "\n";
	}
	return 0;
}
