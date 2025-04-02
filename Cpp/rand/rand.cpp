#include <iostream>
#include <cstdlib> // rand(), srand()
#include <time.h> // time()
#include <windows.h> // Sleep()

using namespace std;

int main() {

	srand(time(0));

	while (true) {
		cout << (rand() % 6) + 1 << endl;
		Sleep(1000);
	}


	return 0;
}