from enum import Enum
from typing import Optional, Tuple, List
from base import Attribute, Attributes, Feat, Action, Attack

# Generic base for anything with stats
class Entity(Base):
    hp: Tuple[int,int]
    ac: int
    attributes: Attributes
    actions: Optional[List[Action]]
    attacks: Optional[List[Attack]]
    feats: Optional[List[Feat]]

# D&D-style stat block for enemies
class MonsterStatBlock(Entity):
    xp: int

class NPC(Entity):
    disposition: str
    motives: Motive[]
    knowledge: Lore[]
    character_traits: Trait[]