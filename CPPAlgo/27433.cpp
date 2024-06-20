#include <iostream>

using namespace std;

int main(void)
{
    unsigned long long n;
    cin >> n;
	if (n == 0)
		n = 1;
    for (int i = n - 1; i > 1; i--)
        n = n * i;
    cout << n << "\n";
}
