#!/usr/bin/python
def namer():
	return "success"

level_two_hash = {'your': namer()}
level_one_hash = {'what': level_two_hash}
x = level_one_hash
response_analyse = ['what','your', 'name']
ignore = 0
for sen_counter in range(0, len(response_analyse)):
	print response_analyse[sen_counter]
#depth_counter = 0
#if(depth_counter <= len(response_analyse)):
	if (ignore != 1):
		x = x[response_analyse[sen_counter]]
		print x
		if(isinstance(x, str) == True):
			ignore = 1
		sen_counter = sen_counter + 1
print x + "is the final result"
     

