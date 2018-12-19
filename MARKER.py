import os
import urllib.request
print("Marker made by Calin Novogreblevschi.")
print("Beta V1.0")
bad_chars="[]',"
print("Updating data...")
data = urllib.request.urlretrieve("https://computedigit.000webhostapp.com/Directory.txt","tasklist.txt")
data1 = urllib.request.urlretrieve("https://computedigit.000webhostapp.com/task.txt","task.txt")
print("Done!")
os.system('cls' if os.name=='nt' else 'clear')
f = open("tasklist.txt")
d = open("task.txt")
print("These are the tasks:")
print(f.read())
task = input("Which task do you want to submit?: ")
d = open("task.txt")
tasknum = d.read().find(task) + 1
d = open("task.txt")
endtasktxt = d.read().find("`")
d = open("task.txt")
endinput = d.read().find("@")
d = open("task.txt")
enteredinput = d.read()[endtasktxt+2:endinput-1]
print(enteredinput)
d = open("task.txt")
print("Your task is: ")
print(d.read()[tasknum:endtasktxt])
d = open("task.txt")
endexpecttask = d.read().find("//-END-//")
d = open("task.txt")
expectedoutput = d.read()[endinput+2:endexpecttask-1]
lines = int(input("How many lines are in your python code: "))
submit = []
a_submit = []
output = 0
for x in range(lines):
    y = x+1
    submit.append(input("Enter line "+str(y)+" of your code: "))
for i in range(len(submit)):
    if submit[i].find("print(") != -1:
        code = submit[i]
        find = submit[i].find("print(")
        value = code[find+6:-1]
        if output > 0:
            a_submit.append("output.append("+str(value)+")")
        else:
            a_submit.append("output = ["+str(value)+"]")
        output+=1
file = open("mark.py", "w")
file.write(a_submit[0])
file.close()
for i in range(len(a_submit)-1):
    file = open("mark.py", "a")
    file.write('\n'+a_submit[i+1])
    file.close()
file1 = open("mark.py", "a")
file1.write('\n'+"with open(\"output.txt\", \"w\") as f:")
file1.close()
print("Testing...")
file2 = open("mark.py", "a")
file2.write('\n'+"  "+"f.write(str(output))")
file2.close()
print("Test program created!")
print("Running...")
print(os.system('mark.py'))
print("Attempting to gather output data...")
r = open("output.txt")
print("Gathered successfully!")
print("Marking...")
char = []
char1 = []
insertend = False
insertend1 = False
words = []
words1 = []
word = ""
word1 = ""
for i in range(len(r.read())):
    r = open("output.txt")
    if bad_chars.find(r.read()[i]) == -1:
        r = open("output.txt")
        char.append(r.read()[i])
        r = open("output.txt")
        insertend = True
    elif insertend == True:
        insertend = False
        char.append("END")

for i in range(len(char)):
    if char[i] != "END":
        word = word+char[i]
    else:
        words.append(word)
        word = ""
print("Done filtering!")
d = open("task.txt")
for i in range(len(expectedoutput)):
    d = open("task.txt")
    if not expectedoutput[i] == "~":
        char1.append(expectedoutput[i])
        insertend1 = True
    elif insertend1 == True:
        insertend1 = False
        char1.append("END")
for i in range(len(char1)):
    if char1[i] != "END":
        word1 = word1+char1[i]
    else:
        words1.append(word1)
        word1 = ""
print("Done filtering!(expected output)")
mark = 0
total_marks = len(words1)
for i in range(len(words1)):
    if words1[i] == words[i]:
        mark+=1
print("Cleaning up...")
d.close()
f.close()
r.close()
os.remove("task.txt")
os.remove("tasklist.txt")
os.remove("mark.py")
os.remove("output.txt")
print("Done!")
print("You got",mark,"out of",total_marks)

