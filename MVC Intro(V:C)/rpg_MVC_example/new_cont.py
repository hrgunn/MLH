import random
from view import View

class Game:
	def __init__(self):
		self.adventure.index = 0
		self.adventure = []
		self.player = None
		self.view= View()

		def begin(self):
			self.player = self.view.input_player_name()

		def create_player(self):
			name = self.view.input_player_name()
			job = self.view.input_player_job()
			return Player(name, job)

		def play(self):
			self.view.introduction_message()
			while self.adventure_index<len(self.adventure):
				if self.adventure[self.adventure_index].start(self.player):
					self.mission_index += 1
					self.view.passed_adventure_message()
				else:
					self.view.failed_mission_message()
					break

				def load_adventure(self, adventure):
					self.adventure = passed_adventure_messageself.adventure_index = 0



class Player:
	def __init__ (self, name, job):
		self.name = name
		self.job = job
		self.hp = hp
		self.attack = attack


class Smuggler(Player):
	hp = 120
	attack = 25
	def __init__(self, name, job):
		Player.__init__(self,name,job)

class Thief(Player):
	hp = 100
	attack = 35
	def __init__(self, name, job):  
		Player.__init__(self,name,job)

class Merchant(Player):
	hp = 110
	attack = 30
	def __init__(self, name, job):
		Player.__init__(self,name,job)

class Bounty_Hunter(Player):
	hp = 120
	attack = 40
	def __init__(self, name, job):
		Player.__init__(self,name,job)





class Mission:
	def __init__ (self, descriptions, actions, level):
		self.description = description
		self.actions = actions
		self.level = level
		self.view = View()

	def start(self, player):
	self.player = player
	self.mission_description(self.description)

	decision = self.view.input_mission_decision(self.actions)   

	passed_mission = self.determine_outcome(decision)
	if passed_mission:
		battle = Battle(self.player, self.level)
		while battle.take_turn():
			pass
		if battle.lost == False:
			return True
	return False

# Bad Guys!

class Bad_Guy:
	def __init__ (self, name, job, hp, attack):
		self.name = name
		self.job = job
		self.hp = hp
		self.attack = attack
	def take_damage(self, take_damage):
		self.hp -= damage

	def is_dead(self):
		return self.hp < 0



	class Thug(Bad_Guy):
		hp = 30
		attack = 15
		def __init__(self, name, job):
			Bad_Guy.__init__(self,name,job)


	# This could eventually become a Boss Player, possible special attributes/weapons
	class Badass_Thug(Bad_Guy):
		hp = 120
		attack = 40
		def __init__(self, name, job):
			Bad_Guy.__init__(self,name,job)


	# These could be added in to create some (chase/run away scenereos. The snitch would "get spotted" and bail, and the user decides to chase and potentially stop the snitch from giving away their position, or run and try to get away...???...)
	class Government_Snitch(Bad_Guy):
		hp = 20
		attack = 20
		def __init__(self, name, job):
			Bad_Guy.__init__(self,name,job)

	class Totem_Soldier(Bad_Guy):
		hp = 60
		attack = 40
		def __init__(self, name, job):
			Bad_Guy.__init__(self,name,job)



	# This would only take into effect in Act 2 (Act 1 ending when you and the Price sucessfully take off). They could chase you on your way to safety once you break atmosphere
	class Enemy_Pilot(Bad_Guy):
		hp = 120
		attack = 40
		def __init__(self, name, job):
			Bad_Guy.__init__(self,name,job)


	# Leader of the Totems, my dad wanted to be in the game.
	class Phil_Da(Bad_Guy):
		hp = 150
		attack = 70
		def __init__(self, name, job):
			Bad_Guy.__init__(self,name,job)


	# Put in charge of the man-hunt, my mom wanted to be involved too.
	class LaLuK(Bad_Guy):
		hp = 120
		attack = 40
		def __init__(self, name, job):
			Bad_Guy.__init__(self,name,job)



	class Battle:
		def __init__(self, player, level):
			self.player = player
			self.level = level
			self.monster = 







