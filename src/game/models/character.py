from typing import Tuple, List
from src.game.models.base import Base, Attributes, Feat, Status, Action, Attack, Item, Lore
from src.game.models.spell import Spell

# PC Stats 
class PlayerCharacter:
    # Static Stats
    _class: str
    level: int
    attributes: Attributes
    max_hp: int
    ac: int
    capacity: int
    feats: List[Feat]
    spells: List[str] | None
    # Dynamic Stats
    hp: int
    knowledge: List[str] | None
    memories: List[str] | None
    conditions: List[Status] | None
    gold: int
    inventory: List[Item]
    equipped: List[Item]
    spell_slots: List[int] | None
    experience: Tuple [int,int]

# Generic base for anything else with stats
class Entity(Base):
    attributes: Attributes
    max_hp: int
    max_morale: int
    ac: int
    actions: List[Action | str] | None
    attacks: List[Attack | str] | None
    feats: List[Feat | str] | None
    lore: List[Lore | str] | None
    # Dynamic Stats
    hp: int
    morale: int
    conditions: List[Status | str] | None
    inventory: List[Item | str] | None
    equipped: List[Item | str] | None


# D&D-style stat block for enemies
class MonsterStatBlock(Entity):
    xp: int

# Conversation History classes for PC and NPC conversations
class Message:
    text: str
    speaker_id: str
    listener_id: str
class Conversation:
    id: str
    messages: List[Message]
class ConversationSummary(Base):
    pass
# Characterization for NPCs
class Character(Entity):
    disposition: str
    prior_conversations: List[Conversation | ConversationSummary] | None
    