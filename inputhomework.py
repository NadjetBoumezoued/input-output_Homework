#qst1
file=open("./student_names.txt") 
student=file.read()
print(student)
#qst2
student = student+"\njoe \nanne "
file=open("./student_names.txt","w")
file.write(student)
#qst3
file = open("./student_names.txt")
n = int(input("please enter the number of the first n line"))
for i in range(n):
    line = file.readline()
    print(line,end="")
#qst4
file = open("./student_names.txt")
n = int(input("please enter the number of the last n line"))
lines = file.readlines()[-n:]
print(lines)
#qst5
file = open("./student_names.txt")
student=file.read()
x = input("enter a name you want to search in file: ")
if(x in student):
    print("name found")
else:
    print("name not found")
#qst6
import string, os
if not os.path.exists("letters"):
   os.makedirs("letters")
for letter in string.ascii_uppercase:
   with open(letter + ".txt", "w") as f:
       f.writelines(letter)
