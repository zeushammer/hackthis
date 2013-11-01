import sys, os, urwid

print "Initializating connection handshake to secure server..."
#show blinking cursor, disable keyboard entry
#wait
print "Encrypting connection..."
print "Generating RSA/DXS algorthim key..."
# print random 200 random characters medium speed
print "Connected....welcome back hacker."
# wait

# while true
print ">"
# wait for input
# if input not in command list
# print "Command Not Found"
# else
# run command

# commands
# > begin hacking
#  -> show on server response terminal (SRT): "Connected to server X"
# \> run serverinfo
#  -> show on SRT: info about target, searching for relevant exploit, found THIS
# \> load payload THIS
# \> initiate hack payload
#  -> "spit out attempt to hack"
# if hack fails, then username/password crack
# else hack successful, hacker on the server
#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import Tkinter

class simpleapp_tk(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()

        # Text command line
        self.entry = Tkinter.Entry(self)
        self.entry.grid(column=0,row=1,columnspan=2,sticky='EW')
        self.entry.bind("<Return>", self.OnPressEnter)

        # Server response
        self.serverlog = Tkinter.Text(state='disabled', width=80, height=24, wrap='none', bg='black', fg='white')
        self.serverlog.grid(column=0,row=0,columnspan=1,sticky='EW')
        self.serverlog.grid(column=1,row=0)

        #label = Tkinter.Label(self, anchor="w",fg="white",bg="blue")
        #label.grid(column=0,row=1,columnspan=2,sticky='EW')

        # Local system response
        self.log = Tkinter.Text(state='disabled', width=80, height=24, wrap='none')
        self.log.grid(column=0,row=0,columnspan=1,sticky='EW')

        self.grid_columnconfigure(0,weight=1)
        self.resizable(True,False)

    def OnButtonClick(self):
        print "You clicked the button !"

    def OnPressEnter(self,event):
        print "You pressed enter !"
        self.writeToLog(self.entry.get())
        self.entry.delete(0, len(self.entry.get()))

    def writeToLog(self, msg):
        numlines = self.log.index('end - 1 line').split('.')[0]
        self.log['state'] = 'normal'
        if numlines==24:
            self.log.delete(1.0, 2.0)
        if self.log.index('end-1c')!='1.0':
            self.log.insert('end', '\n')
        self.log.insert('end', msg)
        self.log['state'] = 'disabled'    

    def writeToServerLog(self, msg):
        numlines = self.serverlog.index('end - 1 line').split('.')[0]
        self.serverlog['state'] = 'normal'
        if numlines==24:
            self.serverlog.delete(1.0, 2.0)
        if self.serverlog.index('end-1c')!='1.0':
            self.serverlog.insert('end', '\n')
        self.serverlog.insert('end', msg)
        self.serverlog['state'] = 'disabled'

if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('my application')
    app.mainloop()
