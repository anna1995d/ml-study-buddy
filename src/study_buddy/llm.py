# llm.py

from openai import OpenAI
from study_buddy import config

client = OpenAI()

def ask(prompt:str) -> str:
    """Send a single user prompt, return the model's text reply."""
    response = client.chat.completions.create(
        model=config.MODEL,
        messages=[{"role":"system", "content":config.SYSTEM_PROMPT},
                  {"role":"user", "content":prompt}]
    )

    return response.choices[0].message.content

class Conversation:
    """Holds message history so the model remembers the exchange."""

    def __init__(self):
        self.messages = [
            {"role": "system", "content": config.SYSTEM_PROMPT},
        ]

    def send(self, prompt:str) -> str:
        self.messages.append({"role":"user", "content":prompt})
        response = client.chat.completions.create(
            model=config.MODEL,
            messages=self.messages
        )
        reply = response.choices[0].message.content
        self.messages.append({"role": "assistant", "content": reply})

        return reply