import os
import urllib.request
print("Marker made by Calin Novogreblevschi.")
version = "Alpha V1"
print(version)
bad_chars="[]',"
os.remove("temp_update.py")
print("Updating data...")
data0 = urllib.request.urlretrieve("https://raw.githubusercontent.com/CREATORGAME19/MARKER/master/Version","V.txt")
v = open("V.txt")
if v.read() != version:
    print("Update avaliable!")
    print("Downloading...")
    data0 = urllib.request.urlretrieve("https://raw.githubusercontent.com/CREATORGAME19/MARKER/master/update.py","temp_update.py")
    print(os.system('temp_update.py'))
else:
    data = urllib.request.urlretrieve("https://raw.githubusercontent.com/CREATORGAME19/MARKER/master/Directory.txt","tasklist.txt")
    data1 = urllib.request.urlretrieve("https://raw.githubusercontent.com/CREATORGAME19/MARKER/master/task.txt","task.txt")
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
    endtasktxt = d.read().find(str(task)+"`")
    d = open("task.txt")
    endinput = d.read().find(str(task)+"@")
    d = open("task.txt")
    enteredinput = d.read()[endtasktxt+2:endinput]
    endinput_list = []
    char_input = []
    insertend = False
    word_input = ""
    for i in range(len(enteredinput)):
        if enteredinput[i].find(",") == -1:
            char_input.append(enteredinput[i])
            insertend = True
        elif insertend == True:
            insertend = False
            char_input.append("END")
    for i in range(len(char_input)):
        if char_input[i] != "END":
            word_input = word_input+char_input[i]
        else:
            endinput_list.append(word_input)
            word_input = ""
    d = open("task.txt")
    d = open("task.txt")
    print("Your task is: ")
    print(d.read()[tasknum:endtasktxt])
    d = open("task.txt")
    endexpecttask = d.read().find("//-END-//"+str(task))
    d = open("task.txt")
    expectedoutput = d.read()[endinput+len(task)+2:endexpecttask-3]
    lines = int(input("How many lines are in your python code: "))
    submit = []
    a_submit = []
    output = 0
    stat_input = 0
    received_input=0
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
        elif submit[i].find("input(") != -1:
            code = submit[i]
            find = submit[i].find("input(")
            value = code[:find-1]
            a_submit.append(value+str(endinput_list[stat_input]))
            stat_input += 1
            received_input += 1
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
    a_task = False
    for i in range(len(expectedoutput)):
        d = open("task.txt")
        if not expectedoutput[i] == "~" and a_task == False:
            char1.append(expectedoutput[i])
            insertend1 = True
        elif insertend1 == True:
            insertend1 = False
            a_task = True
            i_clock = i
        elif i_clock+len(str(task)) == i:
            a_task = False
            char1.append("END")
    for i in range(len(char1)):
        if char1[i] != "END":
            word1 = word1+char1[i]
        else:
            words1.append(word1)
            word1 = ""
    print("Done filtering!(expected output)")
    mark = 0
    total_marks = len(words1)+len(endinput_list)
    for i in range(len(words1)):
        if words1[i] == words[i]:
            mark+=1
    if received_input == len(endinput_list):
        mark+=received_input
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

