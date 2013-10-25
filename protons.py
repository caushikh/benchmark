fr = open("generate_prot12.inp",'r')
fw = open("temp_generate_prot12.inp",'w')
complex = open("complex.txt",'r')

pdb_infile = '1AHW.pdb' 
pdb_outfile = 'proton_coord/1AHW.pdb'
psf_outfile = 'proton_struct/1AHW.psf'

while 1:
	file = complex.readline()
	if file == "":
		break
	file = file[0:4] 
	pdb_infile = file + '.pdb' 
	pdb_outfile = 'proton_coord/' + file + '.pdb'
	psf_outfile = 'proton_struct/' + file + '.psf'

	# read and copy proton file, making modifications 
	
	while 1:
		tempstr = fr.readline()
		#end of file
		if tempstr == "":
			break
		#infile
		if tempstr.find('coordinate_infile=') != -1:
			templst = tempstr.split('"')
			tempstr = tempstr.replace(templst[1],pdb_infile)
		#coordinate outfile
		if tempstr.find('coordinate_outfile=') != -1:
			templst = tempstr.split('"')
			tempstr = tempstr.replace(templst[1],pdb_outfile)
		#structure outfile
		if tempstr.find('structure_outfile=') != -1:
			templst = tempstr.split('"')
			tempstr = tempstr.replace(templst[1],psf_outfile)

		fw.write(tempstr)
fr.close()
fw.close()



