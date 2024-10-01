#include <iostream>

using namespace std;


class Employee {

public:
    string mName;
    string mCompany;
    int mAge;

    Employee(string name, string company, int age) : mName(name), mCompany(company), mAge(age) {}


    void introduceYourself() {
        cout << "Name: " << mName << endl;
    }
};

int main()
{
    Employee e = Employee("Adam", "MS", 27);
    Employee e2 = Employee("Mateusz", "MS", 27);

    e.introduceYourself();
    e2.introduceYourself();

}


