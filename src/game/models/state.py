from src.game.models.schemas import Base, Attribute, Attributes, Status
from typing import List, Tuple
from dataclasses import dataclass

# Simple Item and Weapon classes
@dataclass
class AttackStats:
    range: int
    base_attribute: Attribute
    damage: str

@dataclass
class Item(Base):
    hp: Tuple[int,int]
    cost: int
    weight: int
    effects: List[Status]
    attack_stats: AttackStats | None

# # Conversation History classes for PC and NPC conversations
# class Message:
#     text: str
#     speaker_id: str
#     listener_id: str
# class Conversation:
#     id: str
#     messages: List[Message]
# class ConversationSummary(Base):
#     pass

# PC Stats 
@dataclass
class PlayerCharacter(Base):
    # Persistent Stats
    _class: str
    level: int
    attributes: Attributes
    max_hp: int
    ac: int
    capacity: int
    feats: List[Status]
    # spells: List[Lore] | None
    # Semi-Dynamic Stats (Status + Roleplay)
    # knowledge: List[Lore] | None
    # memories: List[Lore] | None
    # prior_conversations: List[Conversation | ConversationSummary] | None
    # Inventory and Experience
    xp: Tuple [int,int]
    gold: int
    inventory: List[Item]
    # Dynamic Stats (Combat)
    equipped: List[Item]
    spell_slots: List[int] | None = None
    # to_notice: Requirement | None
    conditions: List[Status]
    hp: int
# NPCs and Monsters
@dataclass
class Entity(Base):
    xp: int | None
    attributes: Attributes
    max_hp: int
    ac: int
    hp: int
    disposition: str
    conditions: List[Status]
    inventory: List[Item]
    equipped: List[Item]
    # to_notice: Requirement | None
# class Character(Grunt):
#     disposition: str
#     prior_conversations: List[Conversation | ConversationSummary] | None
#     feats: List[Feat] | None
#     # lore: List[Lore] | None

# Locations
@dataclass
class Location(Base):
    # possibilities: List[Lore] | None
    is_explored: bool
# class Door(Location):
#     next_room_id: str                       # ID of connecting room.
#     is_open: bool
#     locked: Requirement | None
#     to_notice: Requirement | None
@dataclass
class Room(Location):
    # doors: List[Door] | None
    occupants: List[Entity]
    items: List[Item]
@dataclass
class Level(Base):
    room_ids: List[str]
    # hooks: List[Lore] | None
    effects: List[Status]

# class Trap(Base):
#     to_notice: Requirement | None      # Anything to_notice must have Requirement met to be seen
#     to_trigger: Requirement | None     # Trap must have requirement met to be triggered.
#     attack_stats: AttackStats

@dataclass
class GameState:
    """Aggregate root - the 'current situation' snapshot"""
    # Meta
    # session_id: str
    # created_at: datetime
    # updated_at: datetime
    
    # Player
    player: PlayerCharacter
    
    # Current context (what's immediately relevant)
    level: Level
    location: Room
    
    # Active interactions
    # active_combat: Combat | None
    # active_conversation: Conversation | None
    
    # Recent history (for context)
    recent_actions: list[str]  # last 5-10 actions

    def summary(self) -> str:
        """Returns a concise summary of game state for LLM context."""
        
        # Player summary
        pc = self.player
        equipped_names = ", ".join(item.name for item in pc.equipped) or "nothing"
        inventory = ", ".join(item.name for item in pc.inventory) or "empty"
        conditions = ", ".join(s.name for s in pc.conditions) or "none"
        
        player_summary = (
            f"PLAYER: Level {pc.level} {pc._class} | "
            f"HP: {pc.hp}/{pc.max_hp} | AC: {pc.ac} | "
            f"Conditions: {conditions}"
        )

        # Inventory summary
        inventory_summary = (
            f"INVENTORY: Equipped: {equipped_names} | {inventory}"
        )
        
        # Location summary
        location_summary = f"LOCATION: {self.location.name}\n{self.location.description}"
        
        # Entities in room
        entities = []
        for e in self.location.occupants:
            weapon = e.equipped[0].name if e.equipped else "unarmed"
            status = "hostile" if e.disposition == "hostile" else e.disposition
            entities.append(f"- {e.name}: HP {e.hp}/{e.max_hp}, AC {e.ac}, {weapon} ({status})")
        
        entities_summary = "ENTITIES:\n" + "\n".join(entities) if entities else "ENTITIES: None"
        
        # Room items
        items = [item.name for item in self.location.items] if self.location.items else []
        items_summary = f"ITEMS IN ROOM: {', '.join(items) or 'None'}"
        
        # Recent context
        recent = "\n".join(f"- {a}" for a in self.recent_actions[-5:])
        recent_summary = f"RECENT:\n{recent}" if recent else ""
        
        return "\n\n".join(filter(None, [
            player_summary,
            inventory_summary,
            location_summary,
            entities_summary,
            items_summary,
            recent_summary
        ]))