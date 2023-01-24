import tkinter as tk
from tkinter import ttk
from tkinter import * 
from tkinter.ttk import *
import tkinter.font as tkFont
from tkinter.messagebox import showinfo
import os
import time
from datetime import datetime
import threading
from tkinter import messagebox
import glob
import os.path

# root window
root = tk.Tk()
root.geometry("400x300")
root.resizable(False, False)
root.title('__________Stadia Logs Downloader__________')

#p1 = PhotoImage(file = 'C:\google-stadia.png')
#root.iconphoto(False, p1)

Parameter = tk.StringVar()

def login_clicked():
    
    msg = Parameter.get()
    print("Launching Build with parameter: "+msg)
    
    now = datetime.now()
    dt_string = now.strftime("___%Y-%m-%d___%H-%M-%S")

    str ='a'
    for a in str:
        #print(os.system("ggp run --cmd "+msg +"> C:\Logs"+dt_string+".txt"))
        print(os.system("ggp run --cmd "+msg +"> cd > Logs"+dt_string+".txt"))
        time.sleep(2)
        
    username = os.path.expanduser('~')
    src_folder = r"\AppData\Roaming\GGP\logs"
    folder_path = username + src_folder
    file_type = r'\ggp*log'
    files = glob.glob(folder_path + file_type)
    max_file = max(files, key=os.path.getctime)
    os.system("copy "+max_file)
    print("Closing Game")
        
def Download_Logs():
    print(os.system("ggp ssh get /var/game/scimitar_online*.log"))
    
def Info_display():
    messagebox.showinfo("Info:", "Creator : Ninad Deshpande\nDo contact if need help")
  
signin = ttk.Frame(root)
signin.pack(padx=10, pady=10, fill='x', expand=True)


    


Label_LL=tk.Label(root)
Label_LL["bg"] = "#f2cf5d"
ft = tkFont.Font(family='Times',size=14)
Label_LL["font"] = ft
Label_LL["fg"] = "#f53535"
Label_LL["justify"] = "center"
Label_LL["text"] = "Live Logs"
Label_LL.place(x=25,y=20,width=350,height=35)

Para_label=tk.Label(root)
ft = tkFont.Font(family='Times',size=12)
Para_label["font"] = ft
Para_label["fg"] = "#333333"
Para_label["justify"] = "center"
Para_label["text"] = "Launch Parameter:"
Para_label.place(x=10,y=80,width=132,height=39)


Para_entry=tk.Entry(root)
Para_entry["borderwidth"] = "2px"
ft = tkFont.Font(family='Times',size=10)
Para_entry["font"] = ft
Para_entry["fg"] = "#333333"
Para_entry["justify"] = "left"
Para_entry["textvariable"] = Parameter
Para_entry.place(x=140,y=80,width=250,height=40)
Para_entry.focus()


login_button=tk.Button(root)
login_button["bg"] = "#efefef"
login_button["borderwidth"] = "2px"
ft = tkFont.Font(family='Times',size=12)
login_button["font"] = ft
login_button["fg"] = "#000000"
login_button["justify"] = "center"
login_button["text"] = "Launch"
login_button.place(x=100,y=150,width=200,height=30)
login_button["command"] = login_clicked
#login_button["command"]= threading.Thread(target=login_clicked).start


Name_label=tk.Label(root)
ft = tkFont.Font(family='Times',size=10)
Name_label["font"] = ft
Name_label["fg"] = "#333333"
Name_label["justify"] = "center"
Name_label["text"] = "Live Logs will get downloaded in Current Folder"
Name_label.place(x=50,y=180,width=300,height=39)


Download_button=tk.Button(root)
Download_button["bg"] = "#efefef"
Download_button["borderwidth"] = "2px"
ft = tkFont.Font(family='Times',size=12)
Download_button["font"] = ft
Download_button["fg"] = "#000000"
Download_button["justify"] = "center"
Download_button["text"] = "Download Logs"
Download_button.place(x=100,y=240,width=200,height=30)
Download_button["command"] = Download_Logs

Name_label=tk.Label(root)
ft = tkFont.Font(family='Times',size=10)
Name_label["font"] = ft
Name_label["fg"] = "#333333"
Name_label["justify"] = "center"
Name_label["text"] = "Pre Recorded / Saved Logs will get Downloaded"
Name_label.place(x=50,y=270,width=300,height=39)


Info_button=tk.Button(root)
Info_button["bg"] = "#efefef"
Info_button["borderwidth"] = "2px"
ft = tkFont.Font(family='Times',size=8)
Info_button["font"] = ft
Info_button["fg"] = "#000000"
Info_button["justify"] = "center"
Info_button["text"] = "i"
Info_button.place(x=5,y=270,width=20,height=20)
Info_button["command"] = Info_display

root.mainloop()