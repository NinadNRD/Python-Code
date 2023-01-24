import tkinter as tk
from tkinter import ttk
from tkinter import * 
from tkinter.ttk import *
import tkinter.font as tkFont
from tkinter.messagebox import showinfo
import os
import time
from datetime import datetime
from tkinter import messagebox
#Tool Maker: Ninad Deshpande
# root window
root = tk.Tk()
root.geometry("400x360")
root.resizable(False, False)
root.title('Stadia Manipulator__________________________________________________')


Parameter = tk.StringVar()
############################################################################

def reset_achievements():
    print("\n Resetting achievements..... \n")
    time.sleep(1)
    print(os.system("ggp achievement player update --completion-percentage 0 --all"))
    time.sleep(1)
    print("\n Achievements reset successfully..... \n")
    print("______________________________________________________________________________")
    
############################################################################
    
def clear_pipeline():
    print("\n Clearing Pipeline Cache..... \n")
    time.sleep(1)
    print(os.system("ggp pipeline-cache delete --all"))
    time.sleep(1)
    print("\n Pipeline-Cache reset successfully..... \n")
    print("______________________________________________________________________________")
    
############################################################################
    
def clearing_saves():
    
    print("\n Clearing Stadia Kit Saves..... \n")
    time.sleep(1)
    print(os.system("ggp save delete --all"))
    print(os.system("ggp gamerstat player delete --all"))
    time.sleep(1)
    print("\n Stadia-Saves reset successfully..... \n")
    print("______________________________________________________________________________")

############################################################################
    
def clear_stadia_storage():
    decide = messagebox.askyesno('Yes|No', 'Do you want to proceed?\nContact Stadia Senior or Lead before using !!!')
    if(decide == True):
        print("\n Clearing Stadia Storage and Deployed Builds..... \n")
        time.sleep(1)
        print("\n Cleaning up Stadia-Storage..... \n")
        print(os.system("ggp ssh sync assets\* -rv --delete"))
        time.sleep(1)
        #print("\n Stadia-Storage cleared successfully..... \n")
        print("______________________________________________________________________________")
    else:
        print("Contact Stadia Senior or Lead")

############################################################################
def Info_display():
    messagebox.showinfo("Info:", "Creator : Ninad Deshpande\nDo contact if need help")

############################################################################


Label_LL=tk.Label(root)
Label_LL["bg"] = "#f2cf5d"
ft = tkFont.Font(family='Times',size=14)
Label_LL["font"] = ft
Label_LL["fg"] = "#f53535"
Label_LL["justify"] = "center"
Label_LL["text"] = "Data Clearer"
Label_LL.place(x=25,y=20,width=350,height=35)

############################################################################
reset_achieve=tk.Button(root)
reset_achieve["bg"] = "#efefef"
reset_achieve["borderwidth"] = "2px"
ft = tkFont.Font(family='Times',size=10)
reset_achieve["font"] = ft
reset_achieve["fg"] = "#000000"
reset_achieve["justify"] = "center"
reset_achieve["text"] = "Reset Achievements"
reset_achieve.place(x=30,y=80,width=150,height=30)
reset_achieve["command"] = reset_achievements

achieve_label=tk.Label(root)
ft = tkFont.Font(family='Times',size=9)
achieve_label["font"] = ft
achieve_label["fg"] = "#333333"
achieve_label["justify"] = "center"
achieve_label["text"] = "Reset all 1st Party Achievements"
achieve_label.place(x=20,y=110,width=160,height=30)
############################################################################

clear_cache=tk.Button(root)
clear_cache["bg"] = "#efefef"
clear_cache["borderwidth"] = "2px"
ft = tkFont.Font(family='Times',size=10)
clear_cache["font"] = ft
clear_cache["fg"] = "#000000"
clear_cache["justify"] = "center"
clear_cache["text"] = "Clear Pipeline-Cache"
clear_cache.place(x=220,y=80,width=150,height=30)
clear_cache["command"] = clear_pipeline

cache_label=tk.Label(root)
ft = tkFont.Font(family='Times',size=9)
cache_label["font"] = ft
cache_label["fg"] = "#333333"
cache_label["justify"] = "center"
cache_label["text"] = "Use when build have \n issue while Launching"
cache_label.place(x=200,y=115,width=180,height=30)

###############################################################################
clear_saves=tk.Button(root)
clear_saves["bg"] = "#efefef"
clear_saves["borderwidth"] = "2px"
ft = tkFont.Font(family='Times',size=10)
clear_saves["font"] = ft
clear_saves["fg"] = "#000000"
clear_saves["justify"] = "center"
clear_saves["text"] = "Clear-Saves"
clear_saves.place(x=140,y=160,width=110,height=30)
clear_saves["command"] = clearing_saves

saves_label=tk.Label(root)
ft = tkFont.Font(family='Times',size=9)
saves_label["font"] = ft
saves_label["fg"] = "#333333"
saves_label["justify"] = "center"
saves_label["text"] = "It will clear stadia saves, not Uplay-Saves \n Use only when saves are messed up!!!"
saves_label.place(x=70,y=200,width=250,height=30)
###############################################################################
clear_storage=tk.Button(root)
clear_storage["bg"] = "#efefef"
clear_storage["borderwidth"] = "2px"
ft = tkFont.Font(family='Times',size=10)
clear_storage["font"] = ft
clear_storage["fg"] = "#000000"
clear_storage["justify"] = "center"
clear_storage["text"] = "Clear Stadia Storage"
clear_storage.place(x=95,y=265,width=200,height=30)
clear_storage["command"] = clear_stadia_storage

storage_label=tk.Label(root)
ft = tkFont.Font(family='Times',size=9)
storage_label["font"] = ft
storage_label["fg"] = "#333333"
storage_label["justify"] = "center"
storage_label["text"] = "Use if Carefully, it will clear all Stadia Storage"
storage_label.place(x=70,y=300,width=250,height=30)
###############################################################################
Info_button=tk.Button(root)
Info_button["bg"] = "#efefef"
Info_button["borderwidth"] = "2px"
ft = tkFont.Font(family='Times',size=8)
Info_button["font"] = ft
Info_button["fg"] = "#000000"
Info_button["justify"] = "center"
Info_button["text"] = "i"
Info_button.place(x=5,y=330,width=20,height=20)
Info_button["command"] = Info_display

root.mainloop()
