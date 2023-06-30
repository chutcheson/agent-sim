import json

from langchain.schema import SystemMessage, HumanMessage

from agent_sim.prompts_library import (
    EXTRACT_USER_PROMPT,
    REFLECT_USER_PROMPT,
    REFLECT_SYSTEM_PROMPT
    )

def extract_json(model, text):
    try:
        return json.loads(text)
    except:
        llm_messages = [
            HumanMessage(content=EXTRACT_USER_PROMPT.format(data=text))
        ]
        response = model.predict_messages(llm_messages).content
        return json.loads(response)


def reflect(sequencet_to_summarize):
    llm_messages = [
        SystemMessage(content=REFLECT_SYSTEM_PROMPT),
        HumanMessage(content=REFLECT_USER_PROMPT.format(
            sequence=sequence_to_summarize))
    ]
    response = self.model.predict_messages(llm_messages).content
    return response


