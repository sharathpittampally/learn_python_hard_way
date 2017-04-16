from sys import argv
script, file = argv

#open file.
txt = open(file)

print "Here is your file name: %r" % file
print "Here are its contents: "

#print out its contents.
print txt.read()
txt.close()

print "Type the file name again: "
file_name = raw_input(">")
print "Here are the contents again for you: "
txt_file = open(file_name)
print txt_file.read()
txt_file.close()

