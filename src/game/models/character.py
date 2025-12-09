from base import Attributes, Feat, Status
from item import Item, Weapon
from spell import Spell
from typing import Tuple, Optional

# Derived modifiers, proficiency bonus
class CharStats:
    name: str
    _class: str
    level: int
    experience: int
    attributes: Attributes
    hp: Tuple[int,int]
    ac: int
    attributes: Attributes
    inventory: list[Item]
    weapons: list[Weapon]
    feats: list[Feat]
    spells: Optional[Spell]
    gold: int
    conditions: list[Status]  # poisoned, prone, etc.