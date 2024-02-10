print("\n_.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._")
print("_.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._")
print("\n\tWelcome here")

# ADD Contact
def add():
    file = open("contact.txt", "a")
    name, phone, mail, address = "", "", "``", "``"
    # name input
    while(True):
        name = input("\nEnter contact name = ")
        name.strip()
        if(len(name) == 0):
            print("WARNING : Contact name can't be empty. Try again")
        else:
            break    
    # phone input
    while(True):
        phone = input("\nEnter mobile number = ")
        phone.strip()
        if(len(phone) == 0):
            print("WARNING : Mobile number can't be empty. Try again")
        else:
            break
    # mail input    
    mail = "`" + input("\nEnter contact mail = ") + "`"
    # address input
    address = "`" + input("\nEnter contact address = ") + "`"
    # writing into file
    file.write(name + "-" + phone + "-" + mail + "-" + address + "\n")
    print("\nRESULT : Your new contact is added")
    file.close()

# VIEW Contact List
def view():
    file = open("contact.txt", "a+")
    file.seek(0)
    li = file.readlines()
    if(len(li) > 0):
        print()
        # Printing 1st line with column name
        print(f"{'|'}{'-'*19}{'|'}{'-'*14}{'|'}{'-'*19}{'|'}{'-'*39}{'|'}")
        print("|{:^19}|{:^14}|{:^19}|{:^39}|".format("NAME","MOBILE","MAIL","ADDRESS"))
        print(f"{'|'}{'-'*19}{'|'}{'-'*14}{'|'}{'-'*19}{'|'}{'-'*39}{'|'}")
        # print(f"{'|'}{'-'*94}{'|'}")
    else:
        print("\nRESULT : Your contact book is empty")
        file.close()
        return
    for line in li:
        row = line.split('-')
        name = row[0]
        mobile = row[1]
        mail = row[2].strip('`')
        address = row[3].rstrip("\n").strip('`')
        # Printing all rows of records
        print("|{:^19}|{:^14}|{:^19}|{:^39}|".format(name, mobile, mail, address))
        print(f"{'|'}{'-'*19}{'|'}{'-'*14}{'|'}{'-'*19}{'|'}{'-'*39}{'|'}")
    file.close()

# SEARCH Contact List
def search():
    file = open("contact.txt", "a+")
    file.seek(0)
    target = input("\nEnter name or contact number to be searched = ").lower()
    li = file.readlines()
    find = 0
    if(not len(li)):
        print("\nRESULT : Your contact book is empty")
        file.close()
        return
    for line in li:
        row = line.split('-')
        if((target in row[0].lower()) or (target in row[1].lower())):
            find += 1
            name = row[0]
            mobile = row[1]
            mail = row[2].strip('`')
            address = row[3].rstrip("\n").strip('`')
            # Printing 1st line with column names for only single time
            if(find==1):
                print()
                print(f"{'|'}{'-'*19}{'|'}{'-'*14}{'|'}{'-'*19}{'|'}{'-'*39}{'|'}")
                print("|{:^19}|{:^14}|{:^19}|{:^39}|".format("NAME","MOBILE","MAIL","ADDRESS"))
                print(f"{'|'}{'-'*19}{'|'}{'-'*14}{'|'}{'-'*19}{'|'}{'-'*39}{'|'}")
            print("|{:^19}|{:^14}|{:^19}|{:^39}|".format(name, mobile, mail, address))
            print(f"{'|'}{'-'*19}{'|'}{'-'*14}{'|'}{'-'*19}{'|'}{'-'*39}{'|'}")
    if(find<1):
        print("\nRESULT : No record found with this input")
    file.close()

# UPDATE Contact List
def update():
    # Storing previous all records
    file = open("contact.txt", "a+")
    file.seek(0)
    li = file.readlines()
    count_total = len(li)
    file.close()
    if(not count_total):
        print("\nRESULT : Your contact book is empty")
        return
    # Replacing with new if found, else overwriting all records
    file = open("contact.txt", "w")
    target = input("\nEnter name or contact number to be updated = ")
    not_modify = 0
    for line in li:
        row = line.rstrip('\n').split('-')
        if(row[0]!=target and row[1]!=target):
            file.write(line)
            not_modify += 1
        else:
            # Same as ADD New Contact
            name, phone, mail, address = "", "", "``", "``"
            # name input
            while(True):
                name = input("\nEnter new contact name = ")
                name.strip()
                if(len(name) == 0):
                    print("WARNING : Contact name can't be empty. Try again")
                else:
                    break
            # phone input
            while(True):
                phone = input("Enter new mobile number = ")
                phone.strip()
                if(len(phone) == 0):
                    print("WARNING : Mobile number can't be empty. Try again")
                else:
                    break
            # mail input    
            mail = "`" + input("\nEnter new contact mail = ") + "`"
            # address input
            address = "`" + input("\nEnter new contact address = ") + "`"
            # writing into file
            file.write(name + "-" + phone + "-" + mail + "-" + address + "\n")
    if(count_total == not_modify):
        print("\nRESULT : No record found to be updated with given input")
    else:
        print("\nRESULT : Your existing contact list is updated")
    file.close()

# DELETE Contact
def delete():
    # Read everything initially
    file = open("contact.txt", "a+")
    file.seek(0)
    li = file.readlines()
    count_total = len(li)
    file.close()
    if(not count_total):
        print("\nRESULT : Your contact book is empty")
        return
    # Write everything except the user input
    file = open("contact.txt", "w")
    target = input("\nEnter name or contact number to be deleted = ").lower()
    not_delete = 0
    for line in li:
        row = line.rstrip('\n').split('-')
        if(row[0].lower()!=target and row[1].lower()!=target):
            not_delete += 1
            file.write(line);
    if(count_total == not_delete):
        print("\nRESULT : No record found to be deleted with given input")
    else:
        print("\nRESULT : The contact with given value is deleted successfully")
    file.close()


# _main_
quit = ""
while(len(quit)==0 or quit[0]=='y' or quit[0]=='Y'):
    print("\nPress :-",
            "\n\t1 -> for ADD Contact",
            "\n\t2 -> for VIEW Contact list",
            "\n\t3 -> for SEARCH in Conatct list",
            "\n\t4 -> for UPDATE in Contact list",
            "\n\t5 -> for DELETE in Contact list")
    ch = input("Enter your choice = ")
    # For any rubbish value
    if(ch.isdigit()==False):
        print("\nERROR : Choose from the list wisely")
        continue
    # ADD
    if(int(ch) == 1):
        add()

    # VIEW
    elif(int(ch) == 2):
        view()

    # SEARCH
    elif(int(ch) == 3):
        search()

    # UPDATE
    elif(int(ch) == 4):
        update()

    #DELETE
    elif(int(ch) == 5):
        delete()

    # No operation
    else:
        print("\nERROR : Choose from the list wisely")
    
    quit = input("\nWant to continue ? (Y/n) = ")
    print("\n_.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._")
    print("_.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._")
