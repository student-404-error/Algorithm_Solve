#include <iostream>

using namespace std;

int	main(void)
{
	int	n;
	int M[2];

	cin >> n;
	int	arr[n];
	for (int i = 0; i < n; i++)
		cin >> arr[i];
	M[0] = M[1] = arr[0];
	for (int i = 1; i < n; i++)
	{
		if (M[0] > arr[i])
			M[0] = arr[i];
		if (M[1] < arr[i])
			M[1] = arr[i];
	}
	cout << M[0] << " "  << M[1] << "\n";
	return 0;
}
