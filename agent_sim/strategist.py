import json

from langchain.schema import SystemMessage, HumanMessage

from agent_sim.util import extract_json
from agent_sim.prompts_library import (
    STRATEGIST_USER_PROMPT,
    STRATEGIST_SYSTEM_PROMPT,
)

class Strategist:
    def __init__(self, model, role, goal):
        self.model = model
        self.role = role
        self.goal = goal
        self.thoughts = ""

    def strategize(self, previous_conversation):
        llm_messages = [
            SystemMessage(content=STRATEGIST_SYSTEM_PROMPT.format(role=self.role, goal=self.goal)),
            HumanMessage(content=STRATEGIST_USER_PROMPT.format(
                conversation=previous_conversation,
                thoughts=self.thoughts))
        ]
        response = self.model.predict_messages(llm_messages).content
        print(response)
        json_response = extract_json(self.model, response)
        new_thought = json_response['thought']
        self.thoughts = new_thought
        return new_thought

