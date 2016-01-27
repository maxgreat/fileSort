import glob
import sys
import os

def dirExplore(dirname):
	"""
		Explore a directory, and the sub directory and return everry file with a given extension
	"""
	els = []
	for path in glob.glob(dirname+'/*'):
		if os.path.isdir(path) :
			print(path, 'is a directory')
			els += dirExplore(path)
		elif os.path.isfile(path):
			if '.cbr' in path or '.cbz' in path:
				els.append(path)
	return els
	

def isfloat(value):
	"""
		Test if the value can be cast to float
	"""
	try:
		float(value)
		return True
	except ValueError:
		return False
    
if __name__ == '__main__':
	if len(sys.argv) > 1:
		mainDir = os.path.abspath(sys.argv[1])
	else:
		mainDir = os.path.abspath(os.path.curdir)
	
	l = dirExplore(mainDir)
	listSerie = []
	for comic in l:
		name, ext = os.path.splitext(comic.split('/')[-1])
		tmp = name.split(' ')
		date = tmp[0]
		#verify year
		if len(date.split('-')) != 2:
			continue
		year, month = date.split('-')
		
		#extract name of the serie
		serie = ''
		i = 1
		while i < len(tmp) and not isfloat(tmp[i]):
			serie += tmp[i]+' '
			i += 1
		serie = serie[0:-1]
		
		#create the file in the year directory
		if not os.path.isdir(mainDir+'/'+year):
			os.mkdir(mainDir+'/'+year)
		if not os.path.isfile(mainDir+'/'+year+'/'+name+ext):
			os.link(comic, mainDir+'/'+year+'/'+name+ext)
		
		#create the file in the serie directory
		if not os.path.isdir(mainDir+'/'+serie):
			os.mkdir(mainDir+'/'+serie)
		if not os.path.isfile(mainDir+'/'+serie+'/'+name+ext):
			os.link(comic, mainDir+'/'+serie+'/'+name+ext)
		
		

