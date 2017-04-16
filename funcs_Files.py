def print_line(line_number, f):
    print line_number, f.read_line()

file_pntr = open(sample.txt)
print_line(2, file_pntr)