from typing import Optional, List
from enum import Enum
from base import Action, Diceroll, AttackStats
from item import Item

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
    school: Optional[School]
    components: Optional[List[Item]]
    duration: Optional[int]
    damage: Optional[Diceroll]
class Spell(Action):
    
    attack_stats: Optional[AttackStats]