import json

from langchain.schema import SystemMessage, HumanMessage

from agent_sim.util import extract_json
from agent_sim.prompts_library import (
    WRITER_USER_PROMPT,
    WRITER_SYSTEM_PROMPT,
)

class Writer:
    def __init__(self, model, role):
        self.model = model
        self.role = role

    def write(self, previous_conversation, current_thoughts):
        llm_messages = [
            SystemMessage(content=WRITER_SYSTEM_PROMPT.format(role=self.role)),
            HumanMessage(content=WRITER_USER_PROMPT.format(conversation=previous_conversation, thoughts=current_thoughts))
        ]
        message = self.model.predict_messages(llm_messages).content
        return message

