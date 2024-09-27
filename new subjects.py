print("1) create a new file")
print("2) display the file")
print("3) add a new item to the file")
user = input("please choose a number to make a selection:")
if "1" in user:
    sub = input("please enter the subject's name:")
    subject = open("C:\\Users\\20SShahid.ACC\\Downloads\\subject.txt\\"+sub+".txt","w")
    subject.write(sub)
    subject.close()
    print(sub)
    
if "2" in user:
    sub = open("C:\\Users\\20SShahid.ACC\\Downloads\\subject.txt\\"+sub+".txt","r")
    x = content.read()
    print(x)
    
if "3" in user:
    new = input("please enter a new subject's name:")
    new_subjects = open("C:\\Users\\20SShahid.ACC\\Downloads\\subject.txt\\"+new+".txt","w")
    new_subjects.write(new)
    new_subjects.close()
    print(new)
    