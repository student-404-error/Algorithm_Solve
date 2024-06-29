#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

int main (int argc, char *argv[]) {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N, M;
	int	cnt = 0;

	cin >> N >> M;
	set<string>	no_listen;
	set<string>	result;
	string			comp;
	set<string>::iterator iter;
	for (int i = 0; i < N; i++)
	{
		cin >> comp;
		no_listen.insert(comp);
	}
	for (int i = 0; i < M; i++) {
		cin >> comp;
		if (no_listen.count(comp) == 1){
			result.insert(comp);
		}
	}
	cout << result.size() << '\n';
	for (iter = result.begin(); iter != result.end(); iter++) {
		cout << *iter << '\n';
	}
	// for(string var : result) {
	// 	cout << var << '\n';
	// }
	return 0;
}
