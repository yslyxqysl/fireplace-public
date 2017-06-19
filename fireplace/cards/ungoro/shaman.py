from ..utils import *

##
# Minions

class UNG_025:
	"Volcano"
	def play(self):
		count = self.controller.get_spell_damage(15)
		yield Hit(RANDOM_MINION, 1) * count

class UNG_201:
	"Primalfin Totem"
	events = OWN_TURN_END.on(Summon(CONTROLLER, "UNG_201t"))

class UNG_202:
	"Fire Plume Harbinger"
	play = Buff(FRIENDLY_HAND + ELEMENTAL, "UNG_202e")

@custom_card
class UNG_202e:
	tags = {
		GameTag.CARDNAME: "Fire Plume Harbinger Buff",
		GameTag.CARDTYPE: CardType.ENCHANTMENT,
		GameTag.COST: -1
	}
	events = REMOVED_IN_PLAY

class UNG_208:
	"Stone Sentinel"
	powered_up = ELEMENTAL_PLAYED_LAST_TURN
	play = powered_up & Summon(CONTROLLER, "UNG_208t") * 2

#class UNG_211:
#	"Kalimos, Primal Lord"
#	powered_up = ELEMENTAL_PLAYED_LAST_TURN
#	play =

class UNG_211a:
	"Invocation of Earth"
	play = Summon(CONTROLLER, "UNG_211aa") * 7

class UNG_211b:
	"Invocation of Water"
	play = Heal(FRIENDLY_HERO, 12)

class UNG_211c:
	"Invocation of Fire"
	play = Hit(ENEMY_HERO, 6)

class UNG_211d:
	"Invocation of Air"
	play = Hit(ENEMY_MINIONS, 3)

class UNG_938:
	"Hot Spring Guardian"
	play = Heal(TARGET, 3)

##
# Spells

class UNG_817:
	"Tidal Surge"
	play = Hit(TARGET, 4), Heal(FRIENDLY_HERO, 4)

#class UNG_942:
#	"Unite the Murlocs"

class UNG_956:
	"Spirit Echo"
	play = Buff(FRIENDLY_MINIONS, "UNG_956e")

class UNG_956e:
	deathrattle = Bounce(OWNER)
	tags = {GameTag.DEATHRATTLE: True}
