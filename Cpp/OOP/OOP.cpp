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


class Teacher : public Employee {
    int teachingYears;

    Teacher(string name, string company, int age, int years) : Employee(name, company, age), teachingYears(years) {

    }


};

int main()
{
    Employee e = Employee("Adam", "MS", 27);
    Employee e2 = Employee("Mateusz", "MS", 27);

    Teacher t = Teacher("Aasd", "ZSK", 29, 1);

    e.introduceYourself();
    e2.introduceYourself();

}


