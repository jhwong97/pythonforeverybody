import re

fn = input()
fh = open(fn)

count = 0

# To filter the line and extract the only interested data
for line in fh:
    line = line.rstrip()
    item = re.findall('[0-9]+', line)
    if len(item) == 0 : continue
    
# To convert string into int and sum it out
    for x in item:
        x = int(x)
        count = count + x
print(count)