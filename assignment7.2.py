# Use the file name mbox-short.txt as the file name
# Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines 
# and compute the average of those values and produce an output as shown below. 
# Do not use the sum() function or a variable named sum in your solution.

fname = input("Enter file name: ")
fh = open(fname)
count = 0
fvalue = 0
for line in fh:
    line = line.rstrip()