#include <iostream>
#include <vector>
using namespace std;

long long score1=0, score2=0;

void display(vector<vector<char>> &arr, string &p1, char &ch1, string &p2, char &ch2){
	cout << endl << "\tNote :- " << ch1 << "'s :- " << p1;
	cout << endl << "\t        " << ch2 << "'s :- " << p2;
	cout << endl << endl;
    int num = 0;
	for(auto i=0; i<3; i++){
        cout << "\t";
        for(auto j=0; j<3; j++){
            ++num;
            if(arr[i][j] == ch1)
				cout << " " << ch1 << " ";
			else if(arr[i][j] == ch2)
				cout << " " << ch2 << " ";
			else
				cout << " " << num << " ";

			if(j != 2)
				cout << '|';
        }
        if(i != 2)
            cout << endl << "\t---|---|---" << endl;
    }
	cout << endl;
}

int ver_check(vector<vector<char>> &arr, char &ch){
	
	// _all vertical positions checking simultaneously_
	int count1 = 0, count2 = 0, count3 = 0;
	for(auto i=0; i<3; i++){
        if(arr[i][0] == ch)     ++count1;
        if(arr[i][1] == ch)     ++count2;
        if(arr[i][2] == ch)     ++count3;
    }

    if(count1==3 || count2==3 || count3==3)
        return 1;		
	return 0;
}

int hor_check(vector<vector<char>> &arr, char &ch){
	
	// _all horizontal positions checking simultaneously_
	vector<int> count(3,0);
	for(auto i=0; i<3; i++){
        for(auto j=0; j<3; j++){
            if(arr[i][j] == ch)
                ++count[i];
        }
    }

    if(count[0]==3 || count[1]==3 || count[2]==3)
        return 1;
	return 0;
}

int dia_check(vector<vector<char>> &arr, char &ch){
	
	// _both diagonal positions checking simultaneously_
    int count1 = 0, count2 = 0;
    for(auto i=0; i<3; i++){
        if(arr[i][i] == ch)     ++count1;
        if(arr[i][2-i] == ch)   ++count2;
    }

    if(count1==3 || count2==3)
        return 1;
	return 0;
}

int match_result(vector<vector<char>> &arr, char &ch){
	if(ver_check(arr, ch) == 0){
		if(hor_check(arr, ch) == 0){
			if(dia_check(arr, ch) == 0){
				return 0;
            }
			else
				return 1;
		}
		else
			return 1;
	}
	else
		return 1;
}

void TicTacToe(vector<vector<char>> &arr){
	
	string p1, p2;
    char ch1, ch2;
	int p1_ind, p2_ind, win=0, board_fill=0;
	
	cout << endl << "    Note :- Player-1 will start the game always";
	cout << endl << "            So, enter the players name accordingly\n";
	
	cout << endl << "Enter player-1 name = ";
	getline(cin, p1);
	cout << "Enter player-2 name = ";
	getline(cin, p2);
	cout << endl;
	
	// _Player-1 character entry untill valid character found_
	for(int i=1; i>0; i++){
		cout << "Enter player-1 choice (X or O) = ";
		cin >> ch1;
		fflush(stdin);
		ch1 = toupper(ch1);
		if(ch1=='x' || ch1=='X' || ch1=='o' || ch1=='O')
			break;
		else
			cout << "WARNING! = Only X or O is accepted. Enter again to continue.\n" << endl;
	}

	
	// _Player-2 character have to be alternate_
	ch1 == 'X' ? ch2 = 'O' : ch2 = 'X';
	cout << "Now player-2 choice is = " << ch2 << endl;
	
	// Initially
	display(arr, p1, ch1, p2, ch2);
	cout << endl << "REMARKS :- Start the match" << endl;
	
	while( win!=1 ){		
		
		// _1st player's mark entry untill valid mark found_
		for(int i=1; i>0; i++){
			cout << endl << p1 << "'s turn : Enter any integer shown to put your mark = ";
			cin >> p1_ind;
			fflush(stdin);
			--p1_ind;
			if(p1_ind>=0 && p1_ind<=8 && arr[p1_ind/3][p1_ind%3]==0){		// Already vacant, so accepted
				arr[p1_ind/3][p1_ind%3] = ch1;
				break;
			}				
			else if(p1_ind>=0 && p1_ind<=8 && arr[p1_ind/3][p1_ind%3]!=0)	// Not vacant, so taking input again
				cout << "Enter only the vacant place that doesn't contain any previous mark" << endl;
			else
				cout << "WARNING! = Enter only among the numbers shown" << endl;
		}
		board_fill += 1;
		display(arr, p1, ch1, p2, ch2);					// Print game baord after every mark entered
		win = match_result(arr, ch1);					// Deciding if player-1 wins immediately or not
        cout << endl << "REMARKS :- ";
		if(win==1){
			cout << "Congratulations, " << p1 << " has won the game" << endl;
			++score1;
			return;
		}
		else if(board_fill==9){
			cout << "Match DRAW" << endl;
			return;
		}
        else
            cout << "Hold on your breath, match is ongoing" << endl;
		
		
		// _2nd player's mark entry untill valid mark found_
		for(int i=1; i>0; i++){
			cout << endl << p2 << "'s turn : Enter any integer shown to put your mark = ";
			cin >> p2_ind;
			fflush(stdin);
			--p2_ind;
			if(p2_ind>=0 && p2_ind<=8 && arr[p2_ind/3][p2_ind%3]==0){		// Already vacant, so accepted
				arr[p2_ind/3][p2_ind%3] = ch2;
				break;
			}				
			else if(p2_ind>=0 && p2_ind<=8 && arr[p2_ind/3][p2_ind%3]!=0)	// Not vacant, so taking input again
				cout << "Enter only the vacant place that doesn't contain any previous mark" << endl;
			else
				cout << "WARNING! = Enter only among the numbers shown" << endl;
		}
		board_fill += 1;
		display(arr, p1, ch1, p2, ch2);					// Print game baord after every mark entered
		win = match_result(arr, ch2);					// Deciding if player-2 wins immediately or not
        cout << endl << "REMARKS :- ";
		if(win==1){
			cout << "Congratulations, " << p2 << " has won the game" << endl;
			++score2;
			return;
		}
		else if(board_fill==9){
			cout << "Match DRAW" << endl;
			return;
		}
        else
            cout << "Hold on your breath, match is ongoing" << endl;
	}
}

int main(){
    string quit;
	
	cout << endl;
	cout << "\t        Welcome to Tic Tac Toe game\n";
	cout << "\t       Let's start and have some fun\n";
	
	// _Start_
	while( quit.size()==0 || quit[0]=='y' || quit[0]=='Y' ){
		
		// For every new game 3x3 matrix will be allocated
		vector<vector<char>> arr(3, vector<char>(3, 0));
		
		TicTacToe(arr);
		
		// Exit block
		cout << endl << "Want to play another game ? (Y/n) = ";
		getline(cin, quit);

        // clearing the matrix memory blocks after every game round
        arr.clear();
        arr.shrink_to_fit();
		
	}
	
	cout << endl <<"Come back again. Have a nice day" << endl;

    return 0;
}