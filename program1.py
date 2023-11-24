adding = print 
f = open("C:\\Users\\20SShahid.ACC\\Desktop\\files\\numbers.txt",'r')
for line in f:
     line = line.strip()
     if(len(line)!=0):
         a =int(line)
         print(a)