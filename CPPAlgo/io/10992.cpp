#include <iostream>

using namespace std;

int main(void)
{
  int n, i = 0, k = 0;

  cin >> n;
  while (i < n - 1)
  {
    k = 1;
    while (k < n - i - 1)
    {
      cout << " ";
      k++;
    }
    while (k < n + i + 1)
    {
      if (k == n - i || k == n + i)
        cout << "*";
      else
        cout << " ";
      k++;
    }
    cout << "\n";
    i++;
  }
  k = 0;
  while (k < n + i)
  {
    cout << "*";
    k++;
  }
  cout << "\n";
}
