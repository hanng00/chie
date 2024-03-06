
from typing import Protocol


class LLMPort(Protocol):
  """ Abstract Interface for interacting with an LLM """

  def completion(self, instruction: str, prompt: str) -> str:
    """ Generate a completion for a given prompt. """