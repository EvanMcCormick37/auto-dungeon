# Attributes (D&D standard six)
class Attributes:
    strength: int
    dexterity: int
    constitution: int
    intelligence: int
    wisdom: int
    charisma: int

# Derived modifiers, proficiency bonus
class PCStats:
    name: str
    character_class: str
    level: int
    experience: int
    attributes: Attributes
    max_hp: int
    current_hp: int
    armor_class: int
    proficiency_bonus: int
    skills: dict[str, int]  # skill_name -> modifier
    saving_throws: dict[str, int]
    inventory: list[str]  # item IDs
    equipped: dict[str, str | None]  # slot -> item_id
    gold: int
    conditions: list[str]  # poisoned, prone, etc.