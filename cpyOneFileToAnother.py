print "Enter source file: "
s = raw_input(">")
print "Enter destination file: "
d = raw_input(">")
sopen = open(s)
dopen = open(d,"w")
dopen.write(sopen.read())
print "Data copied successfully!"
sopen.close()
dopen.close()