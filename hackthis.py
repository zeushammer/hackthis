import sys, os, shlex, time, md5

#show blinking cursor, disable keyboard entry
#wait
#print "Encrypting connection..."
#print "Generating RSA/DXS algorthim key..."
# print random 200 random characters medium speed or md5 hash
#print "Connected....welcome back hacker."
# wait

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
from Tkinter import END

class simpleapp_tk(Tkinter.Tk):
# ^ make simpleapp_tk a full blown Tk with access to all tools

    def __init__(self,parent):
        Tkinter.Tk.__init__(self, parent)
        # ^ initialize the super class
        self.parent = parent
        # ^ global parent
        self.initialize()
        # ^ run to build the window

    def initialize(self):
        # create a grid
        self.grid()

        # Your computer nameplate
        self.serverLabel = Tkinter.Label(text="Your Computer:")
        self.serverLabel.grid(column=0,row=0,columnspan=1,sticky='W')

        # Connected server nameplate
        self.serverLabel = Tkinter.Label(text="Server: INSERT NAME HERE")
        self.serverLabel.grid(column=1,row=0,columnspan=1,sticky='W')

        # Server response
        self.serverlog = Tkinter.Text(state='disabled', width=80, height=24, wrap='none', bg='black', fg='white')
        self.serverlog.grid(column=1,row=1,columnspan=1,sticky='EW')

        # Local system response
        self.log = Tkinter.Text(state='disabled', width=80, height=24, wrap='none', bg='black', fg='green')
        self.log.grid(column=0,row=1,columnspan=1,sticky='EW')

        # Text command line
        self.entry = Tkinter.Entry(self, bg='black', fg='green')
        self.entry.grid(column=0,row=3,columnspan=2,sticky='EW')

        #Capture the Return key
        self.entry.bind("<Return>", self.OnPressEnter)
        
        #Capture the Backspace key
        self.entry.bind("<BackSpace>", self.OnPressBackSpace)
        
        #Insert the first > in the console
        self.entry.insert(0, '> ')

        #Put the cursor in the box
        self.entry.focus()        

        ## ???
        self.grid_columnconfigure(0,weight=1)
        self.resizable(True,False)

        self.welcomeUser()

    def writeToScreen(self, msg):
        #numlines = self.log.index('end - 1 line').split('.')[0]
        self.log['state'] = 'normal'
        #if numlines==24:
        #    self.log.delete(1.0, 2.0)
        #if self.log.index('end-1c')!='1.0':
        #    self.log.insert('end', '\n')
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

    def typewriter(self, screen, msg, pace):

        for char in msg:
            if screen == "client":
                self.log['state'] = 'normal'
                self.log.insert('end', char)
                self.log['state'] = 'disabled'
            if screen == "server":
                self.serverlog['state'] = 'normal'
                self.serverlog.insert('end', char)
                self.serverlog['state'] = 'disabled'
            self.log.update()
            time.sleep(pace)

    def welcomeUser(self):
        self.typewriter("client", "Initializating connection to secure server", 0.025)
        self.typewriter("client", "...\n", 0.10)
        self.typewriter("client", "Encrypting connection", 0.025)
        self.typewriter("client", "...\n", 0.025)
        self.blinkCursor(3)
        self.typewriter("client", "Generating RSA/DXS algorthim key", 0.025)
        self.typewriter("client", "...\n", 0.025)
        self.blinkCursor(2)
        # # print random 200 random characters medium speed
        self.typewriter("client", "Connected...\n", 0.025)
        self.typewriter("client", "Welcome back hacker\n\n\n", 0.025)

    def blinkCursor(self, times):
        for x in range(0, times):
            self.log['state'] = 'normal'
            self.log.insert('end', '_')
            # take the string currently in the widget, all the way up to the last character
            txt = self.log.get("1.0",END)[:-1]
            txt = txt[:-1]
            self.log.update()
            time.sleep(0.4)
            # clear the widget of text
            self.log.delete("0.0", END)
            # insert the new string, sans the last character
            self.log.insert("0.0", txt)
            self.log['state'] = 'disabled'
            self.log.update()
            time.sleep(0.4)

    def OnPressBackSpace(self, event):

        #get what is in the textbox
        prevTypedText = self.entry.get()

        # entry.get() captures what the input looked like BEFORE the bksp key
        # was hit. Stupid. So I have to take the text captured and subtract one
        # letter to get the currentText in the box
        currentText = prevTypedText[:-1]

        # If the user deleted the space after the carrot, re-insert it
        if currentText == '>':
            #delete what is in the text box
            self.entry.delete(0, len(self.entry.get()))
            
            # insert the correctly formatted prompt    
            self.entry.insert(0, ">  ")
            # ^ a double space is needed instead of " " I had to use "  "

    def OnPressEnter(self,event):
        
        # strip the command of "> " and send the command off to be interpeted
        self.interpet(self.entry.get()[2:])

        # delete the command typed in the textbox
        self.entry.delete(0, len(self.entry.get()))

        # insert the prper command line prompt
        self.entry.insert(0, '> ')

    def interpet(self, command):
        validCommands = ['connect', 'serverinfo', 'ls']
        # write the command to the screen
        self.writeToScreen(command + '\n')
        # write to debug screen
        print 'Command: "%s"' % command

        # get the keyword attempted
        if command.find(' ') > 0:
            keyword = command[:command.find(' ')]
        else:
            keyword = command

        # write to debug screen
        print 'keyword: "%s"' % keyword        

        while True:
            if keyword not in validCommands:
                self.writeToScreen('Invalid Command\n')
                break

            #dict mapping commands to methods for easy selection
            dictCommands = {'connect': self.connect, 'serverinfo': self.serverinfo, 'ls': self.ls}

            #get the args from the string
            args = shlex.split(command[command.find(' '):])

            # print out args on debug console
            for arg in args:
                print arg

            #run method with args
            dictCommands[keyword](args)
            
            # end main loop
            break

    def connect(self, args):
        print 'connect method running'
        print len(args)
        if len(args) != 1:
            self.writeToScreen('Invalid parameters\n')
        else:
            self.typewriter("client", 'Attempting to connect to: ' + args[0] + '...\n', 0.025)

    def serverinfo(self, args):
        self.writeToServerLog('Probing server for info...\n')
        for i in range(1, 5):
            self.writeToServerLog(">"*i)
            time.sleep(0.25)
        self.writeToServerLog('OS: Redhat Linux 3.4.15\n')

    def ls(self, args):
        self.typewriter('client','Installed programs: connect ls serverinfo', 0.025)

if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('my application')
    app.mainloop()