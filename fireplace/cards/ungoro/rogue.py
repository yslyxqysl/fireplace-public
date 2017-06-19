from ..utils import *

##
# Minions

class UNG_058:
	"Razorpetal Lasher"
	play = Give(CONTROLLER, "UNG_057t1")

class UNG_063:
	"Biteweed"
	combo = Buff(SELF, "UNG_063e") * Attr(CONTROLLER, GameTag.NUM_CARDS_PLAYED_THIS_TURN)

UNG_063e = buff(+1, +1)

class UNG_064:
	"Vilespine Slayer"
	combo = Destroy(TARGET)
	
#class UNG_065:
#	"Sherazin, Corpse Flower"

##
# Spells

class UNG_057:
	"Razorpetal Volley"
	play = Give(CONTROLLER, "UNG_057t1") * 2

class UNG_057t1:
	"Razorpetal"
	play = Hit(TARGET, 1)

class UNG_060:
	"Mimic Pod"
	play = Draw(CONTROLLER).then(Give(CONTROLLER, Copy(Draw.CARD)))
	
#class UNG_067:
#	"The Caverns Below"

class UNG_856:
	"Hallucination"
	play = DISCOVER(RandomCollectible(card_class=ENEMY_CLASS))

##
# Weapon

#class UNG_061:
#	"Obsidian Shard"
