import time
import os
import urllib.request
from tkinter import *
root = Tk()
root.title("Marker made by Calin Novogreblevschi.")
root.geometry("800x800")
version = "Alpha V2"
label = Label(root,text = "MARKER "+version)
label.pack()
bad_chars="[]',"
f = open("temp_update.py","w")
f.close()
os.remove("temp_update.py")
status_bar = Label(root, text="Updating data…", bd=1, relief=SUNKEN, anchor=W)
status_bar.pack(side=BOTTOM, fill=X)
data0 = urllib.request.urlretrieve("https://raw.githubusercontent.com/CREATORGAME19/MARKER/master/Version","V.txt")
v = open("V.txt")

if v.read().find(version) == -1:
    label = Label(root,text = "Update avaliable!")
    label.pack()
    status_bar.pack_forget()
    status_bar = Label(root, text="Downloading...", bd=1, relief=SUNKEN, anchor=W)
    status_bar.pack(side=BOTTOM, fill=X)
    data0 = urllib.request.urlretrieve("https://raw.githubusercontent.com/CREATORGAME19/MARKER/master/update.py","temp_update.py")
    print(os.system('temp_update.py'))
else:
    data = urllib.request.urlretrieve("https://raw.githubusercontent.com/CREATORGAME19/MARKER/master/Directory.txt","tasklist.txt")
    data1 = urllib.request.urlretrieve("https://raw.githubusercontent.com/CREATORGAME19/MARKER/master/task.txt","task.txt")
    status_bar.pack_forget()
    status_bar = Label(root, text="Done!", bd=1, relief=SUNKEN, anchor=W)
    status_bar.pack(side=BOTTOM, fill=X)
    os.system('cls' if os.name=='nt' else 'clear')
    f = open("tasklist.txt")
    d = open("task.txt")
    info1 = Label(root,text = "Here are the tasks: ")
    info1.pack()
    info2 = Label(root,text = f.read())
    info2.pack()
    info3 = Label(root,text = "Which task do you want to submit?: ")
    info3.pack()
    task = ""
    e = Entry(root, width=50)
    e.pack(side=TOP)
    ent_button = Button(root, text="Enter", width=10,command= lambda: next_button() )
    ent_button.pack(side=TOP)
    status_bar.pack_forget()



    def next_button():
        task = e.get()
        info1.pack_forget()
        info2.pack_forget()
        info3.pack_forget()
        e.destroy()
        ent_button.destroy()

        ent_button1 = Button(root, text="Next", width=10,command= lambda: task_dis() )
        ent_button1.pack(side=TOP)
        def task_dis():
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
            endexpecttask = d.read().find(str(task)+"//-END-//")
            d = open("task.txt")
            expectedoutput = d.read()[endinput+len(task)+2:endexpecttask]
            lines = 0
            info0 = Label(root,text = "Your task is: ")
            info0.pack()
            d = open("task.txt")
            info4 = Label(root,text = d.read()[tasknum:endtasktxt-1])
            info4.pack()
            info5 = Label(root,text = "Enter your python code: ")
            info5.pack()
            ent_button1.destroy()
            e = Entry(root, width=50)
            e.pack(side=TOP)
            ent_button = Button(root, text="Enter", width=10,command= lambda: lines_entered() )
            ent_button.pack(side=TOP)
            
            def lines_entered():
                code = e.get()
                e.destroy()
                ent_button.destroy()
                ent_button2 = Button(root, text="Next", width=10,command= lambda: analyse() )
                ent_button2.pack(side=TOP)
                def analyse():
                    ent_button2.destroy()
                    submit = []
                    a_submit = []
                    info5.destroy()
                    stat_input = 0
                    
                    submitappend = ""
                    for x in range(len(code)):
                        if code[x] == ";":
                            submit.append(submitappend)
                            submitappend = ""
                        else:
                            submitappend = str(submitappend)+str(code[x])
                        
                        def code_lines():
                            submitappend = e.get()
                            e.destroy()
                            ent_button.destroy()
                            info4.destroy()
                            info0.destroy()
                            
                    ent_button3 = Button(root, text="Next", width=10,command= lambda: rest() )
                    ent_button3.pack(side=TOP)
                    def rest():
                            a_submit = []
                            output = 0
                            received_input=0
                            stat_input = 0
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
                            
                            status_bar1 = Label(root, text="Done filtering!", bd=1, relief=SUNKEN, anchor=W)
                            status_bar1.pack(side=BOTTOM, fill=X)
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
                                    char1.append("END")
                                elif i_clock+len(str(task)) == i:
                                    a_task = False
                                    char1.append("END")
                            for i in range(len(char1)):
                                if char1[i] != "END":
                                    word1 = word1+char1[i]
                                else:
                                    words1.append(word1)
                                    word1 = ""
                            status_bar1.pack_forget()
                            status_bar1 = Label(root, text="Done filtering!(expected output)", bd=1, relief=SUNKEN, anchor=W)
                            status_bar1.pack(side=BOTTOM, fill=X)
                            mark = 0
                            total_marks = (len(words1)-1)+len(endinput_list)
                            print(words1)
                            print(words)
                            for i in range(len(words1)-1):
                                if words1[i] == words[i]:
                                    mark+=1
                            if received_input == len(endinput_list):
                                    mark+=received_input
                            status_bar1.pack_forget()
                            status_bar1 = Label(root, text="Cleaning up...", bd=1, relief=SUNKEN, anchor=W)
                            status_bar1.pack(side=BOTTOM, fill=X)
                            d.close()
                            f.close()
                            r.close()

                            os.remove("tasklist.txt")
                            os.remove("mark.py")
                            os.remove("output.txt")
                            status_bar1.pack_forget()
                            status_bar1 = Label(root, text="Done!", bd=1, relief=SUNKEN, anchor=W)
                            status_bar1.pack(side=BOTTOM, fill=X)
                            
                            ent_button3.destroy()
                            info5 = Label(root,text ="You got "+str(mark)+" out of "+str(total_marks))
                            info5.pack()
                        
                

      

    
root.mainloop()
