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
        """
        # Format updates as a bulleted list for clarity
        updates_formatted = "\n".join(f"- {update}" for update in updates)
        
        prompt = GMPrompts.NARRATE_STATE_UPDATE.format(summary=state_summary,updates_formatted=updates_formatted)

        return self.llm.generate(
            prompt,
            system_prompt=GMPrompts.NARRATE_SYSTEM_PROMPT
        )