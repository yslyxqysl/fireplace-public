from ..utils import *

##
# Minions

class UNG_011:
	"Hydrologist"
	play = DISCOVER(RandomSpell(secret=1))

class UNG_015:
	"Sunkeeper Tarim"
	play = Buff(ALL_MINIONS - SELF, "UNG_015e")

class UNG_015e:
	atk = SET(3)
	max_health = SET(3)

#class UNG_953:
#	"Primalfin Champion"

class UNG_962:
	"Lightfused Stegodon"
	powered_up = Find(ID("CS2_101t"))
	play = ADAPT(FRIENDLY_MINIONS + ID("CS2_101t"))

##
# Spells

class UNG_004:
	"Dinosize"
	play = Buff(TARGET, "UNG_004e")

class UNG_004e:
	atk = SET(10)
	max_health = SET(10)

class UNG_952:
	"Spikeridged Steed"
	play = Buff(TARGET, "UNG_952e")

class UNG_952e:
	deathrattle = Summon(CONTROLLER, "UNG_810")
	tags = {
		GameTag.ATK: +2,
		GameTag.HEALTH: +6,
		GameTag.DEATHRATTLE: True
	}

#class UNG_954:
#	"The Last Kaleidosaur"
	
class UNG_960:
	"Lost in the Jungle"
	play = Summon(CONTROLLER, "CS2_101t") * 2

class UNG_961:
	"Adaptation"
	play = ADAPT(TARGET)

##
# Weapons

class UNG_950:
	events = Attack(FRIENDLY_HERO).after(Summon(CONTROLLER, "CS2_101t") * 2)
