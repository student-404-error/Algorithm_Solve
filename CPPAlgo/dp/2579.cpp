#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main (int argc, char *argv[]) {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int	N;

	cin >> N;
	vector<int>	arr(N + 1, 0);
	vector<int>	dp(N + 1, 0);

	for (int i = 1; i <= N; i++) {
		cin >> arr[N - i];
	}
	for (int i = 0; i <= N; i++) {
		cout << arr[i] << " ";
	}
	return 0;
}
