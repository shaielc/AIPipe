
from datatypes.content_types import StringContent
from typing import List, TypedDict
import requests

class ChatTurn(TypedDict):
    user: str
    assistant: str

TURN_FORMAT: ChatTurn = {
    "user": "### Human: {content}",
    "assistant": "### Assistant: {content}"
}
SYSTEM_PROMPT = "A chat between a curious human and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the human's questions."


class LlamaCPPServerBackend:
    """LLM provider through Llama CPP Server.
    """
    def __init__(self, base_url, **options) -> None:
        self.base_url = base_url
        self.options = {
            "stop": [f'\n{TURN_FORMAT["user"].format(content="")}']
        }
        self.options.update(**options)
        self.history: List[ChatTurn] = []
    
    def format_prompt(self, prompt):
        formatted_prompt = SYSTEM_PROMPT + "\n" + "\n".join(
            [
                f'{TURN_FORMAT["user"].format(content=turn["user"])}\n' + \
                f'{TURN_FORMAT["assistant"].format(content=turn["assistant"])}'
                for turn
                in self.history
            ]
        )
        return formatted_prompt + "\n" + \
            f'{TURN_FORMAT["user"].format(content=prompt)}\n' + \
            f'{TURN_FORMAT["assistant"].format(content="")}'

    def chat(self, prompt):
        response = requests.post(
            f"{self.base_url}/completion",
            json={
                "prompt": prompt,
                **self.options
            }
        )
        return response.json()["content"]
        
         
    def process(self, prompt: str):
        formatted_prompt = self.format_prompt(prompt)
        response = self.chat(formatted_prompt)
        self.history.append(
            {
                "user": prompt,
                "assistant": response,
            }
        )
        return response
    
    def reset(self, ):
        self.history = []