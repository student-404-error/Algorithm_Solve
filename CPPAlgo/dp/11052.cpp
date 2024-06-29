#include <iostream>

using namespace std;

int main (int argc, char *argv[]) {
	int	N;

	cin >> N;
	vector<int>	dp(N + 1, 0);
	vector<int>	arr(N + 1, 0);

	for (int i = 1; i <= N; i++) {
		cin >> arr[i];
	}
	for (int i = 1; i <= N; i++) {
		for (int j = i; j <= N; j++) {
			dp[i] = max(dp[i], arr[i] * (N - i + 1));
		}
	}
	return 0;
}
