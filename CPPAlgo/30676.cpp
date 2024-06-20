#include <iostream>
#include <string>

using namespace std;
	
int main (int argc, char *argv[]) {
	int n;
	string result;

	cin >> n;
	if (n >= 380 && n < 425)
		result = "Violet";
	else if (n >= 425 && n < 450) {
		result = "Indigo";
	}
	else if (n >= 450 && n < 495) {
		result = "Blue";
	}
	else if (n >= 495 && n < 570) {
		result = "Green";
	}
	else if (n >= 570 && n < 590) {
		result = "Yellow";
	}
	else if (n >= 590 && n < 620) {
		result = "Orange";
	}
	else if (n >= 620 && n <= 780) {
		result = "Red";
	}
	cout << result << "\n";
	return 0;
}
