#include <iostream>

using namespace std;

void Minus(const int x, const int y)
{
	cout << "X - Y = " << x - y << endl;
}

int Plus(const int x, const int y)
{
	return x+y;
}

int main()
{
	Minus(10, 5);
	cout<<Plus(2, 6)<<endl;

	return 0;
}
