from langchain.schema import HumanMessage

# Determines the external information to which the agent has access
class Memory:
    def __init__(self, agent, prompt=None):
        self.agent = agent
        self.prompt = prompt

    def remember(self, **kwargs):
        if not prompt:
            self.agent.recollection = "".join(self.agent.model.message_history)
        else:
            self.agent.recollection = self.agent.llm.predict_messages([HumanMessage(self.prompt.format(**kwargs))])

# Updates the internal state of the agent
class Thinker:
    def __init__(self, agent, prompt=None):
        self.agent = agent
        self.prompt = prompt

    def think(self):
        if not prompt:
            self.agent.thoughts.append(Thought(self.agent.model.schedule.time, ""))
        else:
            self.agent.thoughts.append(Thought(self.agent.model.schedule.time, self.agent.llm.predict_messages([HumanMessage(self.prompt)])))

# Structure for internal thoughts of the agent
class Thought:
    def __init__(self, timestamp, content):
        self.timestamp = timestamp
        self.content = content

# Determines the information that the agent reveals to the rest of the model
class Speaker:
    def __init__(self, agent, prompt=None):
        self.agent = agent
        self.prompt = prompt
        # Add a prompt property if needed

    def speak(self):
        if not prompt:
        else:
            content = self.agent.llm.predict_messages([HumanMessage(self.prompt)])
            self.agent.model.message_history.append(Message(self.agent.unique_id, self.agent.recipient, self.agent.model.schedule.time, content, self.agent.model.message_id))

