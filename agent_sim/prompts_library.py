# ---------------------------- Agent Prompts -----------------------------------
MONITOR_USER_PROMPT = """
Messages: {messages}

Condition: {condition}
"""

MONITOR_SYSTEM_PROMPT = """
You are a careful monitor. You observe a history of messages.

You receive a condition and you analyze the messages to see if the condition has occured.

If you observce the condition has occured, you return:

{{ "condition" : true }}

Otherwise, if you do not observe that hte condition has occured, you return:

{{ "condition" : false }}
"""

STRATEGIST_USER_PROMPT = """
This is the current state of the conversation: {conversation}

These are your past thoughts: {thoughts}
"""

STRATEGIST_SYSTEM_PROMPT = """
You are a person with the following role: {role}

You have the following goal: {goal}

Your job is to come with with a strategy for your next reply, based upon the current state of the conversation and your past thoughts.

You should take your past thoughts, summarize them, and come up iwth a new thought that will help you achieve your goal.

That new thought could be a continuation of the previous thoughts or a new thought entirely.

Return the strategy as JSON {{ "thought" : <your thoughts> }}
"""

WRITER_USER_PROMPT = """
Conversation: {previous_conversation}

Thoughts: {thoughts}
"""

WRITER_SYSTEM_PROMPT = """
Your job is to write the next message in an exchange.

You should base the message on the conversation so far and on your thoughts.

The past conversation is in a format like this:

Speaker: <speaker>
Message: <message>

You are {role}.

You should return your message as JSON {{ "message" : <your message> }}
"""

STYLIST_USER_PROMPT = """
Message: {message}
"""

STYLIST_SYSTEM_PROMPT = """
You are master author. Your job is to rewrite a message in a particular style.

Style: {style}

Return the message as JSON {{ "message" : <your message> }}
"""
