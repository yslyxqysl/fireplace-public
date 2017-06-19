from ..utils import *

##
# Minions

#class UNG_002:
#	"Volcanosaur"

class UNG_070:
	"Tol'vir Stoneshaper"
	powered_up = ELEMENTAL_PLAYED_LAST_TURN
	play = powered_up & (Buff(SELF, "UNG_070e"), GiveDivineShield(SELF))

UNG_070e = buff(taunt=True)

class UNG_072:
	"Stonehill Defender"
	play = DISCOVER(RandomMinion(taunt=True))

class UNG_075:
	"Vicious Fledgling"
	events = Attack(SELF, ENEMY_HERO).after(ADAPT(SELF))

class UNG_079:
	"Frozen Crusher"
	events = Attack(SELF).after(Freeze(SELF))

class UNG_083:
	"Devilsaur Egg"
	deathrattle = Summon(CONTROLLER, "UNG_083t1")

class UNG_807:
	"Golakka Crawler"
	play = Destroy(TARGET), Buff(SELF, "UNG_807e")
	
UNG_807e = buff(+1, +1)

class UNG_816:
	"Servant of Kalimos"
	powered_up = ELEMENTAL_PLAYED_LAST_TURN
	play = powered_up & DISCOVER(RandomMinion(race=Race.ELEMENTAL))
