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

Your job is to come with a summary of your past thoughts that includes an idea for your next approach to achieve your goal.

You should take your past thoughts, brainstorm possible approaches, then come up with a new thought that will help you achieve your goal and write it down.

That new thought could be a continuation of the previous thoughts or a new thought entirely.

If there are no previous thoughts then it is the start of the conversation. 

In that case, come up with a first thought for yourself as to how to approach the conversation.

Your thoughts are internal thoughts that are only in your own mind.
"""

WRITER_USER_PROMPT = """
Conversation: {conversation}

Thoughts: {thoughts}
"""

WRITER_SYSTEM_PROMPT = """
Your job is to write the next message in an exchange.

You should base the message on the conversation so far and on your thoughts.

Messages should be short and succinct. No more than a sentence or two.

The past conversation is in a format like this:

Speaker: <speaker>
Message: <message>

You are {role}.
"""

STYLIST_USER_PROMPT = """
Message: {message}
"""

STYLIST_SYSTEM_PROMPT = """
You are master author. Your job is to rewrite a message in a particular style.

Style: {style}
"""

EXTRACT_USER_PROMPT = """
Data: {data}

Extract the JSON. Return only the JSON.

If you receive this message:

Here is the JSON:

{{ ... }}

Return 

{{ ... }}

If you receive this message:

{{ ... }}

Return:

{{ ... }}
"""
