import shutil
import time
import tkinter as tk
from tkinter import *
import tkinter 
from tkinter.ttk import *
import tkinter.font as tkFont
from tkinter.messagebox import showinfo
import os
from datetime import datetime
from tkinter import messagebox
from zipfile import ZipFile
from atlassian import Jira
from jira.client import JIRA
from os import listdir

root = tk.Tk()
root.geometry("500x300")
root.eval('tk::PlaceWindow . center')
root.resizable(False, False)
root.title('RW Logger')

tkvar = tkinter.StringVar(root)
mainframe = tkinter.Frame(root)
mainframe.grid(column=0, row=0)
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.place(x=330,y=0,width=150,height=60)
choices = {'Testing','Production','App-Testing'}
popupMenu = tkinter.OptionMenu(mainframe, tkvar, *choices)
tkinter.Label(mainframe, text="Choose Environemnt", font=('Times',10),justify='right').grid(row = 1, column = 1)
popupMenu.grid(row = 2, column =1)
def change_dropdown(*Env):
    Env = tkvar.get()
    root.title('RW '+Env+' Logger')
    print(Env)
tkvar.trace('w', change_dropdown)

now = datetime.now()
dt_string = now.strftime("_%Y-%m-%d")
dt_string1 = now.strftime("__%Y-%m-%d__%H-%M-%S")



#########################################################   GET LOGS  #####################################################################
def Get_Action():

    toSearch1=r"RW.log"
    toSearch2=r"RW_2.log"
    toSearch3=r"Launcher"+dt_string+".log"
    toSearch4=r"Cef"+dt_string+".log"
    toSearch5=now.strftime("%d-%m-%Y")
    user = os.getlogin()
    dest="C:/Users/"+user+"/Desktop/Logs/"
    title = root.title()
    list_1 = title.split()
    str = list_1[1]
    if(title == 'RW1 Logger'):
        messagebox.showinfo("Info", "Please Select the Environment and Proceed further")
    
    elif(str=='Testing'):
        try:
            Testing_Path_1="C:/Users/"+user+"/AppData/Roaming/(testing)/Core/Saved/Logs/"
            Testing_Path_2="C:/Users/"+user+"/AppData/Roaming/(testing)/Launcher/Logs/" 
            zipObj = ZipFile('Log'+dt_string1+'.zip', 'w')
            try:   
                if(shutil.copy2(Testing_Path_1+toSearch1, dest+toSearch1)):
                    zipObj.write('RW.log')
                    os.remove("RW.log")
            except:
                print("RW1.log file is missing")

            try:
                if(shutil.copy2(Testing_Path_1+toSearch2, dest+toSearch2)):
                    zipObj.write('RW1_2.log')
                    os.remove("RW1_2.log")
            except:
                print("RW1_2.log file is missing")

            try:
                if(shutil.copy2(Testing_Path_2+toSearch3, dest+toSearch3)):
                    zipObj.write('Launcher'+dt_string+'.log')
                    os.remove('Launcher'+dt_string+'.log')   
            except:
                print("Launcher.log file is missing")

            try:
                if(shutil.copy2(Testing_Path_2+toSearch4, dest+toSearch4)):
                    zipObj.write('Cef'+dt_string+'.log')
                    os.remove('Cef'+dt_string+'.log')
            except:
                print("Cef.log file is missing")
            
            zipObj.close()
            messagebox.showinfo("Info", "Testing Env Logs are downloaded in Desktop/Logs path !!!")
        except:
            messagebox.showwarning("Warning", "Multiple Files are Missing")



    elif(str=='Production'):
        try:
            Production_Path_1="C:/Users/"+user+"/AppData/Roaming//RCore/Saved/Logs/"
            Production_Path_2="C:/Users/"+user+"/AppData/Roaming//Launcher/Logs/"
            zipObj = ZipFile('Log'+dt_string1+'.zip', 'w')
            try:
                if(shutil.copy2(Production_Path_1+toSearch1, dest+toSearch1)):
                    zipObj.write('RW1.log')
                    os.remove("RW1.log")
            except:
                print("RW.log file is missing")

            try:
                if(shutil.copy2(Production_Path_1+toSearch2, dest+toSearch2)):
                    zipObj.write('RW1_2.log')
                    os.remove("RW1_2.log")
            except:
                print("RW_2.log file is missing")
            
            try:
                if(shutil.copy2(Production_Path_2+toSearch3, dest+toSearch3)):
                    zipObj.write('Launcher'+dt_string+'.log')
                    os.remove('Launcher'+dt_string+'.log')
            except:
                print("Launcher.log file is missing")

            try:
                if(shutil.copy2(Production_Path_2+toSearch4, dest+toSearch4)):
                    zipObj.write('Cef'+dt_string+'.log')
                    os.remove('Cef'+dt_string+'.log')
            except:
                print("Cef.log file is missing")
            zipObj.close()
            messagebox.showinfo("Info", "Production Env Logs are downloaded in Desktop/Logs path !!!")
        except:
            messagebox.showwarning("Warning", "Multiple file are Missing")


    elif(str=='App-Testing'):
        try:
            App_Testing_Path_1="C:/Program Files/(app-testing)/sharedData//CoreClient/Saved/Logs/"
            App_Testing_Path_2="C:/Users/"+user+"/AppData/Roaming/(app-testing)/logs/"
            zipObj = ZipFile('Log'+dt_string1+'.zip', 'w')
            try:
                if(shutil.copy2(App_Testing_Path_1+toSearch1, dest+toSearch1)):
                    zipObj.write('RW1.log')
                    os.remove("RW1.log")
            except:
                print("RW1.log file is missing")
            
            try:
                if(shutil.copy2(App_Testing_Path_1+toSearch2, dest+toSearch2)):
                    zipObj.write('RW1_2.log')
                    os.remove("RW1_2.log")
            except:
                print("RW1_2.log file is missing")
            
            try:
                if(shutil.copy2(App_Testing_Path_2+(toSearch5+'.log'), dest+(toSearch5+'.log'))):
                    zipObj.write(toSearch5+'.log')
                    os.remove(toSearch5+'.log')
            except:
                print("App Core Logs are missing")
            zipObj.close()
            messagebox.showinfo("Info", "App-Testing Env Logs are downloaded in Desktop/Logs path !!!")
        except:
            messagebox.showwarning("Warning", "Multiple files are Missing")


#########################################################   GET CRASH DUMP  #####################################################################
def Crash():
    user = os.getlogin()
    
    title = root.title()
    list_1 = title.split()
    str = list_1[1]
    if(title == 'RW1 Logger'):
        messagebox.showinfo("Info", "Please Select the Environment and Proceed further")
    
    elif(str=='Testing'):
        try:
            scr = 'C:/Users/'+user+'/AppData/Roaming/(testing)//Saved/Crashes/'
            trg = 'C:/Users/'+user+'/Desktop/Logs'

            path1=max([os.path.join(scr,d) for d in os.listdir(scr)], key=os.path.getmtime)
            folder_name=os.path.basename(path1)
            files=os.listdir(path1)
            for fname in files:
                shutil.copy2(os.path.join(path1,fname), trg)

            zipObj = ZipFile(folder_name+'.zip', 'w')
            try:  
                if(zipObj.write('.cr')):
                    os.remove('.cr')
                os.remove('.cr')
            except:
                print(".cr file is missing")
            try:
                if(zipObj.write('.fatal')):
                    os.remove('.fatal')
                os.remove('.fatal')
            except:
                print(".fatal file is missing")
            try:
                if(zipObj.write('CrashContext.runtime-xml')):
                    os.remove('CrashContext.runtime-xml')
                os.remove('CrashContext.runtime-xml')
            except:
                print("CrashContext.runtime-xml file is missing")
            try:
                if(zipObj.write('CrashReportClient.ini')):
                    os.remove('CrashReportClient.ini')
                os.remove('CrashReportClient.ini')
            except:
                print("CrashReportClient.ini file is missing")
            try:
                if(zipObj.write('dumpdata.bin')):
                    os.remove('dumpdata.bin')
                os.remove('dumpdata.bin')
            except:
                print("dumpdata.bin file is missing")
            try:
                if(zipObj.write('UE4Minidump.dmp')):
                    os.remove('UE4Minidump.dmp')
                os.remove('UE4Minidump.dmp')
            except:
                print("UE4Minidump.dmp file is missing")
            try:
                if(zipObj.write('R1212.log')):
                    os.remove('RW121.log')
                os.remove('R1244.log')
            except:
                print(".log file is missing")

            try:
                if(zipObj.write('W1_2.log')):
                    os.remove('W1_2.log')
                os.remove('R1_2.log')
            except:
                print("R1_2.log file is missing")

            zipObj.close() 
            messagebox.showinfo("Info", "Testing Env Crash-Dump zip file created, Successfilly !! ")
        except:
            messagebox.showwarning("Warning", "Missing Files")

    elif(str=='Production'):
        try:
            scr = 'C:/Users/'+user+'/AppData/Roaming//Core/Saved/Crashes/'
            trg = 'C:/Users/'+user+'/Desktop/Logs'

            path1=max([os.path.join(scr,d) for d in os.listdir(scr)], key=os.path.getmtime)
            folder_name=os.path.basename(path1)
            files=os.listdir(path1)
            for fname in files:
                shutil.copy2(os.path.join(path1,fname), trg)
            zipObj = ZipFile(folder_name+'.zip', 'w')

            try:  
                if(zipObj.write('.cr')):
                    os.remove('.cr')
                os.remove('.cr')
            except:
                print(".cr file is missing")
            try:
                if(zipObj.write('.fatal')):
                    os.remove('.fatal')
                os.remove('.fatal')
            except:
                print(".fatal file is missing")
            try:
                if(zipObj.write('CrashContext.runtime-xml')):
                    os.remove('CrashContext.runtime-xml')
                os.remove('CrashContext.runtime-xml')
            except:
                print("CrashContext.runtime-xml file is missing")
            try:
                if(zipObj.write('CrashReportClient.ini')):
                    os.remove('CrashReportClient.ini')
                os.remove('CrashReportClient.ini')
            except:
                print("CrashReportClient.ini file is missing")
            try:
                if(zipObj.write('dumpdata.bin')):
                    os.remove('dumpdata.bin')
                os.remove('dumpdata.bin')
            except:
                print("dumpdata.bin file is missing")
            try:
                if(zipObj.write('UE4Minidump.dmp')):
                    os.remove('UE4Minidump.dmp')
                os.remove('UE4Minidump.dmp')
            except:
                print("UE4Minidump.dmp file is missing")
            try:
                if(zipObj.write('RW_2.log')):
                    os.remove('RW_2.log')
                os.remove('RW_2.log')
            except:
                print("RW_2.log file is missing")
            try:
                if(zipObj.write('R.log')):
                    os.remove('R.log')
                os.remove('R.log')
            except:
                print("R.log file is missing")


            zipObj.close()  
            messagebox.showinfo("Info", "Production Env Crash-Dump zip file created, Successfilly !! ")
        except:
            messagebox.showwarning("Warning", "Multiple files are Missing")

    elif(str=='App-Testing'):
        try:
            scr = 'C:/Program Files/(app-testing)/sharedData/shared/CoreClient/Saved/Crashes/'
            trg = 'C:/Users/'+user+'/Desktop/Logs'

            path1=max([os.path.join(scr,d) for d in os.listdir(scr)], key=os.path.getmtime)
            folder_name=os.path.basename(path1)
            files=os.listdir(path1)
            for fname in files:
                shutil.copy2(os.path.join(path1,fname), trg)

            zipObj = ZipFile(folder_name+'.zip', 'w')
            try:  
                if(zipObj.write('.cr')):
                    os.remove('.cr')
                os.remove('.cr')
            except:
                print(".cr file is missing")
            try:
                if(zipObj.write('.fatal')):
                    os.remove('.fatal')
                os.remove('.fatal')
            except:
                print(".fatal file is missing")
            try:
                if(zipObj.write('CrashContext.runtime-xml')):
                    os.remove('CrashContext.runtime-xml')
                os.remove('CrashContext.runtime-xml')
            except:
                print("CrashContext.runtime-xml file is missing")
            try:
                if(zipObj.write('CrashReportClient.ini')):
                    os.remove('CrashReportClient.ini')
                os.remove('CrashReportClient.ini')
            except:
                print("CrashReportClient.ini file is missing")
            try:
                if(zipObj.write('dumpdata.bin')):
                    os.remove('dumpdata.bin')
                os.remove('dumpdata.bin')
            except:
                print("dumpdata.bin file is missing")
            try:
                if(zipObj.write('UE4Minidump.dmp')):
                    os.remove('UE4Minidump.dmp')
                os.remove('UE4Minidump.dmp')
            except:
                print("UE4Minidump.dmp file is missing")
            try:
                if(zipObj.write('RW1.log')):
                    os.remove('RW1.log')
                os.remove('RW1.log')
            except:
                print("RW.log file is missing")
            try:
                if(zipObj.write('R_2.log')):
                    os.remove('W1_2.log')
                os.remove('R_2.log')
            except:
                print("RW_2.log file is missing")

            zipObj.close() 
            messagebox.showinfo("Info", "App-Testing Env Crash-Dump zip file created, Successfilly !! ")
        except:
            messagebox.showwarning("Warning", "Multiple files are Missing")


#########################################################   CLEAR LOGS  #####################################################################

def Clear_Logs():
    
    txt = messagebox.askquestion("Wait", "Are you sure want to clear logs?")
    print(txt)
    if(txt == 'yes'):
        user = os.getlogin()
        title = root.title()
        print("title :"+title)
        list_1 = title.split()
        str = list_1[1]

        if(title=='RW1 Logger'):
            print("please select the Environment")
            messagebox.showinfo("Info", "Please Select the Environment and Proceed further")

        elif(str=='Testing'):
            Testing_Path_1="C:/Users/"+user+"/AppData/Roaming//Core/Saved/Logs/"
            Testing_Path_2="C:/Users/"+user+"/AppData/Roaming/(testing)/Launcher/Logs/"
            for file_name in os.listdir(Testing_Path_1):
                file = Testing_Path_1 + file_name
                if os.path.isfile(file):
                    print('Deleting file:', file)
                    os.remove(file)
            time.sleep(2)
            for file_name in os.listdir(Testing_Path_2):
                file = Testing_Path_2 + file_name
                if os.path.isfile(file):
                    print('Deleting file:', file)
                    os.remove(file)
            print("Testing Files has been cleared")
            messagebox.showinfo("Info", "Testing Env Logs Cleared")

        elif(str=='Production'):

            Production_Path_1="C:/Users/"+user+"/AppData/Roaming/Core/Saved/Logs/"
            Production_Path_2="C:/Users/"+user+"/AppData/Roaming/Launcher/Logs/"
            for file_name in os.listdir(Production_Path_1):
                file = Production_Path_1 + file_name
                if os.path.isfile(file):
                    print('Deleting file:', file)
                    os.remove(file)
            time.sleep(2)
            for file_name in os.listdir(Production_Path_2):
                file = Production_Path_2 + file_name
                if os.path.isfile(file):
                    print('Deleting file:', file)
                    os.remove(file)
            print("Production Files has been cleared")
            messagebox.showinfo("Info", "Production Env Logs Cleared")

        
        elif(str=='App-Testing'):
            App_Testing_Path_1="C:/Program Files/(app-testing)/sharedData/rshared/CoreClient/Saved/Logs/"
            App_Testing_Path_2="C:/Users/"+user+"/AppData/Roaming/(app-testing)/logs/"
            for file_name in os.listdir(App_Testing_Path_1):
                file = App_Testing_Path_1 + file_name
                if os.path.isfile(file):
                    print('Deleting file:', file)
                    os.remove(file)
            time.sleep(2)
            for file_name in os.listdir(App_Testing_Path_2):
                file = App_Testing_Path_2 + file_name
                if os.path.isfile(file):
                    print('Deleting file:', file)
                    os.remove(file)
            print("App-Testing Files has been cleared")
            messagebox.showinfo("Info", "App-Testing Env Logs Cleared")



    elif(txt == 'no'):
        print("else code is working")

#########################################################   CLEAR SAVES  #####################################################################

def Clear_Saves():
        
    txt = messagebox.askquestion("Wait", "Are you sure want to clear saves?")
    print(txt)
    if(txt == 'yes'):
        user = os.getlogin()
        title = root.title()
        print("title :"+title)
        list_1 = title.split()
        str = list_1[1]

        if(title=='RW1 Logger'):
            print("please select the Environment")
            messagebox.showinfo("Info", "Please Select the Environment and Proceed further")

        elif(str=='Testing'):
            Testing_Path_1="C:/Users/"+user+"/AppData/Roaming/(testing)/Core/Saved/SaveGames/"
            for file_name in os.listdir(Testing_Path_1):
                file = Testing_Path_1 + file_name
                if os.path.isfile(file):
                    print('Deleting file:', file)
                    os.remove(file)
            print("Files has been cleared")
            messagebox.showinfo("Info", "Testing Env Saves Cleared")

        elif(str=='Production'):
            Production_Path_1="C:/Users/"+user+"/AppData/Roaming/one/Core/Saved/SaveGames/"
            for file_name in os.listdir(Production_Path_1):
                file = Production_Path_1 + file_name
                if os.path.isfile(file):
                    print('Deleting file:', file)
                    os.remove(file)
            print("Files has been cleared")
            messagebox.showinfo("Info", "Production Env Saves Cleared")
        
        elif(str=='App-Testing'):
            App_Testing_Path_1="C:/Program Files/(app-testing)/sharedData/shared/CoreClient/Saved/SaveGames/"
            for file_name in os.listdir(App_Testing_Path_1):
                file = App_Testing_Path_1 + file_name
                if os.path.isfile(file):
                    print('Deleting file:', file)
                    os.remove(file)
            print("Files has been cleared")
            messagebox.showinfo("Info", "App-Testing Env Saves Cleared")

#########################################################   JIRA LOGS UPLOAD  #####################################################################
def Link_D_Jira():
        txt = messagebox.askquestion("Wait", "Are you sure want to direct link logs in Jira?")
        print(txt)
        if(txt == 'yes'):
            user = os.getlogin()
            title = root.title()
            print("title :"+title)
            list_1 = title.split()
            str = list_1[1]

            toSearch1=r"R.log"
            toSearch2=r"R_2.log"
            toSearch3=r"Launcher"+dt_string+".log"
            toSearch4=r"Cef"+dt_string+".log"
            toSearch5=now.strftime("%d-%m-%Y")

            inp = Text_ID_Jira.get()
            print("Text through Field :"+inp)
            user = os.getlogin()
            dest="C:/Users/"+user+"/Desktop/Logs/"

            if(inp==''):
                messagebox.showinfo("Info", "Text Field is Empty")
                breakpoint
            
            
            title = root.title()
            list_1 = title.split()
            str = list_1[1]
            if(title == 'RW1 Logger'):
                messagebox.showinfo("Info", "Please Select the Environment and Proceed further")

          
            
            elif(str=='Testing'):
                try:
                    if(inp==''):
                        messagebox.showinfo("Info", "Text Field is Empty")
                        breakpoint
                    Testing_Path_1="C:/Users/"+user+"/AppData/Roaming/(testing)/Core/Saved/Logs/"
                    Testing_Path_2="C:/Users/"+user+"/AppData/Roaming/(testing)/Launcher/Logs/"
                    jira_client = JIRA(options={'server': 'URL'}, basic_auth=('email ID', 'API Token'))

                    try:
                        if(shutil.copy2(Testing_Path_1+toSearch1, dest+toSearch1)):
                            jira_client.add_attachment(inp,'RW1.log')
                            os.remove("RW1.log")
                    except:
                        print("RW1.log are missing and failed to upload")

                    try:
                        if(shutil.copy2(Testing_Path_1+toSearch2, dest+toSearch2)):
                            jira_client.add_attachment(inp,'RW1_2.log')
                            os.remove("RW1_2.log")
                    except:
                        print("RW1_2.log are missing and failed to upload")

                    try:
                        if(shutil.copy2(Testing_Path_2+toSearch3, dest+toSearch3)):
                            jira_client.add_attachment(inp,'Launcher'+dt_string+'.log')
                            os.remove('Launcher'+dt_string+'.log')
                    except:
                        print("Launcher.log are missing and failed to upload")
                    try:
                        if(shutil.copy2(Testing_Path_2+toSearch4, dest+toSearch4)):
                            jira_client.add_attachment(inp,'Cef'+dt_string+'.log')
                            os.remove('Cef'+dt_string+'.log')
                    except:
                        print("Cef.log are missing and failed to upload")
                        messagebox.showinfo("Info", "Operation Failed")
                        
                    time.sleep(1)
                    
                except ValueError as e:
                    messagebox.showwarning("Warning", e)

            elif(str=='Production'):
                try:
                    Production_Path_1="C:/Users/"+user+"/AppData/Roaming//RW1Core/Saved/Logs/"
                    Production_Path_2="C:/Users/"+user+"/AppData/Roaming//Launcher/Logs/"
                    jira_client = JIRA(options={'server': 'URL'}, basic_auth=('email ID', 'API Token'))

                    try:
                        if(shutil.copy2(Production_Path_1+toSearch1, dest+toSearch1)):
                            jira_client.add_attachment(inp,'RW1.log')
                            os.remove("RW1.log")
                    except:
                        print("RW1.log file is missing and failed to upload")
                    try:
                        if(shutil.copy2(Production_Path_1+toSearch2, dest+toSearch2)):
                            jira_client.add_attachment(inp,'RW1_2.log')
                            os.remove("RW1_2.log")
                    except:
                        print("RW1_2.log file is missing and failed to upload")
                    try:
                        if(shutil.copy2(Production_Path_2+toSearch3, dest+toSearch3)):
                            jira_client.add_attachment(inp,'Launcher'+dt_string+'.log')
                            os.remove('Launcher'+dt_string+'.log')
                    except:
                        print("Launcher.log file is missing and failed to upload")
                    try:
                        if(shutil.copy2(Production_Path_2+toSearch4, dest+toSearch4)):
                            jira_client.add_attachment(inp,'Cef'+dt_string+'.log')
                            os.remove('Cef'+dt_string+'.log')
                    except:
                        print("Cef.log file is missing and failed to upload")
                    time.sleep(1)
                    messagebox.showinfo("Info", "Production Environment Logs Uploaded")
                except:
                    messagebox.showwarning("Warning", "Missing Files")

            elif(str=='App-Testing'):
                try:
                    App_Testing_Path_1="C:/Program Files/(app-testing)/sharedData/CoreClient/Saved/Logs/"
                    App_Testing_Path_2="C:/Users/"+user+"/AppData/Roaming/(app-testing)/logs/"
                    jira_client = JIRA(options={'server': 'URL'}, basic_auth=('email ID', 'API Token'))

                    try:
                        if(shutil.copy2(App_Testing_Path_1+toSearch1, dest+toSearch1)):
                            jira_client.add_attachment(inp,'RW1.log')
                            os.remove("RW1.log")
                    except:
                        print("RW1.log file is missing and failed to upload")
                    try:
                        if(shutil.copy2(App_Testing_Path_1+toSearch2, dest+toSearch2)):
                            jira_client.add_attachment(inp,'RW1_2.log')
                            os.remove("R_2.log")
                    except:
                        print("RW1_2.log file is missing and failed to upload")
                    try:
                        if(shutil.copy2(App_Testing_Path_2+(toSearch5+'.log'), dest+(toSearch5+'.log'))):
                            jira_client.add_attachment(inp,toSearch5+'.log')
                            os.remove(toSearch5+'.log')
                    except:
                        print("Application Core are missing and failed to upload")
                    time.sleep(1)
                    messagebox.showinfo("Info", "App-Testing Environment Logs Uploaded")
                except:
                    messagebox.showwarning("Warning", "Missing Files")

def Cls_Folder():
    print("Clearing Files from current folder")
    for fileName in listdir():
    #Check file extension
        if fileName.endswith('.log'):
            os.remove(fileName)
        if fileName.endswith('.zip'):
            os.remove(fileName)
        if fileName.endswith('.cr'):
            os.remove(fileName)
        if fileName.endswith('.fatal'):
            os.remove(fileName)
        if fileName.endswith('.runtime-xml'):
            os.remove(fileName)
        if fileName.endswith('.ini'):
            os.remove(fileName)
        if fileName.endswith('.bin'):
            os.remove(fileName)
        if fileName.endswith('.dmp'):
            os.remove(fileName)
    messagebox.showinfo("Info", "Files cleared from the Desktop/Logs folder.")  
print("All files removed successfully")


#########################################################   UI FRAME DESIGN  #####################################################################
login_button=tk.Button(root)
login_button["bg"] = "#efefef"
login_button["borderwidth"] = "2px"
ft = tkFont.Font(family='Times',size=12)
login_button["font"] = ft
login_button["fg"] = "#000000"
login_button["justify"] = "center"
login_button["text"] = "Get Logs"
login_button.place(x=15,y=80,width=90,height=30)
login_button["command"]= Get_Action

Logs_Crash=tk.Button(root)
Logs_Crash["bg"] = "#efefef"
Logs_Crash["borderwidth"] = "2px"
ft = tkFont.Font(family='Times',size=12)
Logs_Crash["font"] = ft
Logs_Crash["fg"] = "#000000"
Logs_Crash["justify"] = "center"
Logs_Crash["text"] = "Get Crash"
Logs_Crash.place(x=115,y=80,width=90,height=30)
Logs_Crash["command"]= Crash

Name_label=tk.Label(root)
ft = tkFont.Font(family='Times',size=10)
Name_label["font"] = ft
Name_label["fg"] = "#333333"
Name_label["justify"] = "center"
Name_label["text"] = "Downloads files in Dekstop Logs Folder"
Name_label.place(x=10,y=110,width=220,height=40)

Name_label=tk.Label(root)
ft = tkFont.Font(family='Times',size=10)
Name_label["font"] = ft
Name_label["fg"] = "#333333"
Name_label["justify"] = "center"
Name_label["text"] = "Deletes Logs and Saves"
Name_label.place(x=10,y=210,width=200,height=40)

user1 = os.getlogin()
User_Name=tk.Label(root)
ft = tkFont.Font(family='Times',size=10)
User_Name["font"] = ft
User_Name["fg"] = "#333333"
User_Name["justify"] = "left"
User_Name["text"] = "User : "+user1
User_Name.place(x=0,y=5,width=150,height=25)

Clear_log_button=tk.Button(root)
Clear_log_button["bg"] = "#efefef"
Clear_log_button["borderwidth"] = "2px"
ft = tkFont.Font(family='Times',size=12)
Clear_log_button["font"] = ft
Clear_log_button["fg"] = "#000000"
Clear_log_button["justify"] = "center"
Clear_log_button["text"] = "Clear Logs"
Clear_log_button.place(x=15,y=180,width=90,height=30)
Clear_log_button["command"] = Clear_Logs

Clear_save_button=tk.Button(root)
Clear_save_button["bg"] = "#efefef"
Clear_save_button["borderwidth"] = "2px"
ft = tkFont.Font(family='Times',size=12)
Clear_save_button["font"] = ft
Clear_save_button["fg"] = "#000000"
Clear_save_button["justify"] = "center"
Clear_save_button["text"] = "Clear Saves"
Clear_save_button.place(x=115,y=180,width=90,height=30)
Clear_save_button["command"] = Clear_Saves

Link_Log_Button=tk.Button(root)
Link_Log_Button["bg"] = "#efefef"
Link_Log_Button["borderwidth"] = "2px"
ft = tkFont.Font(family='Times',size=12)
Link_Log_Button["font"] = ft
Link_Log_Button["fg"] = "#000000"
Link_Log_Button["justify"] = "center"
Link_Log_Button["text"] = "Link Direct"
Link_Log_Button.place(x=350,y=180,width=80,height=30)
Link_Log_Button["command"] = Link_D_Jira

Text_ID_Jira=tk.Entry(root)
Text_ID_Jira["borderwidth"] = "2px"
ft = tkFont.Font(family='Times',size=10)
Text_ID_Jira["font"] = ft
Text_ID_Jira["fg"] = "#333333"
Text_ID_Jira["justify"] = "left"
#Text_ID_Jira["textvariable"] = Parameter
Text_ID_Jira.place(x=340,y=135,width=100,height=30)
Text_ID_Jira.focus()

Link_label=tk.Label(root)
ft = tkFont.Font(family='Times',size=10)
Link_label["font"] = ft
Link_label["fg"] = "#333333"
Link_label["justify"] = "center"
Link_label["text"] = "Seperate Logs gets Link Directly"
Link_label.place(x=290,y=210,width=200,height=40)

cls_button=tk.Button(root)
cls_button["bg"] = "#efefef"
cls_button["borderwidth"] = "2px"
ft = tkFont.Font(family='Times',size=10)
cls_button["font"] = ft
cls_button["fg"] = "#000000"
cls_button["justify"] = "center"
cls_button["text"] = "Cls"
cls_button.place(x=460,y=270,width=30,height=25)
cls_button["command"] = Cls_Folder

root.mainloop()