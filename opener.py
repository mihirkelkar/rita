from rita import opener
import commands
import re
browsers = ['chrome', 'google-chrome', 'firefox', 'mozilla', 'safari', 'opera']
response_analyse = response_analyse[1:]
print response_analyse
match = re.search(r'[\w\d-]+\.[\w]+', response_analyse[0])
if match:
	print "I am in"
	if(response_analyse[1]) in browsers:
		if response_analyse[1] == 'chrome':
			response_analyse[1] = 'google-chrome'
		if response_analyse[1] == 'mozilla':
			response_analyse[1] = 'firefox'		
		commands.getoutput(response_analyse[1] + ' ' + response_analyse[0])
	else:
		commands.getoutput('google-chrome ' + response_analyse[0])
else:
	if response_analyse[0] in browsers:
		if response_analyse[0] == 'chrome':
			response_analyse[0] = 'google-chrome'
		if response_analyse[0] == 'mozilla':
			response_analyse[0] = 'firefox'
	commands.getoutput(response_analyse[0])
	
