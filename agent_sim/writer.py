import json

from langchain.schema import SystemMessage, HumanMessage

from agent_sim.prompts_library import (
    WRITER_USER_PROMPT,
    WRITER_SYSTEM_PROMPT,
)

class Writer:
    def __init__(self, model, role, goal):
        self.model = model
        self.role = role
        self.goal = goal

    def write(self, previous_conversation, current_thoughts):
        llm_messages = [
            SystemMessage(content=WRITER_SYSTEM_PROMPT.format(self.role)),
            HumanMessage(WRITER_USER_PROMPT.format(previous_conversation=previous_conversation, thoughts=current_thoughts))
        ]
        new_thought = self.model.predict_messages(llm_messages).content
        return json.loads(new_thought)['thought']

