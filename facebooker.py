#!/usr/bin/python
import commands
update = raw_input("What do you want to post as a facebook status?")
commands.getoutput('fbcmd status '+ update)
