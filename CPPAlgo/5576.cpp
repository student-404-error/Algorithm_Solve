#include <iostream>
#include <numeric>
#include <vector>

using namespace std;

int	main(void)
{
	int	n;

	vector<int>	w(3, 0), k(3, 0);
	for (int i = 0; i < 10; i++)
	{
		cin >> n;
		for (int j = 0; j < 3; j++)
		{
			if (w[j] < n)
				swap(w[j], n);
		}
	}
	for (int i = 0; i < 10; i++)
	{
		cin >> n;
		for (int j = 0; j < 3; j++)
		{
			if (k[j] < n)
				swap(k[j], n);
		}
	}
	cout << accumulate(w.begin(), w.end(), 0) << " " << accumulate(k.begin(), k.end(), 0) << "\n";
}
