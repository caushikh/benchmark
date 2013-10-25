import subprocess

fr = open('1to1nbc.inp','r')		# general cns file
fw = open('temp_1to1nbc.inp','w')	# specific structure files
complex = open('complexes.txt','r')	# lists all benchmark complexes
out = open('out.log','w')	

for protein in complex:
	if (len(protein) == 9 or protein[8] == ' '):
		# find non-bonded contacts
	protein = protein[0:4]
	pdb_infile = file + '.pdb' 
	pdb_outfile = 'proton_coord/' + file + '.pdb'
	psf_outfile = 'proton_struct/' + file + '.psf'

	print protein
