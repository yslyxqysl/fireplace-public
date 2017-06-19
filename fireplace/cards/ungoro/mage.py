from ..utils import *

##
# Minions

class UNG_020:
	"Arcanologist"
	play = ForceDraw(RANDOM(FRIENDLY_DECK + SECRET))

class UNG_021:
	"Steam Surger"
	powered_up = ELEMENTAL_PLAYED_LAST_TURN
	play = powered_up & Give(CONTROLLER, "UNG_018")

class UNG_027:
	"Pyros"
	deathrattle = Bounce(SELF), Morph(SELF, "UNG_027t2")

class UNG_027t2:
	"Pyros"
	deathrattle = Bounce(SELF), Morph(SELF, "UNG_027t4")

class UNG_846:
	"Shimmering Tempest"
	deathrattle = Give(CONTROLLER, RandomSpell(card_class=CardClass.MAGE))

##
# Spells

class UNG_018:
	"Flame Geyser"
	play = Hit(TARGET, 2), Give(CONTROLLER, "UNG_809t1")

class UNG_941:
	"Primordial Glyph"
	play = DISCOVER(RandomSpell()).then(Buff(Discover.CARDS, "UNG_941e"))

class UNG_941e:
	"Primal Magic"
	tags = {GameTag.COST: -2}

class UNG_948:
	"Molten Reflection"
	play = Summon(CONTROLLER, ExactCopy(TARGET))

class UNG_955:
	"Meteor"
	play = Hit(TARGET, 15), Hit(TARGET_ADJACENT, 3)

##
# Secrets

class UNG_024:
	"Mana Bind"
	secret = Play(OPPONENT, SPELL).on(
		Reveal(SELF), Give(CONTROLLER, Copy(Play.CARD)).then(Buff(Give.CARD, "UNG_024e"))
	)

@custom_card
class UNG_024e:
	tags = {
		GameTag.CARDNAME: "Mana Bind Buff",
		GameTag.CARDTYPE: CardType.ENCHANTMENT
	}
	update = Refresh(OWNER, {GameTag.COST: SET(0)})
