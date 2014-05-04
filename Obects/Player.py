class Player:
	#This is the player controlled character
	playerx = 5
	playery = 5
	image = "@"

	def act(input):
		if input == "w":
			playery -= 1
			loop = False
		elif input =="a":
			playerx -= 1
			loop = False
		elif input =="s":
			playery += 1
			loop = False
		elif input =="d":
			playerx += 1
			loop = False