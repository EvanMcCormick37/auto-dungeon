from typing import List, Tuple
from src.game.models.base import Base, Item, Lore, Action, Status, AttackStats, Requirement
from src.game.models.character import Entity
class Trap(Base):
    perception_difficulty: int
    reqs: List[Requirement] | None          # The list of possible actions which could trigger the trap's effect.
    attack_stats: AttackStats
    live: bool
    rounds: int

class Location(Base):
    explored: bool
    traps: List[Trap] | None
    possibilities: List[Lore] | None
    is_explored: bool

class Door(Location):
    next_room_id: str                       # ID of connecting room.
    is_open: bool
    is_locked: bool

class Room(Location):
    doors: List[Door] | None
    occupants: List[Entity] | None
    items: List[Item] | None

class Level(Base):
    room_ids: List[str]
    hooks: List[Lore] | None
    effects: List[Status] | None