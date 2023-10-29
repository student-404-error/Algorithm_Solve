#include <iostream>

using namespace std;

int main()
{
	int s, e;
	int a[3];
	int b[3];
	int result[3];
	int work;
	for(int i = 0; i<3; i++)
	{
		cin >> a[0] >> a[1] >> a[2] >> b[0] >> b[1] >> b[2];
		
		s = a[0] * 3600 + a[1] * 60 + a[2];
		e = b[0] * 3600 + b[1] * 60 + b[2];
		
		work = e - s;
		result[0] = work / 3600;
		work = work % 3600;
		result[1] = work / 60;
		work = work % 60;
		result[2] = work;
		cout << result[0] << " " << result[1] << " " << result[2] << "\n";
	}
	return 0;
}
