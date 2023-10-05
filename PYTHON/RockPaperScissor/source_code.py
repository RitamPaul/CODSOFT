import random
from pyfiglet import figlet_format

# 1 means ROCK
# 2 means PAPER
# 3 means SCISSOR

dict_c = {1:'ROCK', 2:'PAPER', 3:'SCISSOR'}
#dict_c = dictionary for convention

dict_r = {'12':2, '21':2,
        '13':1, '31':1,
        '23':3, '32':3}
#dict_r = dictionary that determines result

cuser, ccomp = 0, 0
#count for user win, computer win

#__main__

print("\n_.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._")
print("\n\tWelcome here")

while(1):
    print("\nPress :- ",
          "\n\t1 for ROCK",
          "\n\t2 for PAPER",
          "\n\t3 for SCISSOR",
          "\n\tany other to exit.")
    a=input("Enter your choice = ")    #_User input_

    if(a.isdigit() and int(a)<4 and int(a)>0):
        b=random.randint(1,3)               #_Computer input_
        print("\nComputer chooses = ", dict_c[b])
        
        if(str(a)==str(b)):                 #_Case: Draw
            print("\nSTATUS :- Draw happened.")
            
        else:
            final = dict_r[a+str(b)]
            
            if(final==int(a)):                   #_Case: User wins_
                print("\nSTATUS :- You win...")
                cuser += 1
                
            else:                           #_Case: Computer wins_
                print("\nSTATUS :- Computer wins, better luck next time.")
                ccomp += 1
        
        print("\n\tCurrent scorecard")
        print(figlet_format(f"Computer-{ccomp}  You-{cuser}", font="digital"))
                
        choice = input("Want to play more ? (Y/n) = ")
        print("\n_.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._")
        if(len(choice)==0 or choice[0]=='y' or choice[0]=='Y'):         #_Game continues_
            continue
        break
        
    else:                                   #_Exiting game as invalid input found_
        print("\n_.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._")
        break
