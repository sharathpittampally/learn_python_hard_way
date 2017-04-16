print "Enter the file name: ",
file = raw_input()
txt = open(file, "w")
txt.write("some junk.")
txt.close()