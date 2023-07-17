from langchain.scheuma import HumanMessage

from agent_sim.llm_agent import LLMAgent
from agent_sim.conversational_agent_modules import Memory, Thinker, Speaker

class ConversationalAgent(LLMAgent):

    def __init__(self, unique_id, model, llm, memory=None, thinker=None, speaker=None):
        
        # Initialize parent LLMAgent
        super().__init__(unique_id, model, llm)
        
        # Initialize the memory, thinker and speaker modules
        if memory:
            self.memory = memory 
        else:
            self.memory = Memory(self)
            
        if thinker:
            self.thinker = thinker
        else:
            self.thinker = Thinker(self)
            
        if speaker:
            self.speaker = speaker
        else:
            self.speaker = Speaker(self)
            
        # Lists to store agent thoughts and recollections
        self.thoughts = []
        self.recollection = None

    def step(self):
        """One step for the agent involves: remember -> think -> speak"""
        
        # Call memory module to update recollection
        # self.recollection is set as the new recollection
        self.memory.remember()
        
        # Call thinker module to update thoughts
        # Thoughts are added to self.thoughts
        self.thinker.think()
        
        # Call speaker module to generate utterance
        # Utterance is added to the model message history
        self.speaker.speak()
