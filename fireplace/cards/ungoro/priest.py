from ..utils import *

##
# Minions

class UNG_029:
	"Shadow Visions"
	def play(self):
		decklist = [i.id for i in self.controller.deck if i.type == CardType.SPELL]
		yield DISCOVER(RandomID(*decklist))

class UNG_032:
	"Crystalline Oracle"
	deathrattle = Give(CONTROLLER, Copy(RANDOM(ENEMY_DECK)))

class UNG_034:
	"Radiant Elemental"
	update = Refresh(FRIENDLY_HAND + SPELL, {GameTag.COST: -1})

class UNG_037:
	"Tortollan Shellraiser"
	deathrattle = Buff(RANDOM_FRIENDLY_MINION, "UNG_037e")

UNG_037e = buff(+1, +1)

class UNG_963:
	"Lyra the Sunshard"
	event = OWN_SPELL_PLAY.on(Give(CONTROLLER, RandomSpell(card_class=CardClass.PRIEST)))

##
# Spells

class UNG_030:
	"Binding Heal"
	play = Heal(TARGET | FRIENDLY_HERO, 5)
