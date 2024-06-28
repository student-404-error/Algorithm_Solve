#include <iostream>
#include <vector>

using namespace std;

int main (int argc, char *argv[]) {
	int N;

	cin >> N;
	if ((3 * N) % 2 != 0){
		cout << "0\n";
		return (0);
	}
	vector<int> dp(N + 1, 0);
	dp[0] = 1;
	dp[2] = 3;
	for (int i = 4; i <= N; i += 2)
	{
		dp[i] = dp[i - 2] * 3;
		for (int j = i - 4; j >= 0; j -= 2)
		{
			dp[i] += (dp[j] * 2);
		}
	}
	cout << dp[N] << "\n";
	return 0;
}
