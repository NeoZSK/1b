
#include <iostream>
#include <string>

using namespace std;

int multiplyByTwo(int x) {
	return x * 2;
}

int add(int a, int b) {
	a = a * 2;
	return a + b;
}


string merge(string niewiem, string niewiem2) {
	return niewiem + niewiem2;
}

int main()
{
	string result;
	result = merge("krzeslo", "aura");
	cout << result;

	return 0;
}





//int -> 10
//string -> "aura"
