import subprocess

fr = open('generate_prot12.inp','r')		# general cns file
fw = open('temp_generate_prot12.inp','w')	# specific structure files
complex = open('complexes.txt','r')		# lists all benchmark complexes
out = open('out.log','w')			

for file in complex:
	file = file[0:4]
	print file
	pdb_infile = file + '.pdb' 
	pdb_outfile = 'proton_coord/' + file + '.pdb'
	psf_outfile = 'proton_struct/' + file + '.psf'

	for line in fr:
		if line.find('coordinate_infile=') != -1:
			templst = line.split('"')
			line = line.replace(templst[1],pdb_infile)
		#coordinate outfile
		if line.find('coordinate_outfile=') != -1:
			templst = line.split('"')
			line = line.replace(templst[1],pdb_outfile)
		#structure outfile
		if line.find('structure_outfile=') != -1:
			templst = line.split('"')
			line = line.replace(templst[1],psf_outfile)
		fw.write(line)
	fw.close()
	fw = open('temp_generate_prot12.inp','r')
	subprocess.call(["cns_solve"],stdin=fw,stdout=out)
	fw.close()
	subprocess.call(["rm","-rf","temp_generate_prot12.inp"])
	fr.seek(0,0)
	fw = open('temp_generate_prot12.inp','w')
fr.close()
fw.close()
out.close()
complex.close()
