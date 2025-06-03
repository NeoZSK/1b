#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
    fstream inFile("numbers.txt", ios::in);
    fstream outFile("results.txt", ios::out);
    string line;
    int sum = 0;

    if(!inFile.is_open() or !outFile.is_open())
    {
        cout << "error: cannot open one or more files" << endl;
        return 1;
    }

    while (getline(inFile, line)) {
        int newValue = stoi(line) - 10;

        outFile << newValue << endl;
    }

    outFile.close();
    inFile.close();
}
