###
### Single-screen rework hackthis project
###

import sys, os, shlex, time, md5
import Tkinter
from Tkinter import END

class simpleapp_tk(Tkinter.Tk):
# make simpleapp_tk a full replicant of Tk with access to all tools

	def __init__(self, parent):
		Tkinter.Tk.__init__(self, parent)
		# initialize super class
		self.parent = parent
		# global parent
		self.initialize()
		# run to build GUI window

	def initialize(self):
		# create grid
		self.grid()

		self.title('Hack This Ver: 0.2')

		# User's computer name
		self.windowLabel = Tkinter.Label(text="User:")
		self.windowLabel.grid(column=0, row=0, columnspan=1, sticky='W')

		# Local system response
		self.log = Tkinter.Text(state='disabled', width=80, height=24, \
			wrap='none', bg='black', fg='green')
		self.log.grid(column=0, row=1, columnspan=1, sticky='EW')

		# Command Line text
		self.entry = Tkinter.Entry(self, bg='black', fg='green')
		self.entry.grid(column=0, row=3, columnspan=2, stick='EW')

		# Capture the Return key
		self.entry.bind("<Return>", self.OnPressEnter)

		# Capture the Backspace key
		self.entry.bind("<BackSpace>", self.OnPressBackSpace)

		# Insert first carrot in console-log
		self.entry.insert(0, '> ')

		# Put cursor in GUI box
		self.entry.focus()

		## ???
		self.grid_columnconfigure(0, weight=1)
		self.resizable(True, False)

		self.welcomeUser()

	def writeToScreen(self, msg):

		self.log['state'] = 'normal'
		self.log.insert('end', msg)
		self.log['state'] = 'disabled'

	def typeWrite(self, msg, pace):

		for char in msg:
			self.log['state'] = 'normal'
			self.log.insert('end', char)
			self.log['state'] = 'disabled'
		self.log.update()
		time.sleep(pace)

	def welcomeUser(self):
		self.typeWrite("Query for clearance", 0.025)
		self.typeWrite("...\n", 1)
		self.typeWrite("[+] Clearance granted\n", 0)
		self.blinkCursor(3)
		self.typeWrite("Initializing connection to secure server", 0.025)
		self.typeWrite("...\n", 1)
		self.typeWrite("[+] Connection secured\n", 0)
		self.typeWrite("Encrypting connection", 0.025)
		self.typeWrite("...\n", 0.5)
		self.blinkCursor(3)
		self.typeWrite("Generating RSA/DXS algorthim key", 0.025)
		self.typeWrite("...\n", 1)
		self.blinkCursor(3)
		# # print random 200 character at medium speed
		self.typeWrite("[+] Connection successful\n\n", 0.025)
		self.typeWrite("Welcome back hacker\n\n\n", 0.025)

	def sampleHack(self):
		# MOVE TO NEW CLASS
		# Initiate Battering Ram
		# <A>NEB/NJS<EBA>(NETI=3V)MB1-WK
		# (BEM)RAMJET/SYPHON -XP FUNCTIONS
		# TO SECONDARY-SYSTEM{WATC} DEL SWB
		# --SOFTWARE OVERRIDE
		#
		# <P> PROGRAM - SYPHON/CLI
		# <C> MUTABENIC RESEARCH FILES/WES
		# TO-<B> SWITCH K*CODE/MEMORY ALPH
		# NULL/NOID PROCESSION-45
		#
		# ....
		#
		# SECURITY SYSTEM DISABLED

		# or

		# In Soviet Russia, SQL injects you....
		# [+] URL: http://www.suckerdomain.io/videos?dvdId=70
		# [+] Database: sonypictures
		#		User: root@localhost
		#		Version: 5.1.26-rc

		# Open Ports Required for Crack: Overload
		pass

	def blinkCursor(self, times):
		for x in range(0, times):
			self.log['state'] = 'normal'
			self.log.insert('end', '_')
			# take string currently in widget, all the way to last character
			txt = self.log.get('1.0', END)[:-1]
			txt = txt[:-1]
			# update screen outside thread
			self.log.update()
			time.sleep(0.4)
			# clear widget of text
			self.log.delete('0.0', END)
			# insert new string, sans last character
			self.log.insert('0.0', txt)
			self.log['state'] = 'disabled'
			self.log.update()
			time.sleep(0.4)

	def OnPressBackSpace(self, event):

		# get what is in textbox
		prevTypedText = self.entry.get()

		# entry.get() captues what input looked like BEFORE bksp
		# key was pressed. Stupid. So you have to take the text captured and
		# subtract one character to get the currentText in the box
		currentText = prevTypedText[:-1]

		# if the user has deleted the space after the carrot, re-insert it
		if currentText == '>':
			# delete what is in text box
			self.entry.delete(0, len(self.entry.get()))

			# re-insert correctly formatted prompt
			self.entry.insert(0, '>  ')
			# a double space is NEEDED instead of " " used previously

	def OnPressEnter(self, event):

		# strip command of "> " and send command to be interpreted
		self.interpret(self.entry.get()[2:])

		# delete command typed in textbox
		self.entry.delete(0, len(self.entry.get()))

		# re-insert correctly formatted prompt
		self.entry.insert(0, '> ')

	def interpret(self, command):
		validCommands = ['connect', 'serverinfo', 'ls', 'logout']
		# write the command to the screen
		self.writeToScreen('> ' + command + '\n')
		# write to debug screen
		print 'Command: "%s"' % command

		# get the keyword attempted
		if command.find(' ') > 0:
			keyword = command[:comand.find(' ')]
		else:
			keyword = command

		# write to debug screen
		print 'keyword :"%s"' % keyword

		while True:
			if keyword not in validCommands:
				self.writeToScreen('Invalid Command\n')
				break

			# dict mapping commands to mehtods for easy selection
			dictCommands = {'connect': self.connect,
							'serverinfo': self.serverinfo,
							'ls': self.ls,
							'logout': self.logout
							}

			# print args from string
			args = shlex.split(command[command.find(' '):])

			# get args from string
			for arg in args:
				print arg

			# run method with args
			dictCommands[keyword](args)

			# end main loop
			break

	def connect(self, args):
		print 'connect method running'
		print len(args)
		if len(args) != 1:
			self.writeToScreen('Invalid parameters\n')
		else:
			self.writeToScreen('Attempting to connect to: ' + args[0])
			self.typeWrite('...\n', 0.025)

	def serverinfo(self, args):
		self.writeToScreen('Probbing server for info...\n')
		for i in range(1, 11):
			self.typeWrite('>', 1)
			time.sleep(0.25)
		self.writeToScreen('\nOS: Redhat Linux 3.4.15\n')

	def ls(self, args):
		self.writeToScreen('Installed programs:\n')
		self.writeToScreen('connect ls serverinfo logout')

	def logout(self, args):
		self.typeWrite('Logging out', 0.025)
		self.typeWrite('.....\n', 1)
		self.writeToScreen('[Process Completed]')

if __name__ == "__main__":
	app = simpleapp_tk(None)
	app.mainloop()









