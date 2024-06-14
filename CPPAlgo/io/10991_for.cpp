#include <iostream>

using namespace std;

int main(void)
{
  int n, j;

  cin >> n;
  for (int i = 0; i < n; i++) {
    for (j = 0; j < n - i - 1; j++) {
      cout << " ";
    }
    for (; j < n + i; j++) {
      if ((j + i + (n % 2)) % 2 == 1)
        cout << "*";
      else
        cout << " ";
    }
    cout << "\n";
  }
}
