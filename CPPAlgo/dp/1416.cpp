#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main (int argc, char *argv[]) {
  int n;

  cin >> n;
  vector<int> dp(n + 1, 0);
  for (int i = 2; i <= n; i++) {
    dp[i] = dp[i - 1] + 1;
    if (i % 2 == 0)
      dp[i] = min(dp[i / 2] + 1, dp[i]);
    if (i % 3 == 0)
      dp[i] = min(dp[i / 3] + 1, dp[i]);
  }
  cout << dp[n] << "\n";
  return 0;
}
