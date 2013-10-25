import subprocess

START = -11
END = -7


slist = open('../complexes.txt','r')
flist = open('files/file.cns','r')
new_flist = open('files/temp_file.cns','w')
fstring = 'filenames.bestfile_1'
rstruct = open('files/read_struc.cns','r')
new_rstruct = open('files/temp_read_struc.cns', 'w')
energy = open('files/energy.inp','r')
new_energy = open('files/temp_energy.inp','w')
out = open('out.log','w')

for struct in slist:
	# modify cns files to match structure
	struct = struct[0:4]
	# modify file.cns
	for line in flist:
		if (line.find(fstring) != -1):
			line = line.replace(line[START:END],struct) 
		new_flist.write(line)
	# modify read_struc file
	line = rstruct.readline()
	line = line.replace(line[START:END],struct)	
	new_rstruct.write(line)
	for line in rstruct:
		new_rstruct.write(line)
	# modify energy file
	for line in energy:
		if (line.find('file.cns') != -1):
			line = line.replace('file.cns', 'files/temp_file.cns')
		if (line.find('read_struc.cns') != -1):
			line = line.replace('read_struc.cns', 'files/temp_read_struc.cns')
		if (line.find('energies.disp') != -1):
			line = line.replace('energies.disp','files/'+struct+'energies.disp')
		new_energy.write(line)
	new_flist.close()
	new_rstruct.close()
	new_energy.close()

	# open for reading
	new_energy = open('files/temp_energy.inp','r')
	subprocess.call(["cns_solve"],stdin=new_energy,stdout=out)
	new_energy.close()
	subprocess.call(["rm","-rf","files/temp_file.cns"])
	subprocess.call(["rm","-rf","files/temp_energy.inp"])
	subprocess.call(["rm","-rf","files/temp_read_struc.cns"])
	flist.seek(0,0)
	rstruct.seek(0,0)
	energy.seek(0,0)
	new_flist = open('files/temp_file.cns','w')
	new_rstruct = open('files/temp_read_struc.cns','w')
	new_energy = open('files/temp_energy.inp','w')

slist.close()
flist.close()
new_flist.close()
rstruct.close()
new_rstruct.close()
energy.close()
new_energy.close()
out.close()
