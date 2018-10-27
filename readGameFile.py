DEBUG=True

from metacritic.metacritic import findCritic
from howlongtobeat.howlongtobeat import findMainTimes

def debugPrint(mess):
	if DEBUG:
		print(mess)

class GameEntry:
	def __init__(self, gameInfo, categories):
		"""
			GameInfo should be a list of note and info (like name)
			dict2Number should give, for each index of the list, the corresponding category
		"""
		
		self.infos={}
		
		for i, cat in enumerate(categories):
			if i < len(gameInfo):
				self.infos[cat] = gameInfo[i]
				
					
	def checkMissing(self, categories):
		"""
			Check for missing Entries
			Look online to fill it up
		"""
		print("Checking data for title :", self.infos['Name'])
		
		if not 'metacritic score' in self.infos:
			critics, _, _ = findCritic(self.infos['Name'])
			self.infos['metacritic score'] = int(critics)
			
		if not 'Temps de jeu' in self.infos:
			mainTime = findMainTimes(self.infos['Name'])
			self.infos['Temps de jeu'] = mainTime
			
			
		
	def __str__(self):
		return str(self.infos)
		
	def toTsv(self):
		s = ""
		for inf in self.infos:
			s += str(self.infos[inf]) + "\t"
		return s


class GameList:
	"""
		Handle a list of game entries
	"""
	def __init__(self, fileName='Games.tsv', splitSym='\t'):
		"""
			Read fileName where the first line must be categories
			each entry must be separated by splitSym
		"""
		lines = open(fileName).readlines()
		self.categories = lines[0].split(splitSym)

		#check if metacritic score is already present
		
		self.entries = []
		#for each game, check every entry
		for game in lines[1:3]:
			game = game.split(splitSym)
			self.entries.append(GameEntry(game, self.categories))
		
	def addCategory(self, catName):
		if not catName in self.categories:
			self.categories.append('metacritic score')
		[x.checkMissing(self.categories) for x in self.entries]
		
	def toTsv(self):
		s = ""
		for c in self.categories:
			s += c + "\t"
		s += "\n"
		for e in self.entries:
			s += e.toTsv() + "\n"
		return s
	

if __name__=='__main__':
	gL = GameList()
	gL.addCategory('metacritic score')
	print(gL.toTsv())

	

