import json

from langchain.schema import SystemMessage, HumanMessage

from agent_sim.util import extract_json
from agent_sim.prompts_library import (
    STYLIST_USER_PROMPT,
    STYLIST_SYSTEM_PROMPT,
)

class Stylist:
    def __init__(self, model, style):
        self.model = model
        self.style = style

    def stylize(self, current_message, message_history):
        llm_messages = [
            SystemMessage(content=STYLIST_SYSTEM_PROMPT.format(style=self.style)),
            HumanMessage(content=STYLIST_USER_PROMPT.format(previous_messages=message_history,message=current_message))
        ]
        stylized_message = self.model.predict_messages(llm_messages).content
        return stylized_message
