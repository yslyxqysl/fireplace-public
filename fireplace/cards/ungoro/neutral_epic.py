from ..utils import *

##
# Minions

class UNG_085:
	"Emerald Hive Queen"
	update = Refresh(FRIENDLY_HAND + MINION, {GameTag.COST: +2})

class UNG_087:
	"Bittertide Hydra"
	events = SELF_DAMAGE.on(Hit(FRIENDLY_HERO, 3))
	
#class UNG_088:
#	"Tortollan Primalist"

class UNG_089:
	"Gentle Megasaur"
	play = ADAPT(FRIENDLY_MINIONS + MURLOC)

class UNG_099:
	"Charged Devilsaur"
	play = Buff(SELF, "UNG_099e")

@custom_card
class UNG_099e:
	tags = {
		GameTag.CARDNAME: "Charged Devilsaur Buff",
		GameTag.CARDTYPE: CardType.ENCHANTMENT,
		GameTag.CANNOT_ATTACK_HEROES: True
	}
	events = OWN_TURN_END.on(Destroy(SELF))

class UNG_113:
	"Bright-Eyed Scout"
	play = Draw(CONTROLLER).then(Buff(Draw.CARD, "UNG_113e"))

class UNG_113e:
	"Scouted"
	update = Refresh(OWNER, {GameTag.COST: SET(5)})

class UNG_847:
	"Blazecaller"
	powered_up = ELEMENTAL_PLAYED_LAST_TURN
	play = powered_up & Hit(TARGET, 5)

class UNG_848:
	"Primordial Drake"
	play = Hit(ALL_MINIONS - SELF, 2)

class UNG_946:
	"Gluttonous Ooze"
	play = GainArmor(FRIENDLY_HERO, ATK(ENEMY_WEAPON)), Destroy(ENEMY_WEAPON)
