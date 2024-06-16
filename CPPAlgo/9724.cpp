#include <iostream>
#include <cmath>

using namespace std;

int main (int argc, char *argv[]) {
  int n;
  int a, b;
  int cnt = 0;
  int arr[1260];

  for (int i = 0; i < 1260; i++) {
    arr[i] = i;
  }

  cin >> n;
  for (int i = 0; i < n; i++) {
    cin >> a >> b;
    cnt = (int)cbrt(b) - (int)cbrt(a);
    if (cbrt(a) == arr[(int)cbrt(a)])
      cnt += 1;
    cout << "Case #" << i + 1 << ": " << cnt << "\n";
  }
  return 0;
}
