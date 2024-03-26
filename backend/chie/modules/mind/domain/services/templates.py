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
