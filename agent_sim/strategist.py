import json

from langchain.schema import SystemMessage, HumanMessage

from agent_sim.prompts_library import (
    STRATEGIST_USER_PROMPT,
    STRATEGIST_SYSTEM_PROMPT,
)

class Strategist:
    def __init__(self, model, role, goal, strategy):
        self.model = model
        self.role = role
        self.goal = goal
        self.thoughts = ""

    def strategize(self, previous_conversation):
        llm_messages = [
            SystemMessage(content=STRATEGIST_SYSTEM_PROMPT.format(role=self.role, goal=self.goal)),
            HumanMessage(STRATEGIST_USER_PROMPT.format(
                conversation=previous_conversation,
                thoughts=self.thoughts)
        ]
        new_thought = self.model.predict_messages(llm_messages).content
        self.thoughts += new_thought
        return json.loads(new_thought)['strategy']

