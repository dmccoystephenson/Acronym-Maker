originalString = raw_input("Enter what you want to make into an acronym: ")

list = originalString.split(" ")

acronym = ""

for x in list:
	acronym = acronym + x[:1]
	
print "Your new acronym is %r" % acronym

raw_input("Press 'Enter' to exit the program.")