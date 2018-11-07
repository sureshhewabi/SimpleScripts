#!/usr/bin/env python3
#
# Replaces all the text with new text and save into a new file
#
# Input: This is the sample text with the word old word and I want to replace old word with new word
# Output: This is the sample text with the word new word and I want to replace new word with new word
#
# Format python3 replaceText.py -inf  <input file> -o "old" -n "new" -outf <output file>
# Example1: python3 replaceText.py -inf in.txt -o "old word" -n "new word" -outf out.txt
#
# Author: Suresh Hewapathirana

import argparse

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-inf", "--infile", required=True, help="Input filenamer")
ap.add_argument("-o", "--oldtext", required=True, help="The text that is need to be replaced")
ap.add_argument("-n", "--newtext", required=True, help="The new text that will be replaced")
ap.add_argument("-outf", "--outfile", required=True, help="Output filename")
args = vars(ap.parse_args())

# assign values of the arguments
filein = args["infile"]
fileout = args["outfile"]
old_data =args["oldtext"]
new_data = args["newtext"]

print("Starting reading the input file..")
f = open(filein,'r')
filedata = f.read()
f.close()

print("Replacing the old data with new ones...")
newdata = filedata.replace(old_data, new_data)

print("Writting to a new file...")
f = open(fileout,'w')
f.write(newdata)
f.close()
