import os

files = os.listdir(os.getcwd())
f = open('complexes.txt')
miss = open('missing.txt','w')
for line in f:
	found = 0
	line = line[0:4]
	for i in files:
		if (i[0:4] == line):
			found = 1
			break	
	if not found:
		print line, 'is missing'
		miss.write(line + '\n')
	
f.close()
	
