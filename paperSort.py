import comicSort

"""
	The files must be in the form: 
		paper title - [journal or conference] year [- author1 author2].pdf 
		
		(terms in [] are optional)
		DO NOT use space in the name of an author
"""

if __name__ == '__main__':
	if len(sys.argv) > 1:
		mainDir = os.path.abspath(sys.argv[1])
	else:
		mainDir = os.path.abspath(os.path.curdir)
	
	l = comicSort.dirExplore(mainDir, extension='.pdf')
	for paper in l:
		name, ext = os.path.splitext(paper.split('/')[-1])
		tmp = name.split('-')
		title = tmp[0]
		year = tmp[1].split(' ')[-1]
		#verify year
		if not year.isdigit():
			continue
		
		#lloking for author
		author = ''
		if len(tmp) == 3:
			author = tmp[-1]
		
		#create the file in the year directory
		if not os.path.isdir(mainDir+'/'+year):
			os.mkdir(mainDir+'/'+year)
		if not os.path.isfile(mainDir+'/'+year+'/'+name+ext):
			os.link(comic, mainDir+'/'+year+'/'+name+ext)
		
		#create the file in the author directory
		if len(author) > 1:
			if not os.path.isdir(mainDir+'/authors'):
				os.mkdir(mainDir+'/authors')
			for a in author.split(' '):
				if not os.path.isdir(mainDir+'/authors'+'/'+a):
					os.mkdir(mainDir+'/authors'+'/'+a)
				if not os.path.isfile(mainDir+'/authors'+'/'+a+'/'+name+ext):
					os.link(paper, mainDir+'/authors'+'/'+a+'/'+name+ext)
