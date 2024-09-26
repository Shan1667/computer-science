print("1) create a new file")
print("2) display the file")
print("3) add a new item to the file")
user = input("please choose a number to make a selection:")
if "1" in user:
    subject = open("C:\\Users\\20SShahid.ACC\\Downloads\\subject.txt\\subject.txt","r")
    choice = input("Please enter a school subject:")
    school = subject.read()
    print(school)
    
    