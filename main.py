#imports 


#functions

#handles input

def getMenuChoice():  
    print("Capacity?")
    capacity = int(input())
    seatsAvailable = capacity
    
    
    exit = False
    waitlist = []
    seated_list = []
    
    while(not exit):
        printMenu()
        foundInput = False
        user_input = input()

        user_input = user_input.lower()

        if(user_input == "1" or "add party" in user_input):
            foundInput = True
            waitlist = add_party(waitlist)

        if(user_input == "2" or "add vip" in user_input):
            foundInput = True
            waitlist = add_VIP_party(waitlist)

        if(user_input == "3" or "seat" in user_input):
            foundInput = True
            print("seat")
            waitlist, seated_list,seatsAvailable = seat_party(waitlist,seated_list,seatsAvailable)

        if(user_input == "4" or "clear" in user_input):
            foundInput = True
            print("clear")
            seated_list,seatsAvailable = clear_table(seated_list,seatsAvailable)

        if(user_input == "5" or "remove" in user_input):
            foundInput = True
            print("remove")
            waitlist = remove_party(waitlist)

        if(user_input == "6" or "print wait" in user_input):
            foundInput = True
            print_queue(waitlist)

        if(user_input == "7" or "print tables" in user_input):
            foundInput = True
            print("print tables")
            print_tables_seated(seated_list)

        if(user_input == "8" or "exit" in user_input):
            foundInput = True
            exit = True

        if(not foundInput):
            print("Unknown menu option.")
        
        
        print("")


def printMenu():
    print()
    print("(1) Add party to the queue.")
    print("(2) Add VIP party to the queue.")
    print("(3) Seat a party.")
    print("(4) Clear a table.")
    print("(5) Remove a party.")
    print("(6) Print wait queue.")
    print("(7) Print tables already seated.")
    print("(8) Exit.")

#takes in the existing waitlist and current capacity
#returns the waitlist with the party appended as a tuple
def add_party(waitlist):
    #get customers name
    customer_name = input("Please input customers name: ")
    #get customers party size
    party_size = input("Please input party size: ")
    #vip boolean
    vip = False
    #Puts party name, size, and vip boolean in tuple
    party = (customer_name,party_size, vip)
    #adds tuple to wait list
    waitlist.append(party)
    #returns wait list
    return(waitlist)

def add_VIP_party(waitlist):
    #get customers name
    customer_name = input("Please input customers name: ")
    #get customers party size
    party_size = input("Please input party size: ")
    #vip boolean
    vip = True
    #Puts party name, size, and vip boolean in tuple
    party = (customer_name,party_size, vip)
    
    #if there is another party in the waitlist, check through to see if its a VIP
    if(len(waitlist) > 0):
        #count is the index of how deep into the queue we look to find a non VIP group
        count = 0
        #we are going to iterate over all the parties in the waitlist
        for otherParty in waitlist:
            #if the party is not a VIP, inserts the new party into the list. If not, moves on to the next party and breaks out of the loop
            if(not otherParty[2]):
                waitlist.insert(count,party)
                break
            else:
                count = count + 1
    else:
        waitlist.append(party)
      

    #returns wait list
    return(waitlist)

def seat_party(waitlist,seated_list,seatsAvailable):

    if(len(waitlist) > 0):
        party = waitlist.pop()
        if(seatsAvailable > party[1]):
            print("Now seating " + party[0] + " party of " + party[1])
            seated_list.append(party)
            seatsAvailable = seatsAvailable - party[1]
        else:
            print("Can't seat "+party[0]+ " party of "+ party[1] +" until more tables are cleared.")
            waitlist.insert(0,party)
    else:
        print("No customers to seat")

    return waitlist,seated_list,seatsAvailable

def clear_table(seated_list,seatsAvailable):
    name = input("Input name of customer")
    found = False
    count = 0
    for party in seated_list:
        if(party[0] == name):
            found = True
            print("Clearning table for " + party[0] +" party of "+party[1])
            seated_list = seated_list.remove(seated_list[count])
            seatsAvailable = seatsAvailable + party[1]

        else:
            count = count + 1
    
    if(not found):
        print("No party by that name eating")

    return seated_list,seatsAvailable

       
def remove_party(waitlist):
    name = input("Input name of customer")
    found = False
    count = 0
    for party in waitlist:
        if(party[0] == name):
            found = True
            print("Removing " + party[0] +" party of "+party[1] + " from waitlist")
            waitlist = waitlist.remove(waitlist[count])

        else:
            count = count + 1
    
    if(not found):
        print("No party by that name waiting")

    return seated_list,seatsAvailable

def print_queue(waitlist):
    print("Waiting to be seated:")
    for party in waitlist:
        if(party[2]):
            print("   VIP " + party[0] + " party of "+party[1])
        else:
            print("   " + party[0] + " party of "+party[1])

def print_tables_seated(seated_list):
    print("Parties currently eating:")
    for party in seated_list:
        if(party[2]):
            print("   VIP " + party[0] + " party of "+party[1])
        else:
            print("   " + party[0] + " party of "+party[1])
    




getMenuChoice()