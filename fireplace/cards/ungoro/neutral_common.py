from ..utils import *

##
# Minions

class UNG_001:
	"Pterrordax Hatchling"
	play = ADAPT(SELF)

class UNG_009:
	"Ravasaur Runt"
	powered_up = Count(FRIENDLY_MINIONS - SELF) >= 2
	play = powered_up & ADAPT(SELF)

class UNG_010:
	"Sated Threshadon"
	play = Summon(CONTROLLER, "UNG_201t") * 3

class UNG_073:
	"Rockpool Hunter"
	powered_up = Find(FRIENDLY_MINIONS + MURLOC)
	play = Buff(TARGET, "UNG_073e")
	
UNG_073e = buff(+1, +1)

class UNG_076:
	"Eggnapper"
	deathrattle = Summon(CONTROLLER, "UNG_076t1") * 2

class UNG_082:
	"Thunder Lizard"
	powered_up = ELEMENTAL_PLAYED_LAST_TURN
	play = powered_up & ADAPT(SELF)

class UNG_084:
	"Fire Plume Phoenix"
	play = Hit(TARGET, 2)

class UNG_205:
	"Glacial Shard"
	play = Freeze(TARGET)

class UNG_801:
	"Nesting Roc"
	powered_up = Count(FRIENDLY_MINIONS - SELF) >= 2
	play = powered_up & Taunt(SELF)

class UNG_803:
	"Emerald Reaver"
	play = Hit(ALL_HEROES, 1)

class UNG_809:
	"Fire Fly"
	play = Give(CONTROLLER, "UNG_809t1")

class UNG_818:
	"Volatile Elemental"
	deathrattle = Hit(RANDOM_ENEMY_MINION, 3)

class UNG_845:
	"Igneous Elemental"
	play = Give(CONTROLLER, "UNG_809t1") * 2

class UNG_928:
	"Tar Creeper"
	update = Find(SELF + CONTROLLED_BY(CURRENT_PLAYER)) | Refresh(SELF, {GameTag.ATK: +2})

class UNG_937:
	"Primalfin Lookout"
	powered_up = Find(FRIENDLY_MINIONS + MURLOC - SELF)
	play = powered_up & DISCOVER(RandomMinion(race=Race.MURLOC))
