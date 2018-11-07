#!/bin/bash
#
# Replaces all the strings that has the same name as their filename
# and will be replaced by the filename without underscode
#
# Eg: assume there is a file called a_b_c.txt
# Input : Inside the a_b_c.txt file and some content a_b_c
# Output: Inside the abc.txt file and some content abc
#
# Format replace.sh <folder path> <file extension>
# Example1: ./replacewithoutUnderscore.sh.sh /Users/hewapathirana/Desktop/ txt
# Example1: ./replacewithoutUnderscore.sh.sh /Users/hewapathirana/Desktop/ *
#
# Author: Suresh Hewapathirana

echo "replacement Started!"

for file in $1/*.$2
do
  # get full file name including file extension
  fullFilename=$(basename -- "$file")
  # get only file name
  filename="${fullFilename%.*}"
  # remove all underscores
  corrected="${filename//_}"
  echo "${filename} --> ${corrected}"
  # replace filename with the corrected file name globally(all the occurrences)
  #sed -i "s/$filename/$corrected/g" $file
  sed -i -e "s/$filename/$corrected/g" $file  # for mac uses
done

echo "replacement completed!"
