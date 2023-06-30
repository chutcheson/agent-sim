class Simulation:
    def __init__(self, agents, monitor, max_turns=None):
        self.agents = agents
        self.monitor = monitor
        self.max_turns = max_turns
        self.messages = ""
        self.turns_taken = 0

    def run(self):
        while True:
            for agent in self.agents:
                message = agent.next_message(self.messages)
                print(message)
                self.messages += f"\n{message}"
                self.turns_taken += 1

            if self.monitor.check_condition(self.messages):
                print(self.messages)
                return

            if self.max_turns and self.turns_taken >= self.max_turns:
                print(self.messages)
                return
