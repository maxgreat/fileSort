DEBUG=True

def debugPrint(mess):
	if DEBUG:
		print(mess)

class GameEntry:
	def __init__(self, gameInfo, dict2Number):
		"""
			GameInfo should be a list of note and info (like name)
			dict2Number should give for each index of the list the corresponding category
		"""
		debugPrint("Creating entry with")
		debugPrint(gameInfo)
		debugPrint(len(dict2Number))
		while len(gameInfo) < len(dict2Number):
			gameInfo.append('0.0')
		self.infos = {ind:gameInfo[dict2Number[ind]] for ind in dict2Number}
	
	def __str__(self):
		return str(self.infos)



def gFile2Dict(fileName='Games.csv'):
	lines = open(fileName).readlines()
	categories = lines[0].split(',')

	#check if metacritic score is already present
	if not 'metacritic score' in categories:
		categories.append('metacritic score')
		dict2Number = {x:i for i,x in enumerate(categories)}
	dict2Number = {x:i for i,x in enumerate(categories)}

	#for each game, check every entry
	for game in lines[1:]:
		game = game.split(',')
		gameEntry = GameEntry(game, dict2Number)
		print(str(gameEntry))
		return

if __name__=='__main__':
	gFile2Dict()

	

