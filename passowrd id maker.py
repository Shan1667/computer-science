print("1) Create a new user ID")
print("2) Change a passowrd")
print("3) Display all user IDs")
print("4) Quit")
#password = open("C:\\Users\\20SShahid.ACC\\Downloads\\password ID.txt\\"+menu+".txt","w")
menu = input("please enter a number to choose an option:")
ID = input("please enter a users ID:")
if ID in ID:
    print("you have enterred the ID",ID)
    
    
#password = open("C:\\Users\\20SShahid.ACC\\Downloads\\password ID.txt\\"+menu+".txt","w")
if "1" in menu:
    password = open("C:\\Users\\20SShahid.ACC\\Downloads\\"+menu+".csv","r")
    password.write(menu)
    password.close()
    print(menu)
    
#print("please enter a password including the following. \n it should have at least 8 character \n it should include upper case letters \n it should include lower case letters \n it should include numbers \n it should include one special character !,£,$,%,&,*,# \n")
passowrd_change = input("please enter the passowrd:")