from ..utils import *


##
# Minions

class UNG_838:
	"Tar Lord"
	update = Find(SELF + CONTROLLED_BY(CURRENT_PLAYER)) | Refresh(SELF, {GameTag.ATK: +4})

class UNG_925:
	"Ornery Direhorn"
	play = ADAPT(SELF)

class UNG_926:
	"Cornered Sentry"
	play = Summon(OPPONENT, "UNG_076t1") * 3

class UNG_933:
	"King Mosh"
	play = Destroy(ALL_MINIONS + DAMAGED)

class UNG_957:
	"Direhorn Hatchling"
	deathrattle = Shuffle(CONTROLLER, "UNG_957t1")

##
# Spells

class UNG_922:
	"Explore Un'Goro"
	play = Morph(FRIENDLY_DECK, "UNG_922t1")

class UNG_922t1:
	"Choose Your Path"
	play = DISCOVER(RandomCollectible())

class UNG_923:
	"Iron Hide"
	play = GainArmor(FRIENDLY_HERO, 5)
	
#class UNG_927:
#	"Sudden Genesis"
	
#class UNG_934:
#	"Fire Plume's Heart"

##
# Weapons

#class UNG_929:
#	"Molten Blade"
