from ..utils import *

##
# Minions

#class UNG_078:
#	"Tortollan Forager"


class UNG_086:
	"Giant Anaconda"
	deathrattle = Summon(CONTROLLER, RANDOM(FRIENDLY_HAND + (ATK >= 5)))


class UNG_100:
	"Verdant Longneck"
	play = ADAPT(SELF)


class UNG_101:
	"Shellshifter"
	choose = ("UNG_101a", "UNG_101b")

class UNG_101a:
	play = Morph(SELF, "UNG_101t")

class UNG_101b:
	play = Morph(SELF, "UNG_101t2")


class UNG_109:
	"Elder Longneck"
	powered_up = Find(FRIENDLY_HAND + (ATK >= 5) - SELF)
	play = powered_up & ADAPT(SELF)

##
#Spells

class UNG_103:
	"Evolving Spores"
	play = ADAPT(FRIENDLY_MINIONS)


class UNG_108:
	"Earthen Scales"
	play = Buff(TARGET, "UNG_108e"), GainArmor(FRIENDLY_HERO, ATK(TARGET))

UNG_108e = buff(+1, +1)


class UNG_111:
	"Living Mana"
	def play(self):
		mana_destroy = min(self.controller.max_mana, self.controller.minion_slots)
		yield Summon(CONTROLLER, ["UNG_111t1"]) * mana_destroy
		yield from GainEmptyMana(CONTROLLER, -mana_destroy)

class UNG_111t1:
	deathrattle = GainEmptyMana(CONTROLLER, 1)
	
	
#class UNG_116:
#	"Jungle Giants"
