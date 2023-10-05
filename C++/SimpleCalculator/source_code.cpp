#include <iostream>
using namespace std;

int main(){
    cout << endl << "_.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._" << endl;
    
    cout << endl << "\tWelcome here" << endl;
    long double a, b;
    string quit;
    int ch;

    while( quit.size()==0 || quit[0]=='y' || quit[0]=='Y' ){
        
        cout << endl << "Enter your 1st number = ";
        cin >> a;
        fflush(stdin);

        cout << "Enter your 2nd number = ";
        cin >> b;
        fflush(stdin);

        cout << "Press :-" << endl;
        cout << "\t1 -> for Addition" << endl <<
                "\t2 -> for Subtraction" << endl <<
                "\t3 -> for Multiplication" << endl <<
                "\t4 -> for Division" << endl;
        cout << "Enter your choice number = ";
        cin >> ch;
        fflush(stdin);
        cout << endl;

        // Addition
        if(ch == 1)
            cout << "\tResult for (" << a << "  +  " << b << ") = " << a+b << endl << endl;

        // Subtraction
        else if(ch == 2){
            cout << "\tResult for (" << a << "  -  " << b << ") = " << a-b << endl << endl;
            cout << "\tResult for (" << b << "  -  " << a << ") = " << b-a << endl << endl;
        }

        // Multiplication
        else if(ch == 3)
            cout << "\tResult for (" << a << "  x  " << b << ") = " << a*b << endl << endl;

        // Division
        else if(ch == 4){
            if(a == 0 && b == 0)
                cout << "\tSorry, both numbers are 0 and can't be divided" << endl << endl;
            else{
                if(b != 0)
                    cout << "\tResult for (" << a << "  /  " << b << ") = " << a/b << endl << endl;
                else
                    cout << "\tSorry, " << a << " can't be divided by 0" << endl << endl;
                
                if(a != 0)
                    cout << "\tResult for (" << b << "  /  " << a << ") = " << b/a << endl << endl;
                else
                    cout << "\tSorry, " << b << " can't be divided by 0" << endl << endl;
            }
        }

        // No operation
        else
            cout << "\tERROR :- No such operation code found. Try Again" << endl << endl;

        cout << "Want to continue ? (Y/n) = ";
		getline(cin, quit);

        cout << endl << "_.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._" << endl;
    }

    return 0;
}