#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main (int argc, char *argv[]) {
	int	n, m;
	string	str;
	cin >> n >> m;
	vector<int> arr(m, 0);
	int	k = m;
	for (int i = 0; i < n; i++) {
		cin >> str;
		for (int j = 0; j < m; j++) {
			if (str[j] == 'O')
				arr[j] = 1;
		}
	}
	for (int i = 0; i < n; i++) {
		if (arr[i] == 0)
		{
			k = i;
			break;
		}
	}
	if (k != m)
		cout << k + 1 << "\n";
	else
		cout << "ESCAPE FAILED\n";
	return 0;
}
