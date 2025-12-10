from typing import List
from src.game.llm.client import OllamaClient
from src.game.llm.prompts import GMPrompts

class NarratorOracle:
    """
    LLM interface for the Dungeon Master's narrative role
    Evolves the story through narration, interpreting game state updates into prose and adding it to the ongoing story.
    """
    
    def __init__(self, llm_client: OllamaClient):
        self.llm = llm_client
    
    def compose_narration(
        self,
        updates: List[str],
        state_summary: str
    ) -> str:
        """
        Transform mechanical game updates into immersive narrative prose.
        
        Args:
            updates: List of mechanical fragments describing actions and state changes.
                     e.g., ["[SUCCESS] Sword attack: rolled 18 vs AC 13", 
                            "[DAMAGE] 8 slashing damage to Goblin Scout",
                            "[STATE] Goblin Scout HP: 12 -> 4"]
            state_summary: Paragraph summarizing the current game state including
                          relevant entity positions, conditions, and environment.
            history: Context summarizing the story thus far. Older sections are
                    condensed while recent events have greater detail.
        
        Returns:
            Prose narration describing the events without referencing any game
            mechanics, numbers, or meta-game concepts. Pure story narration
            suitable for player immersion.
        
        Example:
            >>> updates = [
            ...     "[SUCCESS] Sword attack: rolled 18 vs AC 13",
            ...     "[DAMAGE] 8 slashing damage to Goblin Scout"
            ... ]
            >>> state_summary = "A wounded goblin scout cornered in the dim cellar..."
            >>> history = "After descending into the ruins, you encountered a patrol..."
            >>> narration = gm.compose_narration(updates, state_summary, history)
            >>> print(narration)
            "Your blade finds its mark, slicing through the goblin's leather armor.
             The creature shrieks and stumbles backward, clutching at the wound."
        """
        # Format updates as a bulleted list for clarity
        updates_formatted = "\n".join(f"- {update}" for update in updates)
        
        prompt = GMPrompts.NARRATE_STATE_UPDATE.format(history=history,state_summary=state_summary,updates_formatted=updates_formatted)

        return self.llm.generate(
            prompt,
            system_prompt=GMPrompts.NARRATE_SYSTEM_PROMPT
        )