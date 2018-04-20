#!/usr/bin/env python3

filein = '<input file path>'
fileout = '<output file path>'
old_data = 'old_data'
new_data = 'new'

# Read the input file and copy it to the memory
f = open(filein,'r')
filedata = f.read()
f.close()

# Replace the old data with new ones
newdata = filedata.replace(old_data, new_data)

# Write it to a new file
f = open(fileout,'w')
f.write(newdata)
f.close()
