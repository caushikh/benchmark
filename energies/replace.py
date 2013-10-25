orig = open('/raid1/home/bb/caushikh/T60/run1/protocols/energy.inp','r')
new = open('energy.inp','w')

orig_rstruct = open('/raid1/home/bb/caushikh/T60/run1/protocols/read_struc.cns','r')
new_rstruct = open('read_struc.cns','w')

orig_files = open('/raid1/home/bb/caushikh/T60/run1/structures/it1/file.cns','r')
new_files = open('file.cns','w')

out_short = 'NEWIT:analysis/energies.disp'
out_full = 'energies.disp'

rstruct_path = 'RUN:protocols/read_struc.cns'
rstruct_new = 'read_struc.cns'
orig_files_path = 'PREVIT:file.cns'
new_files_path = 'file.cns'

rundir = 'RUN:'
newrundir = '/raid1/home/bb/caushikh/T60/run1/'
previt = 'PREVIT:'
newit = 'NEWIT:'
fullpath = '/raid1/home/bb/caushikh/T60/run1/structures/it1/'

loop = 'while ($count le $Iterations.anastruc) loop main'
cond = 'if ($count ge $Iterations.anastruc) then exit loop main end if'

struc = 2
count = '$count = '

while 1:
	tempstr = orig.readline() 
	if tempstr == '':
		break
	if tempstr.find(loop) != -1:
		continue
	if tempstr.find(cond) != -1:
		orig.readline()
		orig.readline()
		continue
	if (tempstr.find('mean') != -1) | (tempstr.find('stdev') != -1):
		continue
	tempstr = tempstr.replace(rstruct_path,rstruct_new)
	tempstr = tempstr.replace(orig_files_path,new_files_path)
	tempstr = tempstr.replace(rundir,newrundir)
	tempstr = tempstr.replace(previt,fullpath)
	tempstr = tempstr.replace(out_short,out_full)
	tempstr = tempstr.replace(newit,fullpath)
	if (tempstr.find(count) != -1):
		pos = tempstr.find(count)
		tempstr = tempstr.replace(tempstr[pos + len(count)], str(struc))
	new.write(tempstr)
while 1:
	tempstr = orig_rstruct.readline()
	if tempstr == '':
		break
	tempstr = tempstr.replace(rundir,newrundir);
	new_rstruct.write(tempstr) 
while 1:
	tempstr = orig_files.readline()
	if tempstr == '':
		break
	tempstr = tempstr.replace(previt,fullpath)
	new_files.write(tempstr);

orig.close()
orig_rstruct.close()
orig_files.close()
new_rstruct.close()
new_files.close()
new.close()
