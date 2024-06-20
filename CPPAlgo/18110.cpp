#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <numeric>

using namespace std;

int main (int argc, char *argv[]) {
	int n;
	int s;

	cin >> n;
	if (n == 0)	{
		cout << "0\n";
		return (0);
	}
	vector<int> arr(n, 0);
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}
	sort(arr.begin(), arr.end());
	int	slice = floor(n * 0.15 + 0.5);
	s = accumulate(arr.begin() + slice, arr.end() - slice, 0);
	cout << floor((float)s / (n - slice * 2) + 0.5) << "\n";
	return 0;
}
