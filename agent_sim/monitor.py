import json

from langchain.schema import SystemMessage, HumanMessage

from agent_sim.util import extract_json
from agent_sim.prompts_library import (
    MONITOR_USER_PROMPT,
    MONITOR_SYSTEM_PROMPT,
)


class Monitor:
    def __init__(self, model, condition):
        self.model = model
        self.condition = condition

    def check_condition(self, message_history):
        llm_messages = [
            SystemMessage(content=MONITOR_SYSTEM_PROMPT),
            HumanMessage(content=MONITOR_USER_PROMPT.format(messages=message_history, condition=self.condition))
        ]
        response = self.model.predict_messages(llm_messages).content
        json_response = extract_json(self.model, response)
        return json_response['condition']



