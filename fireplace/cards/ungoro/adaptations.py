from ..utils import *

class UNG_999t2:
	play = Buff(TARGET, "UNG_999t2e")

class UNG_999t2e:
	deathrattle = Summon(CONTROLLER, "UNG_999t2t1") * 2
	tags = {
		GameTag.DEATHRATTLE: True
	}

class UNG_999t3:
	play = Buff(TARGET, "UNG_999t3e")

UNG_999t3e = buff(atk=3)

class UNG_999t4:
	play = Buff(TARGET, "UNG_999t4e")

UNG_999t4e = buff(health=3)

class UNG_999t5:
	play = Buff(TARGET, "UNG_999t5e")

UNG_999t5e = buff(cant_be_targeted_by_spells=True)

class UNG_999t6:
	play = Buff(TARGET, "UNG_999t6e")

UNG_999t6e = buff(taunt=True)

class UNG_999t7:
	play = Buff(TARGET, "UNG_999t7e")

UNG_999t7e = buff(windfury=True)

class UNG_999t8:
	play = Buff(TARGET, "UNG_999t8e")

class UNG_999t8e:
	play = GiveDivineShield(TARGET)

class UNG_999t10:
	play = Buff(TARGET, "UNG_999t10e")

class UNG_999t10e:
	tags = {GameTag.STEALTH: True}
	events = OWN_TURN_BEGIN.on(Unstealth(OWNER), Destroy(SELF))

class UNG_999t13:
	play = Buff(TARGET, "UNG_999t13e")

UNG_999t13e = buff(poisonous=True)

class UNG_999t14:
	play = Buff(TARGET, "UNG_999t14e")
	
UNG_999t14e = buff(+1, +1)
