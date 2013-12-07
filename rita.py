#!/usr/bin/python
import re
from time import gmtime, strftime
import urllib
import json as m_json
import random
import commands
import subprocess
import os
#---------------------------------------------------------------------------------------------------------------------------------------------------------
#                       THE MACHINE LEARNING UNIT FILES BEING PICKED UP FROM THE SYSTEM

fp = open('hash_key', 'r')
op = open('hash_value', 'r')

#--------------------------------------------------------------------------------------------------------------------------------------------------------
def opener(response_analyse):
	return 'opener.py'
def joker():
	return 'joker.py'
def whats_up():
	return 'hi there'
def caller_song():
	return 'singer.py'
def thanker(name_final):
	return 'thanker.py'
def thankerrebut(name_final):
	return 'thanker_me.py'
def facebooker(response_analyse):
	return 'facebooker.py'
#__________________________________________________________________________________________________
#THIS FUNCTION RETURNS THE TIME AS PER REQUESTED, EITHER AS SYSTEM TIME OR GOOGLE QUERY.
#STATUS: CAN RETURN SYSTEM TIME TO MOST INPUTS
#UNDER DEVELOPMENT ON 16/09/2012
def timegetter(response_analyse):
#			lock()
			location_found = 0
			for i in response_analyse:
				if(i not in ['time','date',"today",'right','right' 'now', 'here','what', 'whats']):
					location = i
					location_found = 1
			if (location_found == 1):
				query = location + ' time'
				time = str(google_search(query))
				return time
			else:
				time =  strftime("%Y-%m-%d %H:%M:%S", gmtime())
				return "The date and time at your location are " + time
#____________________________________________________________________________________________________________________

#
#_____________________________________________________________________________________________________________________
#THIS FUNCTION JUST RETURNS WHAT YOUR NAME IS
#STATUS: FULLY FUNCTIONAL	
def my_namer(name_final):
#		lock()
		return "You are " + name_final
#
def singer():
	#	lock()
        	subprocess.call(['play', 'song.mp3'])
        	
#______________________________________________________________________________________________________________________
#
#______________________________________________________________________________________________________________________
#CODE TELLS YOU ITS OWN NAME HERE
#STATUS: FULLY FUNCTIONAL
def your_namer():
	#	lock()
		return "My name is Rita. But you knew that already"
#
#_____________________________________________________________________________________________________________________

#____________________________________________________________________________________________________________________
#
#LISTS OF VARIOUS KINDS: <<<<<<<<<<<    DATABASE HERE!!      >>>>>>>>>>>>>>
punctuations = [',','!',';','.','?']
common_verbs = ['is','were','are'] 
prepositions = ['in', 'on', 'at', 'about', 'between']
articles = ['the','a','an']
execs = ['singk']# dont know whether a list of execs is required anymore put on standby
text_unique_responses = ['thank', 'thanks', 'tell','sing','play', 'update', 'post', 'open']
deadly_internet_prompters = ['what','why','when','where']
#
#____________________________________________________________________________________________________________________


#_____________________________________________________________________________________________________________________
#SOUL OF THE CODE FUNCTION
def talker(name_final):
	thank_you_count = 0
	thank_me_count = 0
	talk_count = 0 #keeps track of whether this is your first question to RITA
	response_analyse = []#your questions are initialized in this array
#__  - - - - - - - - -- - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - --  - - - -- - - - - - -- - - - -
#
#                                   <<<<<<< <<<<<<<<<<<<< ERMHAGERD HYASHTHABLES>>>>>>>>>>>>>>>>>>>>
# write for what day is today
#what is today's day
#Rule 1:numericlly higher hash level always on top
#Rule 2:All elements of higher hash have to be in immediately lower hash
#LIST OF HASH UNDER DEVELOPMENT LEVEL_TWO_TODAYHASH (for stuff like "what [day] is today" )
	keys = (fp.read()).split('\n')
	values = (op.read()).split('\n')
	knowledge_hash = dict(zip(keys, values))
	level_four_goodhash = {'joke' : joker()}

	level_three_yourhash = {'name':your_namer()}

	level_three_myhash = {'name':my_namer(name_final), 'nme': my_namer(name_final),  'I': my_namer(name_final), 'i': my_namer(name_final), 'Facebook': facebooker(response_analyse), 'facebook': facebooker(response_analyse), 'fb': facebooker(response_analyse), "FB": facebooker(response_analyse),'status':facebooker(response_analyse) }
	
	level_three_mehash = {'good': level_four_goodhash, 'joke': joker(), 'your': level_three_yourhash}
	
	level_two_tellhash = {'me': level_three_mehash, 'joke':joker()}
	
	level_two_todayhash = {'date': timegetter(response_analyse), 'dte': timegetter(response_analyse)}

	level_two_thankhash = {'you': thanker(name_final), 'me': thankerrebut(name_final)}

	level_two_datehash = {'today':timegetter(response_analyse), 'tomorrow': timegetter(response_analyse)}

	level_two_updatehash = {'my' : level_three_myhash}

	level_two_whathash = {'your': level_three_yourhash, 'my': level_three_myhash, 'time':timegetter(response_analyse), 'date': timegetter(response_analyse), 'date': timegetter(response_analyse), 'today': level_two_todayhash, 'todays': level_two_todayhash, "today's": level_two_todayhash, 'up': whats_up()}

	level_two_whohash = {'am': level_three_myhash, 'you': your_namer()}

	level_one_hash = {'what': level_two_whathash, 'who': level_two_whohash, 'your': level_three_yourhash, 'my': level_three_myhash, 'time':timegetter(response_analyse) ,'whats': level_two_whathash, "what's":level_two_whathash, 'date': level_two_datehash,'dte': level_two_datehash, 'today': level_two_todayhash, 'todays': level_two_todayhash, "today's": level_two_todayhash, "thank": level_two_thankhash, 'sing': caller_song(), 'thanks': thanker(name_final), 'tell': level_two_tellhash, 'open': opener(response_analyse), 'update': level_two_updatehash}


#
#
#-------------------------------------------------------------------------------------------------------------------------
#
#
#				<<<<<<<<<<<<<<<<<<< ERMHAGERD LANGUAGE PROCESSOR>>>>>>>>>>>>>>>>>>>>>>
	while 1:
		talk_count = 0
		while 1:
			if talk_count == 0: 
				response = raw_input("What can I help you with?\n>>")#rita's first convo line
				response = response.lower()
				talk_count = talk_count + 1
			else:
			
				response = raw_input("\n>>") #rita's normal convo line
				response = response.lower()
			response_analyse = response.split() #split array for analysis
# -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-..-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-..-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
#
#				CHECK LAST ELEMENT FOR PUNCTUATION MARKS
			if(((response_analyse[-1])[-1]) in punctuations):
				response_analyse[-1] = (response_analyse[-1])[:-1]
#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
#				RESPOND TO THE "CALL ME XYZ" COMMAND
#				STATUS : NOT UPTO MARK. >> SOMEHOW GET IT TO STORE IT AS NAME_FINAL.
			if(response_analyse[0] == "call" and response_analyse[1] == "me" and len(response_analyse) < 5):
				name_final = response_analyse[-1]
				print  name_final
				break
#_.-.-.-.-.-.-..-...-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-..-.-.-
#				THIS PART OF CODE DELETES SUPERFLUOUS ENGLISH WORDS
			todelete = []
			for i in range(0,len(response_analyse)):
				if(i == 0):
					continue
				else:
					if(response_analyse[i] not in common_verbs):
						if(response_analyse[i] not in prepositions):
							if(response_analyse[i] not in articles):
								continue
							else:
								print response_analyse[i]
								todelete.append(response_analyse[i])
						else:
							print response_analyse[i]
							todelete.append(response_analyse[i])
					else:
						print response_analyse[i]
						todelete.append(response_analyse[i])
			for i in todelete:
				response_analyse = filter(lambda x: x != i, response_analyse)
			print response_analyse
			print " ".join(response_analyse)
#-.-.-.-.-.-.-.-.--..-..-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-
#			<<<<<<<<<<<<<<<<<<<<<<<<<<<<THIS PART OF CODE IS THE MAIN EXECUTOR>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#			STATUS: HEAVY DEVELOPMENT REQUIRED
#			IMMEDIATE CONCERN IS: MAKE CODE SAY "NOT FOUND" AND CONTINUE IF HASH TABLE ENTRY IS MISSED
			x = level_one_hash
			ignore = 0
			#glob_to_one()
			for sen_counter in range(0, len(response_analyse)):
				if (ignore != 1):
					final_locker = 0
					try:
#Here, in the line below, I recursively attain hash table names from the entire knowledge base
						x = x[response_analyse[sen_counter]]
					except KeyError:#here I am looking for a hash miss in the main database
							final_locker = 1
							try:#here now, I try looking up the machine learning databse for learned response
								learned_response = knowledge_hash[' '.join(response_analyse)]
							except KeyError:#now, if the machine hasnt learned yet, it will learn here
								web_choice = raw_input("Umm....I don't know that\nWould you like to do a web search? \ny/n")
								if web_choice == 'y' or web_choice == 'Y':
									response_weber = response.split()
									search_term_list = []
									for i in response_weber:
									#RUN SEARCH QUERIES DIRECTLY INTO BROWSER FROM TERMINAL > SWEET BRO!!
										search_term = '%20' + i
										search_term_list.append(search_term)
									search_term = ''.join(search_term_list)
									commands.getoutput('xdg-open http://google.com/search?q='+ search_term)
									break
								else:
									learner = raw_input("Please tell me what would be an appropriate verbal response?")
									if learner not in ['nothing', 'no', "I won't tell", 'I will not tell you','I dont know']:
										knowledge_hash.update({' '.join(response_analyse):learner})
										fap = open('hash_key', 'a')
										fap.write((' '.join(response_analyse)) + '\n')
										fap.close()
										oap = open('hash_value', 'a')
										oap.write(learner + '\n')
										oap.close()
									else:
										print "Okay, sorry I cant do that for you" + name_final
									break
							print learned_response
							break
									   
					#print x
					if(isinstance(x, str) == True):
						ignore = 1
				sen_counter = sen_counter + 1
			if response_analyse[0] in execs:
				commands.getoutput(x)
#______________________________________________________________________________________________________________________________________
#                  THE LINE ABOVE IS NOW REDUNDANT? TAKE A LOOK HERE...
#______________________________________________________________________________________________________________________________________
#_____________________________________________________________________________________________________________________________________

				break
			if(response_analyse[0] in text_unique_responses and re.search(r'.+\.py', x)):
				execfile(x)
#                      IN CASE YOU WANT AN OUTER FUNCTION TO RUN , GO CHANGE THE TEXT UNIQUE RESPONSE LIST ABOVE
				break	
			if final_locker == 0:
				print x

			#glob_to_zero()
		


#Recognition, Interpretation of Text and Analysis. (R.I.T.A)_________________________________________________________________________
#
#
#This is the name segregator unit of R.I.T.A ; it separates your first name from an input string and says hi to you. A regex checks for a space element in a strign. If it finds the space, then it compares each word against a name_aux_list content to segregate your first name. 
#
#_______________________________________________________________________

name_aux_word_list = ['my','nme', 'name', 'is','us','mu','i', 'am', 'called','caled' 'as','this','dis','im',"I'm","i'm"] + punctuations
name_final = raw_input("Hi, whats your name?\n>>")
#print name_final
name_final.lower()
match = re.search(r'\w+\s\w+',name_final)
#print match.group()
if(match):
	name = name_final.split()
	#print name
	name_counter = 0
	for i in name:
		if(i.lower() not in name_aux_word_list):
			name_counter = name_counter + 1
			name_final = i
			break
#print name_final
print "Hi " + name_final+"\n>>"
talker(name_final)
