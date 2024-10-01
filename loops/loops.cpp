
#include <iostream>
using namespace std;

int main()
{
    int h = 5;
    
    for (int i = 0; i < h; i++) {
        cout << "[";
        cout << i;
        cout << "] ";
        cout << "Hello World!\n";
    }

    int j = 0;
    while (j < 10) {
        cout << "[";
        cout << j;
        cout << "] ";
        cout << "Hello While!\n";

        j++;
    }

    return 0;
}

