import json

from langchain.schema import SystemMessage, HumanMessage

from agent_sim.prompts_library import EXTRACT_USER_PROMPT

def extract_json(model, text):
    try:
        return json.loads(text)
    except:
        llm_messages = [
            HumanMessage(content=EXTRACT_USER_PROMPT.format(data=text))
        ]
        response = model.predict_messages(llm_messages).content
        return json.loads(response)

