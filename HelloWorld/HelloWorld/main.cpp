#include <iostream>

using namespace std;

int main()
{
    int age;

    cout << "How old are you?" << endl;
    cin >> age;


   if ( 18 > age)
   {
        cout << "You're not pe³noletni"<< endl;
   } else
   {
        cout << "you're pe³noletni"<< endl;
        if(age >= 35)
        {
            cout << "You can be a president"<< endl;
        }
   }






    return 0;

}


