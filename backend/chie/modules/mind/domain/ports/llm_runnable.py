from typing import Protocol


class LLMRunnablePort(Protocol):
    def invoke(self, input: str) -> str:
        pass
