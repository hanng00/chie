from chie.modules.mind.domain.ports.llm import LLMPort
from openai import AsyncOpenAI


class OpenAILLM(LLMPort):
    def __init__(self, openai: AsyncOpenAI):
        self.openai = openai

    async def completion(self, instruction: str, prompt: str) -> str:
        messages = [
            {"role": "system", "content": instruction},
            {"role": "user", "content": prompt},
        ]

        completion = await self.openai.chat.completions.create(
            messages=messages,
            model="gpt-3.5-turbo",
        )

        return completion.choices[0].message.content
