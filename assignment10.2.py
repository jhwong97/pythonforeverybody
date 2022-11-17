name = input('Enter the file name: ')
fh = open(name)

counts = dict()

for line in fh:
    if not line.startswith("From "):
        continue
    word = line.rstrip().split(":")
    time = str(word[0]).split()
    hour = time[-1]
    counts[hour] = counts.get(hour,0) + 1

lst = sorted(counts.items())

for k,v in lst:
    print(k,v)