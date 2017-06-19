from ..utils import *

##
# Minions

class UNG_800:
	"Terrorscale Stalker"
	play = Deathrattle(TARGET)

class UNG_912:
	"Jeweled Macaw"
	play = Give(CONTROLLER, RandomMinion(race=Race.BEAST))

class UNG_913:
	"Tol'vir Warden"
	play = ForceDraw( RANDOM(FRIENDLY_DECK + MINION + (COST == 1)) ) * 2

class UNG_914:
	"Raptor Hatchling"
	deathrattle = Shuffle(CONTROLLER, "UNG_914t1")

class UNG_915:
	"Crackling Razormaw"
	powered_up = Find(FRIENDLY_MINIONS + BEAST)
	play = ADAPT(TARGET)

#class UNG_919:
#	"Swamp King Dred"

##
# Spells

class UNG_916:
	"Stampede"
	play = Buff(CONTROLLER, "UNG_916e")

class UNG_916e:
	"Stampeding"
	events = [
		Play(CONTROLLER, BEAST).on( Give(CONTROLLER, RandomCollectible(race=Race.BEAST)) ),
		OWN_TURN_END.on(Destroy(SELF))
	]

class UNG_910:
	"Grievous Bite"
	play = Hit(TARGET, 2), Hit(TARGET_ADJACENT, 1)

class UNG_917:
	"Dinomancy"
	play = Switch(FRIENDLY_HERO_POWER, { None: Summon(CONTROLLER, "UNG_917t1") })

class UNG_917t1:
	"Dinomancy"
	activate = Buff(TARGET, "UNG_917e")

UNG_917e = buff(+2, +2)

#class UNG_920:
#	"The Marsh Queen"

class UNG_920t1:
	"Queen Carnassa"
	play = Shuffle(CONTROLLER, "UNG_920t2") * 15
	
class UNG_920t2:
	"Carnassa's Brood"
	play = Draw(CONTROLLER)

##
# Weapons

