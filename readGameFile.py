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
		print("Checking data for title :", self.infos['Name'])
		
		if not 'metacritic score' in self.infos:
			print("Looking for metacritic score online")
			critics, _, _ = findCritic(self.infos['Name'])
			self.infos['metacritic score'] = critics
			
		if not 'Temps de jeu' in self.infos:
			print("Looking for howlongtobeat time")
			mainTime = findMainTimes(self.infos['Name'])
			self.infos['Temps de jeu'] = mainTime
			
			
		
	def __str__(self):
		return str(self.infos)



def gFile2Dict(fileName='Games.tsv', splitSym='\t'):
	"""
		Read fileName where the first line must be categories
		each entry must be separated by splitSym
	"""
	lines = open(fileName).readlines()
	categories = lines[0].split(splitSym)

	#check if metacritic score is already present
	if not 'metacritic score' in categories:
		categories.append('metacritic score')

	#for each game, check every entry
	for game in lines[1:]:
		game = game.split(splitSym)
		gameEntry = GameEntry(game, categories)
		print(str(gameEntry))
		gameEntry.checkMissing(categories)
		print(str(gameEntry))
		return

if __name__=='__main__':
	gFile2Dict()

	

