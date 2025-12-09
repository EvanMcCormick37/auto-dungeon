from typing import Optional, List, Tuple
from base import Attribute, Attributes, Action, Attack, Diceroll
class Item:
    id: str
    name: str
    description: str
    hp: Tuple[str,str]
    _cost: int
    weight: int
    uses: Optional[List[Action]]
    bonuses: Optional[Attributes]

class Weapon(Item):
    attacks: Optional[List[Attack]]
    base_attribute: Optional[Attribute]
    damage_roll: Optional[Diceroll]
class Spell:
