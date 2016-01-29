import os
import sys
import comicSort

def extractNumber(name, split=' '):
	for i in name.split(split):
		if i.isdigit():
			return int(i)
		if i.split('.')[0].isdigit():
			return int(i.split('.')[0].isdigit())
	return -1

class date:
	def __init__(self, year, month):
		self.y = year
		self.m = month-1
	
	def __str__(self):
		s = str(self.y)+'-'+str(self.m+1).zfill(2)
		return s
	
	def add(self, i):
		self.m += i%12
		self.y += i/12

if __name__=="__main__":
	directory = '/media/portaz/17E771D5010CDC52/Perso/Comics/Captain America v3 1998-2002'
	exportName = 'Captain America v3'
	beginDate = date(1998,01)
	nbStart = 1
	nbEnd = 33
	comicList = comicSort.dirExplore(directory, extension='.cbr')
	comicList += comicSort.dirExplore(directory, extension='.cbz')
	for comic in comicList:
		name, ext = os.path.splitext(comic.split('/')[-1])
		number = extractNumber(name, '_')
		if number == -1:
			print("Cannot find the number of the comic:", comic)
			continue
		else:
			if number >= nbStart and number <= nbEnd:
				d = date(1998,01)
				d.add(number-1)
				os.rename(comic, directory+'/'+str(d)+' '+exportName+' '+str(number).zfill(3)+ext)
