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
    module_title: str
    module_topic: str
    module_minutes: int
    learner_persona: str
    learning_objectives: list[str]
    tools: str
    final_format: str = "markdown"
    prerequisites: list[str] = []

    # referenced internal documentation
    doc_technical_voice: str = documentation["technical_voice"]
    doc_ga_learning_philosophy: str = documentation["ga_learning_philosophy"]
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

        self.state.prerequisites = meta["prerequisites"]
        self.state.microlessons = meta["microlessons"]

        for microlesson in self.state.microlessons:
            microlesson["microlessons_text"] = ""
            if microlesson["id"] > 1:
                numOfPreviousMicrolessons = microlesson["id"] - 1

                for microlesson in self.state.microlessons:
                    if microlesson["id"] >= numOfPreviousMicrolessons:
                        break

                    microlesson["microlessons_text"] = f"{microlesson['microlessons_text']} {microlesson['sme_content']}"
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

                        microlesson["microlessons_text"] = f"{microlesson['microlessons_text']} {microlesson['led_content']}"
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
            "prerequisites": [self.state.prerequisites],
            "tools": [self.state.tools],
            "microlessons": self.state.microlessons
        }

        print(module)

        return json.dumps(module)

def kickoff():
    content_generation_flow = ContentGenerationFlow()
    content_generation_flow.kickoff(inputs={
        "tools": "VS Code",
        "final_format": "markdown",
        "module_title": "Intro to Flexbox",
        "module_topic": "Learn how to use CSS Flexbox for layout design.",
        "microlessons": [],
        "module_minutes": 60,
        "learner_persona": "Beginner web developers",
        "learning_objectives": [
            "Describe how Flexbox works",
            "Use flex-direction and justify-content",
            "Create a responsive nav bar"
        ],
        "doc_technical_voice": "Use clear, precise language suitable for adult learners with minimal jargon.",
        "doc_writing_modularly": "Break complex content into small, reusable, and focused learning blocks.",
        "doc_crafting_modular_code": "Write example code that is concise, logically scoped, and reusable.",
        "doc_ga_learning_philosophy": "Focus on practical, project-based learning with real-world relevance.",
        "doc_ga_inclusivity_guidelines": "Use inclusive examples and avoid assumptions about prior experience.",
        "doc_markdown_document_structure": "Organize content with clear headings, bullet points, and consistent formatting.",
        "doc_exercise_instruction_guidelines": "Write instructions that are step-by-step, beginner-friendly, and goal-driven."
    })


def plot():
    content_generation_flow = ContentGenerationFlow()
    content_generation_flow.plot()


if __name__ == "__main__":
    kickoff()
