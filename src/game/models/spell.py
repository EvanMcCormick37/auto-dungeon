from typing import List
from enum import Enum
from src.game.models.base import Action, Diceroll, AttackStats, Item, Lore
from src.game.models.character import Character

class School(str, Enum):
    ABJURATION = 'Abjuration'
    CONJURATION = 'Conjuration'
    DIVINATION = 'Divination'
    ENCHANTMENT = 'Enchantment'
    EVOCATION = 'Evocation'
    ILLUSION = 'Illusion'
    NECROMANCY = 'Necromancy'
    TRANSMUTATION = 'Transmutation'

class SpellStats:
    level: int
    school: School
    spell_slots_used: List[int] | None
    components: List[Item] | None
    duration: int
    damage: Diceroll
class Spell(Action):
    attack_stats: AttackStats


# Rare, magical Items.
class MacGuffin(Item):
    spells: List[Spell] | None
    lore: List[Lore] | None
    relationships: List[Character] | None