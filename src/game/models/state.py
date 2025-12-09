from src.game.models.base import Item
from src.game.models.character import PlayerCharacter, Entity, Conversation
from src.game.models.location import Room, Level
from datetime import datetime
from typing import List

class CombatantStatus:
    entity: Entity
    friendly: bool


class Combat:
    current_active_entity: str
    combatants: List[CombatantStatus]

class GameState:
    """Aggregate root - the 'current situation' snapshot"""
    # Meta
    session_id: str
    created_at: datetime
    updated_at: datetime
    
    # Player
    player: PlayerCharacter
    
    # Current context (what's immediately relevant)
    current_level: Level
    current_room: Room

    
    # Active interactions
    active_combat: Combat | None
    active_conversation: Conversation | None
    
    # Recent history (for context)
    recent_actions: list[str]  # last 5-10 actions