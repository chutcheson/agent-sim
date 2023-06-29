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

    def stylize(self, current_message):
        llm_messages = [
            SystemMessage(content=STYLIST_SYSTEM_PROMPT.format(style=self.style)),
            HumanMessage(content=STYLIST_USER_PROMPT.format(message=current_message))
        ]
        stylized_message = self.model.predict_messages(llm_messages).content
        json_message = extract_json(self.model, stylized_message)
        return json_message['styled_message']
