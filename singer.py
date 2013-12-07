#!/usr/bin/python
import commands
choice = raw_input("Which song would you like me to play?\n")
choice = choice.split()
choice =  ''.join(choice)
commands.getoutput('vlc ' + choice + '.mp3')

