import os
import time

print
print "+++++++++++++++++++"
print
print " Simple Diff v0.1"
print
print "+++++++++++++++++++"
print

file1_in_PWD = raw_input('Is file 1 in the current directory [Y/N] : ')

if file1_in_PWD == 'Y' or 'y' or 'Yes' or 'yes':
	File1 = raw_input('File 1 : ')
	file1_path = os.path.join(os.getcwd(), File1)
elif file1_in_PWD == 'N' or 'n' or 'No' or 'no':
	File1 = raw_input('Enter full path to file 1: ')


file2_in_PWD = raw_input('Is file 2 in the current directory [Y/N] : ')

if file2_in_PWD == 'Y' or 'y' or 'Yes' or 'yes':
	File2 = raw_input('File 2 : ')
	file2_path = os.path.join(os.getcwd(), File2)
elif file2_in_PWD == 'N' or 'n' or 'No' or 'no':
	File2 = raw_input('Enter full path to file 2: ')

write_to_file = raw_input('Write output to file ? [Y/N]' )

if write_to_file == 'Y' or 'y' or 'Yes' or 'yes':
	write_to_file = True
elif write_to_file == 'N' or 'n' or 'No' or 'no':
	write_to_file = False
	
time.sleep(1.0)


print
print
print "File 1 Path is : " , file1_path
print "File 2 Path is : " , file2_path
time.sleep(1.0)

file1_path = file1_path.replace('\\','/')
file2_path = file2_path.replace('\\','/')

file1_open = open(file1_path,"r")
file2_open = open(file2_path,"r")

open_file_time_start = time.time()
f1_line = file1_open.readline()
f2_line = file2_open.readline()
open_file_time_stop = time.time()
print
print
print "Comparing Files -",File1, "and",File2
print
time.sleep(1.0)


print


diff_file_time_start = time.time()

line_no = 1
diffs_found = False
count = 0

while f1_line != '' or f2_line != '':
	f1_line = f1_line.rstrip()
	f2_line = f2_line.rstrip()
	if f1_line != f2_line:
		diffs_found = True
		count += 1
		if f2_line == '' and f1_line != '':
			print">>>+", "Line-%d" % line_no, f1_line
		elif f1_line != '':
			print">>>", "Line-%d" % line_no, f1_line
		if f1_line == '' and f2_line != '':
			print"<<<+", "Line-%d" % line_no, f2_line
		elif f2_line != '':
			print"<<<", "Line-%d" %  line_no, f2_line
		print""
	
	f1_line = file1_open.readline()
	f2_line = file2_open.readline()
	
	line_no += 1

file1_open.close
file2_open.close

diff_file_time_stop = time.time()	


print
if diffs_found == False:
	print "Complete, files identical."
elif diffs_found == True:
	print "Complete,",count, "differences found."
print
print
load_time = open_file_time_stop - open_file_time_start
diff_time = diff_file_time_stop - diff_file_time_start
print "File Load Time - ", load_time 
print "File Diff Time - ", diff_time
print "Run Time - ", load_time + diff_time
