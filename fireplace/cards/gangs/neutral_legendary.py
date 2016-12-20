from ..utils import *

##
# Minions

#class CFM_341:
#	"Sergeant Sally"

class CFM_344:
	"Finja, the Flying Star"
	events = Attack(SELF).after(
		Find(Attack.DEFENDER + MORTALLY_WOUNDED) & 
		Summon(CONTROLLER, RANDOM(FRIENDLY_DECK + MURLOC) * 2)
		)

#class CFM_621:
#	"Kazakus"

# class CFM_637:
# 	"Patches the Pirate"

#class CFM_670:
#	"Mayor Noggenfogger"
#	TODO: Requires implementation of GameTag.ALL_TARGETS_RANDOM: 477

class CFM_672:
	"Madam Goya"
	def play(self):
		targets = self.controller.deck.filter(type=CardType.MINION)
		if targets:
			yield Shuffle(CONTROLLER, TARGET)
			yield Summon(CONTROLLER, random.sample(targets, 1))
#class CFM_685:
#	"Don Han'Cho"

#class CFM_806:
#	"Wrathion"

#class CFM_807:
#	"Auctionmaster Beardo"

#class CFM_808:
#	"Genzo, the Shark"

#class CFM_902:
#	"Aya Blackpaw"

