from agent_sim.strategist import Strategist
from agent_sim.writer import Writer
from agent_sim.stylist import Stylist

class Player:
    def __init__(self, model, role, goal, style):
        self.role = role
        self.strategist = Strategist(model, role, goal)
        self.writer = Writer(model, role)
        self.stylist = Stylist(model, style)

    def turn(self, world_state):
        message_history = world_state.get_message_history(self.role)
        strategy = self.strategist.strategize(message_history)
        message = self.writer.write(message_history, strategy)
        stylized_message = self.stylist.stylize(message, message_history)
        return f"Sender: {self.role}\n Message: {stylized_message}"
