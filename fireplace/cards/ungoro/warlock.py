from ..utils import *

##
# Minions

#class UNG_047:
#	"Ravenous Pterrordax"

class UNG_049:
	"Tar Lurker"
	update = Find(SELF + CONTROLLED_BY(CURRENT_PLAYER)) | Refresh(SELF, {GameTag.ATK: +3})

class UNG_833:
	"Lakkari Felhound"
	play = Discard(RANDOM(FRIENDLY_HAND) * 2)

##
# Spells

class UNG_831:
	"Corrupting Mist"
	play = Buff(ALL_MINIONS, "UNG_831e")

class UNG_831e:
	events = OWN_TURN_BEGIN.on(Destroy(OWNER))

class UNG_832:
	"Bloodbloom"
	play = Buff(CONTROLLER, "UNG_832e")

class UNG_832e:
	"Dark Power"
	events = [
		OWN_SPELL_PLAY.on(Destroy(SELF)),
		OWN_TURN_END.on(Destroy(SELF))
	]
	update = Refresh(CONTROLLER, {GameTag.SPELLS_COST_HEALTH: True})

class UNG_834:
	"Feeding Time"
	play = Hit(TARGET, 3), Summon(CONTROLLER, "UNG_834t1") * 3
