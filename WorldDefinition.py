class World: 
""" 
Attributes: 
	game_status (str): Whether the game 
	is in progress or has ended. Either "playing", 
	"won", or "lost". 

	player (Player): The player character's info. 

	killer_caught (bool): whether or not the killer
	has been apprehended. Determines the end of the game
""" 
class Player: 
""" 
Attributes: 
	location (str): The current 
	location of the player within the world. 

	has_knife (bool): Whether they have 
	collected the knife at the crime scene. 
	evidence (list): A list of evidence that the 
	player collected.

	knows_killer (bool): whether or not the player
	knows the true killer. Determines the outcome 
	of the game.
"""
class Suspect:
	'''
	Attributes:
		knowledge (str): the specific
		information each suspect has.

		room_number (int): the number
		of that suspect's interrogation room.

		is_killer (bool): whether or not they are
		really the killer.
	'''