"""
!/usr/bin/env python3
__AUTHOR = "JIMOH IDRIS OLANSHILE"
__DATE = "Sept 2020 - till date."
"""
import os as gd, subprocess as sp, time
from tkinter import *
from tkinter import (filedialog as fd, import messagebox as mb)
from tkinter.ttk import Progressbar
from mysql.connnector import connection
from pyAesCrypt import (encryptFile as enc, import decryptFile as dec)
def secNote ():
    global password, bufferSize, anon
    password = pWord
    bufferSize = 64 * 1024
    anon = "attrib "
    secPth = gd.path.join (Pth, "seton\\")
    if gd.path.exists (secPth) == True:pass
    else:
        gd.mkdir (secPth)

    def doTrunc(event):
        def dele():
            data = "01"
            fO = open (f, "rb+")
            fO.read()
            count = fO.tell()
            data = data * int((count/2))
            fO.seek(0)
            fO.write (data.encode("utf-8"))
            fO.close()
        ans = mb.askquestion ("Confirmation", "Do you really want to truncate all of your hidden files?")
        if ans == "no":pass
        else:
            try:
                passes = 5
                num1 = 0
                num2 = 0
                cur.execute ("SELECT file FROM files WHERE user_login = " + "\"" + u_ + "\" ")
                for files in cur: #temp uh
                    files = files[0]
                    lFile = "\"" + files + "\""
                    lFile = lFile.replace ("\\", "/")
                    gd.system (anon + lFile + " -h -r -s -a")
                    F2d = files #unlike system, enc doesnt require the path to the quoted
                    newF2d = files.rpartition (".idr")[0]
                    dec (F2d, newF2d, password, bufferSize)
                    gd.system ("del " + "\"" + F2d.replace ("/", "\\") + "\"")
                    #gd.system ("del " + "\"" + newF2d.replace ("/", "\\") + "\"")
                    #lFile = lFile.replace ("\\", "\\\\")
                    f = newF2d.replace ("\\", "/")
                    num1 += 1
                    for i in range (0, int(passes)):
                        dele()
                        clr()
                    gd.rename (f, "zz028")
                    gd.unlink("zz028")
                cur.execute ("SELECT file FROM securenote WHERE user_login = " + "\"" + u_ + "\" ")
                for files in cur: #temp uh
                    files = files[0]
                    lFile = "\"" + files + "\""
                    lFile = lFile.replace ("/", "\\")
                    gd.system (anon + lFile + " -h -r -s -a")
                    F2d = files #unlike system, enc doesnt require the path to the quoted
                    newF2d = files.rpartition (".idr")[0]
                    dec (F2d, newF2d, password, bufferSize)
                    gd.system ("del " + "\"" + F2d.replace ("/", "\\") + "\"")
                    #gd.system ("del " + "\"" + newF2d.replace ("/", "\\") + "\"")
                    #lFile = lFile.replace ("\\", "\\\\")
                    f = newF2d
                    num2 += 1
                    for i in range (0, int(passes)):
                        dele()
                        clr()
                    gd.rename (f, "zz028")
                    gd.unlink("zz028")
                cur.execute ("truncate files")
                cur.execute ("truncate securenote")
                numTot = num1 + num2
                mb.showinfo ("Success", str (numTot) + " files just got truncated")
                conn.commit()
                clr()
            except OSError:
                logLab = Label (secNoteP, text = "  Error (0%)", bg = "#363277", fg = "WHITE")
                logLab.place (x = 0, y = 517)
                

    def doDel(event):
        def dele():
            data = "01"
            fO = open (f, "rb+")
            fO.read()
            count = fO.tell()
            data = data * int((count/2))
            fO.seek(0)
            fO.write (data.encode("utf-8"))
            fO.close()

        cur.execute ("SELECT file FROM files WHERE user_login = " + "\"" + u_ + "\" ")
        for p in cur: #temp uh
            p = p[0]
            gd.system (anon + "\"" + p + "\"" + " -h -r -s -a")
            clr()
        cur.execute ("SELECT file FROM securenote WHERE user_login = " + "\"" + u_ + "\" ")
        for p in cur: #temp uh
            p = p[0]
            gd.system (anon + "\"" + p + "\"" + " -h -r -s -a")
            clr()
        fileD = fd.askopenfilenames (title = "Choose file (s) to shred", initialdir = Pth)
        cur.execute ("SELECT file FROM files WHERE user_login = " + "\"" + u_ + "\" ")
        for p in cur:
            p = p[0]
            gd.system (anon + "\"" + p + "\"" + " +h +r +s +a")
            clr()
        cur.execute ("SELECT file FROM securenote WHERE user_login = " + "\"" + u_ + "\" ")
        for p in cur:
            p = p[0]
            gd.system (anon + "\"" + p + "\"" + " +h +r +s +a")
            clr()
        if fileD == "":pass
        else:
            qVal = mb.askquestion ("Confirmation", "Proceed to delete file(s)?\nNote: The file cannot be recovered even with recovery tools")
            if qVal == "no":pass
            else:
                passes = 5 #input ("Enter Number of Passes: ")
                num = 0
                n = 0
                progress = Progressbar (secNoteP, orient = HORIZONTAL, length = 100, mode = "determinate")
                progress.place (x = 0, y = 515)
                progress['value'] = 0 #blank slate for progressbar
                logLab = Label (secNoteP, text = " : Success", bg = "#363277", fg = "#363277")#blank success label
                logLab.place (x = 100, y = 517)
                secNoteP.update_idletasks()
                for f in fileD:
                    if f.rpartition (".")[2] == "idr":
                        F2d = f #unlike system, enc doesnt require the path to the quoted
                        newF2d = f.rpartition (".idr")[0]
                        dec (F2d, newF2d, password, bufferSize)
                        f = newF2d
                        gd.system (anon + "\"" + F2d.replace ("/", "\\") + "\"" + " -h -r -s -a")
                        gd.system ("del " + "\"" + F2d.replace ("/", "\\") + "\"")
                    for i in range (0, int(passes)):
                        dele()
                        num += 1
                        clr()
                    gd.rename (f, "zz028")
                    gd.unlink("zz028")
                    filetoDel = "\"" + f + ".idr" + "\""
                    filetoDel = filetoDel.replace ("/", "\\")
                    filetoDel = filetoDel.replace ("\\", "\\\\")
                    cur.execute ("DELETE FROM securenote WHERE FILE = " + filetoDel)
                    conn.commit()
                    n += 100 / len (fileD)
                    if n > 100:n = 70
                    else:
                        progress['value'] = n
                        secNoteP.update_idletasks()
                logLab = Label (secNoteP, text = "   Shredding successful - 100%", bg = "#363277", fg = "WHITE")
                logLab.place (x = 100, y = 517)
    
    def secOpen():
        def readIt():
            fileCont = filetoOpen.read()
            txt.delete ("1.0", END)
            txt.insert (INSERT, fileCont)
            txt.focus_force()
            secNoteP.title ("iDER Secure Note : " + newF2d.rpartition ("seton/")[2])
            filetoOpen.close()
            gd.system ("del " + "\"" + newF2d.replace ("/", "\\") + "\"")
            conn.commit()

        cur.execute ("SELECT file FROM securenote WHERE user_login = " + "\"" + u_ + "\" ")
        for p in cur: #temp uh
            p = p[0]
            gd.system (anon + "\"" + p + "\"" + " -h -r -s -a")
            clr()
        secO = fd.askopenfilename (master = secNoteP, title = "Select file", initialdir = secPth)
        cur.execute ("SELECT file FROM securenote WHERE user_login = " + "\"" + u_ + "\" ")
        for p in cur:
            p = p[0]
            gd.system (anon + "\"" + p + "\"" + " +h +r +s +a")
            clr()
        if secO == "":pass
        elif secO.rpartition (".")[2] == "idr":
            #lFile = "\"" + secO + "\""
            #lFile = lFile.replace ("/", "\\")
            #gd.system (anon + lFile + " -h -r -s -a")
            F2d = secO
            newF2d = secO.rpartition (".idr")[0]
            dec (F2d, newF2d, password, bufferSize)
            filetoOpen = open (newF2d, "r")
            readIt()
        else:
            value = mb.askokcancel ("Error", "Not an iDER Secure Note File, \nCancel or Press Ok to continue")
            if value == "cancel":pass
            else:
                newF2d = secO #.rpartition (".idr")[2]
                filetoOpen = open (newF2d, "r")
                readIt()

    def secSave():
        def writeTo(p):
            saveFile = open (p, "w+")
            saveFile.write (value)
            saveFile.close()
            p = p.replace ("/", "\\")
            gd.system ("move " + "\"" + p + "\"" + " " + "\"" + secPth + "\"")
            fn = p.rpartition ("\\")
            fn = fn [2]
            F2e = secPth + fn
            newF2e = secPth + fn + ".idr"
            enc (F2e, newF2e, password, bufferSize)
            gd.system ("del " + "\"" + F2e + "\"")
            gd.system (anon + "\"" + newF2e + "\"" + " +h +r +s +a")
            t = time.localtime()
            #get current date in the right format
            y, m, d = str(t[0]), str(t[1]), str(t[2])
            curDate = y + " " + m + " " + d
            curDate = curDate.replace (" ", "-")
            #get current time in the right format
            h, m, s = str(t[3]), str(t[4]), str(t[5])
            curTime = h + " " + m + " " + s 
            curTime = curTime.replace (" ", ":")
            file_name = newF2e.replace ("\\", "\\\\") #replacing single "\" with multiple "\\\\" so sql would save the path the right way
            cur.execute ("INSERT INTO securenote (FILE, user_login, DATE, TIME) VALUES (" + "\"" + file_name + "\"" + ", " + "\"" + u_ + "\"" + ", " + "\"" + curDate + "\"" + ", " + "\"" + curTime + "\"" + ")")#save path in database
            conn.commit()
            secNoteP.title ("iDER Secure Note : " + fn)
            clr()

        value = txt.get ("1.0", END)
        txt.focus_force()
        p = fd.asksaveasfilename (master = secNoteP, title = "Save file as", filetypes = [("Text Document",".txt"), ("Python Files",".py"), ("C++",".cpp"), ("Hyper Text Markup Language",".html"), ("PHP Hypertext Preprocessor",".php")])
        p2 = p.rpartition ("/")[2]
        p2 = p2 + ".idr"
        nValue = p2 in gd.listdir(secPth) 
        if p == "":pass
        elif nValue == True:
            questVal = mb.askquestion ("Error", "File already exists\nWould you like to replace it?")
            if questVal == "yes":
                f = secPth + p2
                F2d = f #unlike system, enc doesnt require the path to the quoted
                newF2d = f.rpartition (".idr")[0]
                dec (F2d, newF2d, password, bufferSize)
                gd.system (anon + "\"" + F2d.replace ("/", "\\") + "\"" + " -h -r -s -a")
                gd.system ("del " + "\"" + F2d.replace ("/", "\\") + "\"")
                f = newF2d
                filetoDel = "\"" + f + ".idr" + "\""
                filetoDel = filetoDel.replace ("/", "\\")
                filetoDel = filetoDel.replace ("\\", "\\\\")
                cur.execute ("DELETE FROM securenote WHERE FILE = " + filetoDel)
                conn.commit()
                writeTo (p)
            else:
                secSave()
        else:
            writeTo(p)

    def pickSaveEvent (event):
        secSave()

    def pickOpenEvent (event):
        secOpen()

    def pickIderEvent (event):
        iDer()

    def pickNoteEvent (event):
        secNote()
        
    secNoteP = Tk()
    secNoteP.configure (background = "#363277")
    secNoteP.title("iDER Secure Note")
    #secNoteP.iconbitmap (relPth + "\\Include\\images\\logo.ico")
    ico = PhotoImage(master = secNoteP, file=relPth + "\\Include\\images\\logo.png")
    secNoteP.call('wm', 'iconphoto', secNoteP._w, ico)
    secNoteP.geometry("858x538+340+150")
    menubar = Menu(secNoteP)
    filemenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Run", menu=filemenu)
    filemenu.add_command(label="Save (Ctrl+Shift+S)", command=secSave)
    filemenu.add_command(label="Open (Ctrl+Shift+O)", command=secOpen)
    helpmenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Options", menu=helpmenu)
    helpmenu.add_command(label="Update", command=updateF)
    helpmenu.add_command(label="About Us", command=abtF)
    helpmenu.add_command(label="Guide", command=howtF)
    helpmenu.add_command(label="Help", command=dontF)

    secNoteP.config(menu=menubar)
    txt = Text(secNoteP, width = 104, height = 32, wrap = WORD)
    txt.place(x=0, y=0)
    txt.focus_force()
    txt.bind ("<Control-S>", pickSaveEvent)
    txt.bind ("<Control-O>", pickOpenEvent)
    txt.bind ("<Control-I>", pickIderEvent)
    txt.bind ("<Control-N>", pickNoteEvent)
    txt.bind ("<Control-D>", doDel)
    txt.bind ("<Control-T>", doTrunc)
    secNoteP.resizable(False, False)
    secNoteP.mainloop()
