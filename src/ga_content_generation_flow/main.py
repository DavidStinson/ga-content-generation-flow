#!/usr/bin/env python
import json

from random import randint

from pydantic import BaseModel

from crewai.flow import Flow, listen, start

from ga_content_generation_flow.crews.outline_crew.outline_crew import OutlineCrew
from ga_content_generation_flow.crews.content_crew.content_crew import ContentCrew
from ga_content_generation_flow.crews.ld_crew.ld_crew import LdCrew

from ga_content_generation_flow.data import documentation

token_history = []

class ContentState(BaseModel):
    # module_title: str = "Introduction to Javascript Arrays"
    # module_topic: str = "This JavaScript Arrays module is designed to provide a comprehensive introduction to arrays, a fundamental list datatype in programming. The module concludes with an extended practical exercise where learners will create, modify, and iterate through an array of strings. This content is suitable for beginners who are relatively new to JavaScript programming."
    # learner_persona: str = "Little to no prior coding experience; basic computer literacy is assumed. Students are adult learners and aspiring professionals."
    # learning_objectives: list[str] = [
    #     "Define JavaScript arrays and explain how they organize data.\n",
    #     "Identify the components of an array, including its elements and index positions.\n",
    #     "Create arrays using JavaScript literal notation.\n",
    #     "Access and modify elements within an array using square brackets.\n",
    #     "Use basic array methods, such as push() and pop(), to manage array data.\n"
    # ]
    # tools: str = "Visual Studio Code"

    module_title: str = "OUTREACH AND EMAIL AUTOMATION WITH AI"
    module_topic: str = "In this module you will explore how AI can support solving for time-consuming follow-ups, difficulty in personalizing emails at scale, low response rates due to generic content, testing and optimizing email campaigns can be labor intensive."
    learner_persona: str = "Salespeople who are responsible for reaching out to potential customers and closing deals. You are looking for a way to automate your outreach and email campaigns to save time and increase efficiency."
    learning_objectives: list[str] = [
        "Use effective email sequences and AI to engage prospects\n",
        "Apply the right personalization variables (e.g., role, company size, etc.) to create more tailored and relevant outreach\n",
        "Choose variables for personalization (e.g. role, company size, etc.) and use AI to automate the follow-ups\n",
    ]
    tools: str = "ChatGPT, Outreach"
    module_minutes: int = 40
    final_format: str = "Slides"
    microlessons: list[str] = []
    microlessons_text: list[str] = []
    microlessons_ld_text: list[str] = []
    doc_technical_voice: str = documentation["technical_voice"]
    doc_ga_learning_philosophy: str = documentation["general_assembly_learning_philosophy"]
    doc_ga_inclusivity_guidelines: str = documentation["ga_inclusivity_guidelines"]
    doc_exercise_instruction_guidelines: str = documentation["exercise_instruction_guidelines"]
    doc_markdown_document_structure: str = documentation["markdown_document_structure"]
    doc_crafting_modular_code: str = documentation["crafting_modular_code"]
    doc_writing_modularly: str = documentation["writing_modularly"]

class ContentGenerationFlow(Flow[ContentState]):
    @start()
    def generate_content(self):
        print("Generating content")

    @listen(generate_content)
    def generate_outline(self):
        print(self.state.module_title)
        print("Generating content outline")
        result = (
            OutlineCrew()
            .crew()
            .kickoff(inputs=self.state.model_dump())
        )

        token_history.append(result.token_usage)

        meta = json.loads(result.raw)

        print("OUTLINE GENERATED!!!")
        self.state.microlessons = meta["microlessons"]



        for microlesson in self.state.microlessons:
            microlesson_output = (
                ContentCrew()
                .crew()
                .kickoff(inputs={**self.state.model_dump(), **microlesson})
            )

            token_history.append(microlesson_output.token_usage)

            self.state.microlessons_text.append(microlesson_output.raw)
            self.state.microlessons[microlesson["id"] - 1]["sme_content"] = microlesson_output.raw

            print(self.state.microlessons[microlesson["id"] - 1])

            print("MICROLESSION GENERATED!!!")

        for microlesson in self.state.microlessons:
            microlesson_output = (
                LdCrew()
                .crew()
                .kickoff(inputs={**self.state.model_dump(), **microlesson})
            )

            token_history.append(microlesson_output.token_usage)

            self.state.microlessons_ld_text.append(microlesson_output.raw)

        print(self.state.microlessons_text)

        for item in token_history:
            print(item)


    # @listen(generate_poem)
    # def save_poem(self):
    #     print("Saving poem")
    #     with open("poem.txt", "w") as f:
    #         f.write(self.state.poem)


def kickoff():
    content_generation_flow = ContentGenerationFlow()
    content_generation_flow.kickoff()


def plot():
    content_generation_flow = ContentGenerationFlow()
    content_generation_flow.plot()


if __name__ == "__main__":
    kickoff()
