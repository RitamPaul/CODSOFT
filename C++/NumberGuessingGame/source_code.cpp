#include <iostream>
using namespace std;

int main(){
    cout << endl << "_.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._" << endl;
    
    cout << endl << "\t\tWelcome here" << endl << endl;
    string quit;
    while( quit.size()==0 || quit[0]=='y' || quit[0]=='Y' ){
        
        // user input of how many digit random number should be generated
        int dig, lim=1, close=1, guess;
        cout << "Enter no. of digits to generate the number (<10) = ";
        cin >> dig;
        cout << endl;
        fflush(stdin);

        // range of closeness of user guessed data & generated random data
        for(auto i=1; i<=dig/2; i++)
            close = close * 10;
        
        // range of randomly generated number as per user
        while(dig--)
            lim = lim * 10;
        
        // generating the random number
        int num = rand() % lim;
        cout << "Number is generated" << endl << endl;

        while(true){
            cout << "Guess the number = ";
            cin >> guess;
            fflush(stdin);

            if(guess == num)
                break;
            if(abs(num-guess) <= close)
                cout << "REMARKS :- You guess is close. Try again" << endl << endl;
            else if(guess < num)
                cout << "REMARKS :- You guess is too low" << endl << endl;
            else if(guess > num)
                cout << "REMARKS :- You guess is too high" << endl << endl;
        }

        cout << "Congratulation! you have guessed the number correctly" << endl << endl;

        cout << "Want to continue ? (Y/n) = ";
		getline(cin, quit);

        cout << endl << "_.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._" << endl << endl;

    }

    return 0;
}