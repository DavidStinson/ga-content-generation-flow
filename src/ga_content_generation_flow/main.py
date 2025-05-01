#!/usr/bin/env python
import json

from pydantic import BaseModel

from crewai.flow import Flow, listen, start

from ga_content_generation_flow.crews.outline_crew.outline_crew import OutlineCrew
from ga_content_generation_flow.crews.content_crew.content_crew import ContentCrew
from ga_content_generation_flow.crews.ld_crew.ld_crew import LdCrew
from ga_content_generation_flow.crews.slides_crew.slides_crew import SlidesCrew

from ga_content_generation_flow.data import documentation

token_history = []

class ContentState(BaseModel):
    
    # module_title: str = "Introduction to Javascript Arrays"

    # module_topic: str = "This JavaScript Arrays module is designed to provide a comprehensive introduction to arrays, a fundamental list datatype in programming. The module concludes with an extended practical exercise where learners will create, modify, and iterate through an array of strings. This content is suitable for beginners who are relatively new to JavaScript programming."

    # module_minutes: int = 90

    # learner_persona: str = "Little to no prior coding experience; basic computer literacy is assumed. Students are adult learners and aspiring professionals."

    # learning_objectives: list[str] = [
    #     "Define JavaScript arrays and explain how they organize data.",
    #     "Identify the components of an array, including its elements and index positions.",
    #     "Create arrays using JavaScript literal notation.",
    #     "Access and modify elements within an array using square brackets.",
    #     "Use basic array methods, such as push() and pop(), to manage array data."
    # ]

    # tools: str = "Visual Studio Code"

    module_title: str = "AI for HR workshop"

    module_topic: str = "AI and generative AI tools for HR professionals."

    learner_persona: str = "HR professionals who are looking to use AI to automate their work and improve their efficiency."

    module_minutes: int = 60

    learning_objectives: list[str] = [
        "Differentiate between different types of AI in the HR space.",
        "Describe the use cases and capabilities of HR-specific AI tools.",
        "Recognize key ethical risks associated with using AI in HR, including bias, transparency, and accountability.",
        "Explain how large language models (e.g., ChatGPT) generate text.",
        "Identify the limitations of large language models (e.g., ChatGPT) including risks like hallucination and over-trust."
    ]

    tools: str = "Webinar style - no tools but participants can be given a worksheet to fill out during the lesson."

    final_format: str = "markdown"

    doc_technical_voice: str = documentation["technical_voice"]

    doc_ga_learning_philosophy: str = documentation["general_assembly_learning_philosophy"]

    doc_ga_inclusivity_guidelines: str = documentation["ga_inclusivity_guidelines"]

    doc_exercise_instruction_guidelines: str = documentation["exercise_instruction_guidelines"]

    doc_markdown_document_structure: str = documentation["markdown_document_structure"]

    doc_crafting_modular_code: str = documentation["crafting_modular_code"]

    doc_writing_modularly: str = documentation["writing_modularly"]

    microlessons: list[dict] = []

class ContentGenerationFlow(Flow[ContentState]):
    @start()
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

        self.state.microlessons = meta["microlessons"]

        for microlesson in self.state.microlessons:
            microlesson["microlessons_text"] = ""
            if microlesson["id"] > 1:
                numOfPreviousMicrolessons = microlesson["id"] - 1

                for microlesson in self.state.microlessons:
                    if microlesson["id"] >= numOfPreviousMicrolessons:
                        break

                    microlesson["microlessons_text"] = f"{microlesson["microlessons_text"]} {microlesson['sme_content']}"
                    print("MICROLESSONS TEXT:", microlesson["microlessons_text"])
            
            print("MICROLESSONS TEXT:", microlesson["microlessons_text"])

            microlesson_output = (
                ContentCrew()
                .crew()
                .kickoff(inputs={
                    **self.state.model_dump(),
                    **microlesson
                })
            )
            token_history.append(microlesson_output.token_usage)

            # changing this from something that I know works to test...
            # apply this below if it works!
            microlesson["sme_content"] = microlesson_output.raw

        if self.state.final_format != "Slides":

            for microlesson in self.state.microlessons:
                microlesson["microlessons_text"] = ""
                if microlesson["id"] > 1:
                    numOfPreviousMicrolessons = microlesson["id"] - 1

                    for microlesson in self.state.microlessons:
                        if microlesson["id"] >= numOfPreviousMicrolessons:
                            break

                        microlesson["microlessons_text"] = f"{microlesson["microlessons_text"]} {microlesson['led_content']}"
                        print("MICROLESSONS TEXT:", microlesson["microlessons_text"])
            

                microlesson_output = (
                    LdCrew()
                    .crew()
                    .kickoff(inputs={
                        **self.state.model_dump(),
                        **microlesson
                    })
                )

                self.state.microlessons[microlesson["id"] - 1]["led_content"] = microlesson_output.raw

                token_history.append(microlesson_output.token_usage)

        if self.state.final_format == "Slides":
            for microlesson in self.state.microlessons:
                microlesson_output = (
                    SlidesCrew()
                    .crew()
                    .kickoff(inputs={**self.state.model_dump(), **microlesson})
                )

                token_history.append(microlesson_output.token_usage)

        for item in token_history:
            print(item)

        module = {
            "title": self.state.module_title,
            "about": self.state.module_topic,
            "learner_persona": self.state.learner_persona,
            "prerequisites": [],
            "tools": [],
            "qa_reasoning": "",
            "microlessons": self.state.microlessons
        }

        return json.dumps(self.state.microlessons)

def kickoff():
    content_generation_flow = ContentGenerationFlow()
    content_generation_flow.kickoff()


def plot():
    content_generation_flow = ContentGenerationFlow()
    content_generation_flow.plot()


if __name__ == "__main__":
    kickoff()
