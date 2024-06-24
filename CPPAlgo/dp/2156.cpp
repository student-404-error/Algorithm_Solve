#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main (int argc, char *argv[]) {
	int	n, cnt = 1;

	cin >> n;
	vector<long long>	arr(n + 1, 0);
	vector<long long>	dp(n + 1, 0);

	for (int i = 1; i <= n; i++) {
		cin >> arr[i];
	}
	dp[0] = arr[0];
	dp[1] = arr[1];
	dp[2] = arr[1] + arr[2];
	for (int i = 3; i <= n; i++) {
		dp[i] = max(dp[i - 3] + arr[i - 1] + arr[i], max(dp[i - 2] + arr[i], dp[i - 1]));
	}
	cout << *max_element(dp.begin(), dp.end()) << "\n";
	return 0;
}
