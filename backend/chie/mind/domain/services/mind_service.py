import random
from typing import Dict, List
from chie.mind.domain.entities.knowlet import Knowlet
from chie.mind.domain.entities.question import Question
from chie.mind.domain.ports.llm import LLMPort
from chie.mind.utils import get_current_utc_time
from chie.logger import get_logger

PROMPT = (
    lambda learning_style, response_length: f"""
TASK:
You will be provided a question from the user. Use the provided learning style to formulate your response. Be creative.

LEARNING STYLE:
{learning_style}

RESPONSE LENGTH:
- Use Markdown for improved readability
- Keep the response under {response_length} characters
"""
)

LEARNING_STYLES = [
    {
        "name": "Socratic Dialogues",
        "instruction": "Encourage open-ended questions and engage students in discussions. Prompt them to explore ideas and perspectives through a series of thought-provoking questions. Foster an environment where students actively participate in the dialogue, sharing and challenging each other's thoughts.",
    },
    {
        "name": "Narrative Learning",
        "instruction": "Integrate storytelling into your teaching approach. Craft narratives that illustrate key concepts or historical events related to the topic. Use relatable characters and situations to make the information memorable. Encourage students to create their own narratives to reinforce understanding.",
    },
    {
        "name": "Hands-On Experiences",
        "instruction": "Incorporate practical activities into the learning process. Provide hands-on projects, experiments, or real-world applications related to the subject matter. Guide students through the steps and ensure they actively engage in the experiential learning process.",
    },
    {
        "name": "Reflective Learning",
        "instruction": "Allocate time for reflection exercises. Encourage students to journal their thoughts on the material covered, their understanding, and any questions that arise. Discuss these reflections in class to deepen understanding and facilitate self-awareness.",
    },
    {
        "name": "Collaborative Learning",
        "instruction": "Foster a collaborative learning environment. Organize group activities, discussions, or projects where students can work together to explore the topic. Provide guidelines for effective collaboration and encourage each student to contribute their insights.",
    },
    {
        "name": "Visual Learning",
        "instruction": "Enhance visual learning by incorporating diagrams, charts, and infographics into your presentations. Use visual aids to represent complex ideas and relationships. Encourage students to create visual summaries or mind maps to reinforce their understanding.",
    },
    {
        "name": "Exploratory Learning",
        "instruction": "Promote independent exploration. Assign research projects or topics for self-directed study. Provide resources and guidelines for effective exploration, and encourage students to share their findings with the class.",
    },
    {
        "name": "Problem-Based Learning",
        "instruction": "Introduce real-world problems related to the subject matter. Guide students through the process of analyzing, researching, and solving these problems collaboratively. Emphasize the application of theoretical knowledge to practical situations.",
    },
    {
        "name": "Interactive Simulations",
        "instruction": "Utilize interactive simulations to illustrate complex concepts. Demonstrate how to access and navigate the simulations, and encourage students to explore different scenarios. Facilitate discussions on the insights gained from the interactive experiences.",
    },
    {
        "name": "Mnemonic Devices",
        "instruction": "Teach students mnemonic devices to aid memory. Provide examples and guide them in creating their own memory aids, such as acronyms or rhymes, to remember key information. Encourage the use of mnemonic devices during review sessions to reinforce retention.",
    },
]


MOCK_LIST_KNOWLETS = [
    {
        "title": "Narrative Learning",
        "content": """## Reading through the topic of narrative learning""",
    },
    {
        "title": "Socratic Dialogues",
        "content": """## Understanding Computational Neuroscience Through Real-World Problems

Imagine designing a brain-computer interface for paralyzed patients to control robotic limbs. 
1. Identify the neural circuitry involved.
2. Research how neural signals can be decoded into movement commands.
3. Collaborate to refine algorithms for real-time processing.
4. Apply computational neuroscience principles to improve accuracy and responsiveness.
5. Test and troubleshoot the system in simulated and real-world scenarios.
6. Reflect on the ethical implications and societal impact of your work.""",
    },
]

logger = get_logger(__name__)


class MindService:
    def __init__(self, llm: LLMPort) -> None:
        self.llm = llm

        self.learning_style = LEARNING_STYLES
        self.prompt = PROMPT

    async def ask_mind(self, question: Question) -> List[Knowlet]:
        random_learning_styles = random.sample(self.learning_style, 3)
        logger.info(random_learning_styles)

        knowlets = []
        for ls in random_learning_styles:
            name, instruction = ls["name"], ls["instruction"]
            instruction_prompt = self.prompt(instruction, 500)
            completion = await self.llm.completion(
                instruction=instruction_prompt, prompt=question.content
            )

            knowlet = Knowlet(
                title=name,
                content=completion,
                question=question,
                created_at=get_current_utc_time(),
            )
            knowlets.append(knowlet)
        return knowlets

    async def get_knowlets(self) -> List[Knowlet]:
        current_utc_time = get_current_utc_time()

        # MOCK DATA
        mock_question = Question(
            content="What is the meaning of life?",
            created_at=current_utc_time,
        )
        mock_knowlets = [
            Knowlet(
                title=data.get("title"),
                content=data.get("content"),
                question=mock_question,
                created_at=current_utc_time,
            )
            for data in MOCK_LIST_KNOWLETS
        ]

        return mock_knowlets
