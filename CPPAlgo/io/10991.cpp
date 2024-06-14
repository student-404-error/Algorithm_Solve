#include <iostream>

using namespace std;

int main(void)
{
  int n, i = 0, k = 0;

  cin >> n;
  while (i < n)
  {
    k = 0;
    while (k < n - i - 1)
    {
      cout << " ";
      k++;
    }
    while (k < n + i)
    {
      if ((k + i + (n % 2)) % 2 == 1)
        cout << "*";
      else
        cout << " ";
      k++;
    }
    cout << "\n";
    i++;
  }
}
