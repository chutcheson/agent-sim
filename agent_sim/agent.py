from typing import Any, List, Optional, Union

from langchain.base_language import BaseLanguageModel
from langchain.callbacks.manager import Callbacks
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import SystemMessage, HumanMessage

from agent_sim.prompts_library import (
    INPUT_PROMPT,
    REFLECT_USER_PROMPT,
    REFLECT_SYSTEM_PROMPT,
)


class Agent:
    """
    A class used to represent an Agent.

    Attributes:
        memory (List[str]): A list storing the messages.
        memory_length (int): The length of the memory in characters.
        respond_model (Model): A model used to process messages.
        reflect_model (Model): A model used to summarize memories
        inception_prompt (str): A string used as the initial prompt for the model.
    """

    def __init__(
        self,
        respond_model: BaseLanguageModel,
        reflect_model: BaseLanguageModel,
        inception_prompt: str,
        role_name: str,
    ) -> None:
        """
        Constructs the necessary attributes for the Agent object.
        """

        self.respond_model = respond_model
        self.reflect_model = reflect_model
        self.inception_prompt = inception_prompt
        self.role_name = role_name

        self.memory: List[str] = []
        self.memory_length: int = 0

    def respond(self, input_message: str) -> Union[str, Any]:
        """
        Responds to a message based on an input and the previous memory.
        """

        human_prompt = INPUT_PROMPT.format("\n".join(self.memory), input_message)
        prompt = ChatPromptTemplate.from_messages(
            [
                SystemMessagePromptTemplate.from_template(self.inception_prompt),
                HumanMessagePromptTemplate.from_template(human_prompt),
            ]
        ).format_messages(memory=self.memory)

        return self.respond_model.predict_messages(
            prompt, tags=[self.role_name, "respond"]
        ).content

    def add_to_memory(self, role: str, message: str) -> None:
        """
        Adds a message to the memory.

        This is not automatically done within respond because the messages could be manipulated
        before being added to the memory.
        """

        message = f"{role}: {message}"
        self.memory.append(message)
        self.memory_length += len(message)

        # Summarize messages if too long
        self.reflect()

    def reflect(self) -> None:
        """
        Reflects and summarizes memories so that it fits into the context length.

        If the memory_length is too long, it selects a number of messages from the memory,
        uses the model to summarize them, and replaces them in the memory with the summary.
        """
        if self.memory_length >= 1000:
            # Process the top 10 messages or however much is available,
            # always leave at least two messages for immediate context
            num_messages = min(10, len(self.memory) - 2)
            messages_to_process = "\n".join(self.memory[:num_messages])
            processed_messages = self.reflect_model.predict_messages(
                [
                    SystemMessage(content=REFLECT_SYSTEM_PROMPT),
                    HumanMessage(
                        content=REFLECT_USER_PROMPT.format(messages_to_process)
                    ),
                ],
                tags=[self.role_name, "reflect"],
            ).content

            # Replace the messages in memory with the processed output
            self.memory = [processed_messages] + self.memory[num_messages:]

            # Recalculate memory_length
            self.memory_length = sum(len(message) for message in self.memory)