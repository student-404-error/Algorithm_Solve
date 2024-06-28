#include <iostream>

using namespace std;

int main (int argc, char *argv[]) {
	int arr[5];
	for (size_t i = 0; i < 5; i++) {
		cin >> arr[i];
	}
	// A C    B D
	while (arr[1] > 0 || arr[2] > 0)
	{
		arr[1] -= arr[3];
		arr[2] -= arr[4];
		arr[0]--;
	}
	cout << arr[0] << '\n';
	return 0;
}
