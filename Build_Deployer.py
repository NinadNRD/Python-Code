import tkinter as tk
import tkinter.font as tkFont
import os
import time
import json
import tkinter as tk
from tkinter import ttk
from tkinter import * 
from tkinter.ttk import *
import tkinter.font as tkFont
from tkinter.messagebox import showinfo
from datetime import datetime
import threading
from tkinter import messagebox


root = tk.Tk()
root.geometry("650x550")
root.resizable(False, False)
root.title("Lets Deploy Build on Stadia Kit _________________________________________________________________________________________")

##########################################################################################
def Fetch_Data_command():
    print("Fetching Data .. .. .. .. .. .. .. .. ..\n")
    os.system("ggp package -s list > C:\listofbuilds.json")
    time.sleep(1)
    
    file = open("C:\listofbuilds.json", "r")
    x=file.read()
    finaldata = json.loads(x)
    sourceFile = open('C:\stadiabuilds.txt', 'w')
    for a in finaldata:
        print(a['created'],a['displayName'],a['id'], file = sourceFile)
        list1.insert(parent='',index='end',iid=a,text='',values=(a['displayName'],a['id']))
    sourceFile.close()

    
##########################################################################################
def Deploy_command():
    decide = messagebox.askyesno('Yes|No', 'Do you want to proceed?')
    if(decide == True):
        print("Deploying Build")
        deploy = Package_ID_text.get()
        os.system("ggp instance deploy-package --package="+deploy)
    elif(decide == False):
        print("Contact Senior or Lead if you have a Doubt\n")
        print("_________________________________________________________________________________________________________\n")

##########################################################################################
def Select_Build():
   #clear entry boxes
    Package_ID_text.delete(0,END)
    
    selected=list1.focus()
    values = list1.item(selected,'values')
    
    Package_ID_text.insert(0,values[1])
    print("\nSelected Build Name : "+values[0])
    print("Selected Build ID : "+values[1])

##########################################################################################
def clear_stadia_storage():
    decide = messagebox.askyesno('Yes|No', 'Are you Sure you want to clear Stadia Kit Storage?\nNot Sure !! Contact Senior or Lead !!!')
    if(decide == True):
        print("\n Clearing Stadia Storage and Deployed Builds..... \n")
        time.sleep(1)
        print("\n Cleaning up Stadia-Storage..... \n")
        print(os.system("ggp ssh sync assets\* -rv --delete"))
        time.sleep(1)
        print("\n Stadia-Storage cleared successfully..... \n")
        print("_________________________________________________________________________________________________________\n")
    else:
        print("Contact your Senior or Lead\n")
        print("_________________________________________________________________________________________________________\n")
        
##########################################################################################        
def Tool_Info():
    messagebox.showinfo("Info:", "Creator : Ninad Deshpande\nDo contact if need help")
##########################################################################################        

Label_SBD=tk.Label(root)
Label_SBD["activebackground"] = "#ea5050"
Label_SBD["bg"] = "#e7e086"
ft = tkFont.Font(family='Times',size=14)
Label_SBD["font"] = ft
Label_SBD["fg"] = "#e31111"
Label_SBD["justify"] = "center"
Label_SBD["text"] = "Stadia Build Deployer"
Label_SBD["relief"] = "ridge"
Label_SBD.place(x=20,y=30,width=610,height=40)
##########################################################################################

Package_ID_Label=tk.Label(root)
ft = tkFont.Font(family='Times',size=12)
Package_ID_Label["font"] = ft
Package_ID_Label["fg"] = "#333333"
Package_ID_Label["justify"] = "center"
Package_ID_Label["text"] = "Package ID : "
Package_ID_Label.place(x=35,y=105,width=100,height=25)
##########################################################################################
Package_ID_text=tk.Entry(root)
Package_ID_text["borderwidth"] = "2px"
ft = tkFont.Font(family='Times',size=12)
Package_ID_text["font"] = ft
Package_ID_text["fg"] = "#333333"
Package_ID_text["justify"] = "left"
Package_ID_text["text"] = ""
Package_ID_text.place(x=130,y=100,width=300,height=35)
##########################################################################################
Fetch_Data=tk.Button(root)
Fetch_Data["bg"] = "#efefef"
ft = tkFont.Font(family='Times',size=12)
Fetch_Data["font"] = ft
Fetch_Data["fg"] = "#000000"
Fetch_Data["justify"] = "center"
Fetch_Data["text"] = "Fetch Data"
Fetch_Data.place(x=65,y=250,width=500,height=30)
Fetch_Data["command"] = Fetch_Data_command
##########################################################################################
Deploy=tk.Button(root)
Deploy["bg"] = "#efefef"
ft = tkFont.Font(family='Times',size=12)
Deploy["font"] = ft
Deploy["fg"] = "#000000"
Deploy["justify"] = "center"
Deploy["text"] = "Deploy"
Deploy.place(x=455,y=100,width=140,height=30)
Deploy["command"] = Deploy_command
##########################################################################################
list1 = ttk.Treeview()
list1.pack(padx=5, pady=20, side=tk.BOTTOM)

list1['columns']= ('Build','ID')

list1.column("#0", width=0,  stretch=NO)
Build = list1.column("Build", width=380)
ID = list1.column("ID", width=250)

list1.heading("#0",text="",anchor=CENTER)
list1.heading("Build",text="Build",anchor=CENTER)
list1.heading("ID",text="ID",anchor=CENTER)

##########################################################################################
Select_B=tk.Button(root)
Select_B["bg"] = "#efefef"
ft = tkFont.Font(family='Times',size=12)
Select_B["font"] = ft
Select_B["fg"] = "#000000"
Select_B["justify"] = "center"
Select_B["text"] = "Select-Build"
Select_B.place(x=230,y=150,width=100,height=30)
Select_B["command"] = Select_Build
##########################################################################################
clear_storage=tk.Button(root)
clear_storage["bg"] = "#efefef"
ft = tkFont.Font(family='Times',size=12)
clear_storage["font"] = ft
clear_storage["fg"] = "#000000"
clear_storage["justify"] = "center"
clear_storage["text"] = "Clear Kit Storage"
clear_storage.place(x=455,y=160,width=140,height=30)
clear_storage["command"] = clear_stadia_storage
##########################################################################################
Info=tk.Button(root)
Info["bg"] = "#efefef"
ft = tkFont.Font(family='Times',size=10)
Info["font"] = ft
Info["fg"] = "#000000"
Info["justify"] = "center"
Info["text"] = "i"
Info.place(x=30,y=42,width=15,height=15)
Info["command"] = Tool_Info
##########################################################################################

root.mainloop()
