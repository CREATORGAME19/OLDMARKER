from tkinter import font
import time
import os
import urllib.request
from tkinter import *
import random
from tkinter import messagebox
root = Tk()
root.title("Marker made by Calin Novogreblevschi.")
root.geometry("800x500")
version = "Alpha V2.4"

label = Label(root,text = "MARKER "+version)
label.pack()
bad_chars="[]',"
f = open("temp_update.py","w")
f.close()
os.remove("temp_update.py")
f = open("V.txt","w")
f.close()
os.remove("V.txt")
f = open("tasklist.txt","w")
f.close()
os.remove("tasklist.txt")
f = open("task.txt","w")
f.close()
os.remove("task.txt")
data0 = urllib.request.urlretrieve("https://raw.githubusercontent.com/CREATORGAME19/MARKER/master/Version","V.txt")
c_change = data0 = urllib.request.urlretrieve("https://raw.githubusercontent.com/CREATORGAME19/MARKER/master/MARKER.py","ex.txt")
pr2 = open("ex.txt")
v = open("V.txt")
pr = open("MARKER.py")
if v.read().find(version) == -1 :
    label = Label(root,text = "Update avaliable!")
    label.pack()
    status_bar = Label(root, text="Downloading...", bd=1, relief=SUNKEN, anchor=W)
    status_bar.pack(side=BOTTOM, fill=X)
    data0 = urllib.request.urlretrieve("https://raw.githubusercontent.com/CREATORGAME19/MARKER/master/update.py","temp_update.py")
    pr.close()
    print(os.system('temp_update.py'))
    label2 = Label(root,text = "You may close the window now!")
    label2.pack()
    v.close()
    pr2.close()
    os.remove("V.txt")
    os.remove("ex.txt")
elif pr.read() != pr2.read():
    label = Label(root,text = "Error: Illegal modification detected! This program will reinstall!")
    label.pack()
    status_bar = Label(root, text="Downloading...", bd=1, relief=SUNKEN, anchor=W)
    status_bar.pack(side=BOTTOM, fill=X)
    data0 = urllib.request.urlretrieve("https://raw.githubusercontent.com/CREATORGAME19/MARKER/master/update.py","temp_update.py")
    pr.close()
    print(os.system('temp_update.py'))
    label2 = Label(root,text = "You may close the window now!")
    label2.pack()
    v.close()
    pr2.close()
    os.remove("V.txt")
    os.remove("ex.txt")
else:
    pr2.close()
    os.remove("ex.txt")
    info1 = Label(root,text = "What is your four digit school code?: ")
    info1.pack()
    e = Entry(root, width=50)
    e.pack(side=TOP)
    ent_button = Button(root, text="Enter", width=10,command= lambda: find_school() )
    ent_button.pack(side=TOP)
    def find_school():
        global status_bar
        status_bar = Label(root, text="Updating data…", bd=1, relief=SUNKEN, anchor=W)
        status_bar.pack(side=BOTTOM, fill=X)
        school = e.get()
        e.destroy()
        info1.destroy()
        ent_button.destroy()
        data = urllib.request.urlretrieve("https://raw.githubusercontent.com/CREATORGAME19/MARKER/master/"+school+"Directory.txt","tasklist.txt")
        data1 = urllib.request.urlretrieve("https://raw.githubusercontent.com/CREATORGAME19/MARKER/master/"+school+"task.txt","task.txt")
        status_bar.destroy()
        status_bar = Label(root, text="Done!", bd=1, relief=SUNKEN, anchor=W)
        status_bar.pack(side=BOTTOM, fill=X)
        done()

    def done():
        f = open("tasklist.txt")
        d = open("task.txt")
        global info1
        global info2
        global info3
        info1 = Label(root,text = "Here are the tasks: ")
        info1.pack()
        info2 = Label(root,text = f.read())
        info2.pack()
        info3 = Label(root,text = "Which task do you want to submit?: ")
        info3.pack()
        task = 0
        global e
        e = Entry(root, width=50)
        e.pack(side=TOP)
        global ent_button
        ent_button = Button(root, text="Enter", width=10,command= lambda: del_task() )
        ent_button.pack(side=TOP)
        
    def del_task():
        global task
        task = int(e.get())
        e.destroy()
        ent_button.destroy()
        task = str(task)
        task_dis()
        
    def task_dis():
        
        info1.pack_forget()
        info2.pack_forget()
        info3.pack_forget()
        d = open("task.txt")
        tasknum = d.read().find(str(task)) + 1
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
        info4 = Label(root,text = d.read()[tasknum+(len(str(task))-1):endtasktxt])
        info4.pack()
        info5 = Label(root,text = "Enter your python code: ")
        info5.pack()
        messagebox.showinfo("Attention!","Please make sure you include a ; after every line of code you enter!")
        e = Entry(root, width=60)
        e.pack(side=TOP)
        ent_button = Button(root, text="Enter", width=10,command= lambda: lines_entered() )
        ent_button.pack(side=TOP)
         
        def lines_entered():
            code = e.get()
            ent_button.destroy()
            e.destroy()
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
                                
            a_submit = []
            output = 0
            received_input=0
            stat_input = 0
            outputvar1 = random.randint(1000,10000)
            outputvar = "a"+str(outputvar1)
            for i in range(len(submit)):
                if submit[i].find("print(") != -1:
                    code = submit[i]
                    find = submit[i].find("print(")
                    value = code[find+6:-1]
                    if output > 0:
                        a_submit.append(code[:find]+str(outputvar)+".append("+str(value)+")")
                    else:
                        a_submit.append(code[:find]+str(outputvar)+" = ["+str(value)+"]")
                        output+=1
                elif submit[i].find("input(") != -1:
                    code = submit[i]
                    find = submit[i].find("input(")
                    value = code[:find-1]
                    a_submit.append(value+str(endinput_list[stat_input]))
                    stat_input += 1
                    received_input += 1
                else:
                    a_submit.append(submit[i])
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
            status_bar1 = Label(root, text="Testing...", bd=1, relief=SUNKEN, anchor=W)
            status_bar1.pack(side=BOTTOM, fill=X)
            file2 = open("mark.py", "a")
            file2.write('\n'+"  "+"f.write(str("+str(outputvar)+"))")
            file2.close()
            print("Test program created!")
            status_bar1.pack_forget()
            status_bar1 = Label(root, text="Running...", bd=1, relief=SUNKEN, anchor=W)
            status_bar1.pack(side=BOTTOM, fill=X)
            print(os.system('mark.py'))
            print("Attempting to gather output data...")
            if os.path.exists('./output.txt'):
                r = open("output.txt")
                print("Gathered successfully!")
                status_bar1.pack_forget()
                status_bar1 = Label(root, text="Marking...", bd=1, relief=SUNKEN, anchor=W)
                status_bar1.pack(side=BOTTOM, fill=X)
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
                status_bar1.pack_forget()            
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
                for i in range(len(words1)-1):
                    if words1[i].upper() == words[i].upper():
                        mark+=1
                    elif words[i].upper().find(words1[i].upper()) != -1:
                        mark+=1
                if received_input == len(endinput_list):
                        mark+=received_input
                status_bar1.pack_forget()
                status_bar1 = Label(root, text="Cleaning up...", bd=1, relief=SUNKEN, anchor=W)
                status_bar1.pack(side=BOTTOM, fill=X)
                info0.destroy()
                info4.destroy()
                d.close()
                f.close()
                r.close()
                #os.remove("tasklist.txt")
                os.remove("mark.py")
                os.remove("output.txt")
                #os.remove("task.txt")
                status_bar.destroy()
                status_bar1.pack_forget()
                status_bar1 = Label(root, text="Done!", bd=1, relief=SUNKEN, anchor=W)
                status_bar1.pack(side=BOTTOM, fill=X)       
                info7 = Label(root,text ="You got "+str(mark)+" out of "+str(total_marks)+" on this task!")
                info7.pack()
            else:
                messagebox.showinfo("Error!","Unfortunately an error was detected in the code you just submitted. Please try again!")
                label2 = Label(root,text = "For further diagnostics of your code you can access mark.py in the directory where MARKER.py is in!")
                label2.pack()
                label2 = Label(root,text = "You may close this window now!")
                label2.pack()
root.mainloop()
