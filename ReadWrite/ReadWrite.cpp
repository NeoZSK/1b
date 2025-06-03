
#include <fstream>
#include <iostream>
#include <string>

using namespace std;

int main()
{
    fstream file("numbers.txt", ios::in);
    string line;
    int sum = 0;


    if (!file.is_open()) {
        cerr << "err: cannot open file " << endl;
        return 1;
    }


    while (getline(file, line)) {
        cout << line << endl;
        sum += stoi(line);
    }

    file.close();
    
    cout << "sum is: " << sum << endl;
}
