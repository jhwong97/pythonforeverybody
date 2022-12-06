# Assignment7.1
# Use words.txt as the file name

fname = input("Enter file name:")
try:
    fh = open(fname)
except:
    print("The file is not found in the location,", fname)
    quit()

for line in fh:
    line = line.rstrip().upper()
    print(line)