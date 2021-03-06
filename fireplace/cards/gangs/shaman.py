from ..utils import *

##
# Minions

class CFM_061:
	"Jinyu Waterspeaker"
	play = Heal(TARGET, 6)

class CFM_312:
	"Jade Chieftain"
	play = SummonJadeGolem(CONTROLLER).then(Taunt(SummonJadeGolem.CARD))

class CFM_324:
	"White Eyes"
	deathrattle = Shuffle(CONTROLLER, "CFM_324t")

class CFM_697:
	"Lotus Illusionist"
	events = Attack(SELF, ENEMY_HERO).after(Morph(SELF, RandomMinion(cost=6)))

##
# Spells

class CFM_310:
	"Call in the Finishers"
	play = Summon(CONTROLLER, "CFM_310t") * 4

class CFM_313:
	"Finders Keepers"
	#Force Shaman class cards or else will not work for other classes
	play = DISCOVER(RandomCollectible(card_class=CardClass.SHAMAN, overload=True))

class CFM_696:
	"Devolve"
	def play(self):
		for target in self.controller.opponent.field:
			if 1 <= target.cost <= 10:
				yield Morph(target, RandomMinion(cost=target.cost - 1))

class CFM_707:
	"Jade Lightning"
	play = Hit(TARGET, 4), SummonJadeGolem(CONTROLLER)

##
# Weapons

class CFM_717:
	"Jade Claws"
	play = SummonJadeGolem(CONTROLLER)

