print("\n_.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._")
print("\n\tWelcome here")
quit=""

while(len(quit)==0 or quit[0]=='y' or quit[0]=='Y'):
    a = float(input("\nEnter your 1st number = "))
    b = float(input("\nEnter your 2nd number = "))
    print()

    print("Press :-\n",
            "\t1 -> for Addition\n",
            "\t2 -> for Subtraction\n",
            "\t3 -> for Multiplication\n",
            "\t4 -> for Division")
    ch = input("Enter your choice = ")
    print()
    
    if(ch.isdigit()):
        # Addition
        if(int(ch) == 1):
            print(f"\tResult for ({a}  +  {b}) = {a+b}")
            print()

        # Subtraction
        elif(int(ch) == 2):
            print(f"\tResult for ({a}  -  {b}) = {a-b}")
            print()
            print(f"\tResult for ({b}  -  {a}) = {b-a}")
            print()

        # Multiplication
        elif(int(ch) == 3):
            print(f"\tResult for ({a}  x  {b}) = {a*b}")
            print()

        # Division
        elif(int(ch) == 4):
            if(a==0 and b==0):
                print(f"\tSorry, both numbers are 0 and can't be divided")
                print()
            else:
                if(b != 0):
                    print(f"\tResult for ({a}  /  {b}) = {a/b}")
                    print()
                else:
                    print(f"\tSorry, {a} can't be divided by {b}")
                    print()
                
                if(a != 0):
                    print(f"\tResult for ({b}  /  {a}) = {b/a}")
                    print()
                else:
                    print(f"\tSorry, {b} can't be divided by {a}")
                    print()

        # Not from the operation list
        else:
            print(f"\tERROR :- No such operation code found. Try Again")
            print()
    # Any random input found
    else:
        print(f"\tERROR :- No such operation code found. Try Again")
        print()
        continue

    quit = input("Want to continue ? (Y/n) = ")
    
    print("\n_.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._")