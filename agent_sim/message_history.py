class Message:
    def __init__(self, sender, recipient, timestamp, message, message_id):
        self.message_id = message_id
        self.sender = sender
        self.recipient = recipient
        self.timestamp = timestamp
        self.message = message

class MessageHistory:
    def __init__(self, model):
        self.model = model
        self.model = []
        self.message_id = 0

    def add_message(self, sender, recipient = "all", message = "", timestamp = None):
        if timestamp is None:
            timestamp = self.model.schedule.time
        self.messages.append(Message(sender, recipient, timestamp, message, self.message_id))
        self.message_id += 1

    def get_messages_by_timestamp(self, timestamp):
        return [msg for msg in self.messages if msg.timestamp == timestamp]

    def get_messages_by_sender(self, sender):
        return [msg for msg in self.messages if msg.sender == sender]

    def get_messages_by_recipient(self, recipient):
        return [msg for msg in self.messages if msg.recipient == recipient]

    def get_messages(self):
        return self.messages

    def get_messages_as_string(self):
        messages_str = []
        for message in self.messages:
            message_string = f"From: {message.sender}, To: {message.recipient}, Time: {message.timestamp}, Message: {message.message}"
            messages_str.append(message_string)
        return "\n".join(messages_str)

