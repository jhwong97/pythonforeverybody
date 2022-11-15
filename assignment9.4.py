# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
name = input("Enter file name: ")
handle = open(name)

counts = dict()

# To read each line and filter out lines which do not start with 'From'

for line in handle:
    if not line.startswith ('From '):
        continue
    words = line.split() #To split the words into list
    word = words[1]
    counts[word] = counts.get(word,0) + 1 #To add the words into dict()

#To calculate the most prolific comitter

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)