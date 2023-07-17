import mesa

class LLMAgent(mesa.Agent):
    def __init__(self, unique_id, model, llm):
        super().__init__(unique_id, model)
        self.llm = llm
