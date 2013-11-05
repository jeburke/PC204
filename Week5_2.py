import sys
import urllib
import re

def get_pdb_ligands(pdb):
	f = urllib.urlopen("http://www.rcsb.org/pdb/rest/ligandInfo?structureId=" + pdb)
	ligands = []
	for line in f:
		match = re.search(r"<chemicalName>([^<]*)</chemicalName>", line)
		if match:
			ligands.append(match.group(1))
	f.close()
	return ligands

print ', '.join(get_pdb_ligands(sys.argv[1]))

