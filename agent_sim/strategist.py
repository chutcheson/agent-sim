import json

from langchain.schema import SystemMessage, HumanMessage

from agent_sim.util import extract_json
from agent_sim.prompts_library import (
    STRATEGIST_USER_PROMPT,
    STRATEGIST_SYSTEM_PROMPT,
    REFLECT_USER_PROMPT,
    REFLECT_SYSTEM_PROMPT
)

class Strategist:
    def __init__(self, model, role, goal):
        self.model = model
        self.role = role
        self.goal = goal
        self.thoughts = ["This is the start of the conversation. I should lay out the background."]
        self.max_thought_len = 3000

    def strategize(self, previous_conversation):
        merged_thoughts = "\n".join([f"Thought {i}: {thought}" for i, thought in enumerate(self.thoughts)])
        if len(merged_thought) >= 3000:
            self.reflect()
            merged_thoughts = self.thoughts[0]
        llm_messages = [
            SystemMessage(content=STRATEGIST_SYSTEM_PROMPT.format(role=self.role, goal=self.goal)),
            HumanMessage(content=STRATEGIST_USER_PROMPT.format(
                conversation=previous_conversation,
                thoughts=merged_thoughts))
        ]
        response = self.model.predict_messages(llm_messages).content
        self.thoughts.append(response)
        return response

    def reflect(self):
        llm_messages = [
            SystemMessage(content=REFLECT_SYSTEM_PROMPT),
            HumanMessage(content=REFLECT_USER_PROMPT.format(
                sequence="\n".join(self.thoughts))
        ]
        response = self.model.predict_messages(llm_messages).content
        self.thoughts.append(response)
        return response


 


