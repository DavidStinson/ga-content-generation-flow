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
    module_title: str = ""
    module_topic: str = ""
    module_minutes: int = 0
    learner_persona: str = ""
    learning_objectives: list[str] = []
    tools: list[str] = []
    final_format: str = "markdown"
    prerequisites: list[str] = []
    microlessons: list[dict] = []
    microlessons_text: str = ""

    # referenced internal documentation
    doc_technical_voice: str = documentation["technical_voice"]
    doc_ga_learning_philosophy: str = documentation["ga_learning_philosophy"]
    doc_ga_inclusivity_guidelines: str = documentation["ga_inclusivity_guidelines"]
    doc_exercise_instruction_guidelines: str = documentation["exercise_instruction_guidelines"]
    doc_markdown_document_structure: str = documentation["markdown_document_structure"]
    doc_crafting_modular_code: str = documentation["crafting_modular_code"]
    doc_writing_modularly: str = documentation["writing_modularly"]

class ContentGenerationFlow(Flow[ContentState]):
    @start()
    def generate_content(self):
        self.generate_outline()

        for microlesson in self.state.microlessons:
            microlesson["sme_response"] = self.sme_generate_microlesson(microlesson)
            self.state.microlessons_text = f"{self.state.microlessons_text} {microlesson['sme_response']}"

        self.state.microlessons_text = ""

        if self.state.final_format == "Slides":
            for microlesson in self.state.microlessons:
                microlesson["led_response"] = self.led_generate_microlesson_slides(microlesson)
                self.state.microlessons_text = f"{self.state.microlessons_text} {microlesson['led_response']}"
        else:
            for microlesson in self.state.microlessons:
                microlesson["led_response"] = self.led_generate_microlesson(microlesson)
                self.state.microlessons_text = f"{self.state.microlessons_text} {microlesson['led_response']}"
        
        return self.construct_response()

    def generate_outline(self):
        result = (
            OutlineCrew()
            .crew()
            .kickoff(inputs=self.state.model_dump())
        )

        token_history.append(result.token_usage)

        outline = json.loads(result.raw)

        self.state.prerequisites = outline["prerequisites"]
        self.state.microlessons = outline["microlessons"]

    def sme_generate_microlesson(self, microlesson):

        microlesson_output = (
            ContentCrew()
            .crew()
            .kickoff(inputs={
                **self.state.model_dump(),
                **microlesson
            })
        )

        token_history.append(microlesson_output.token_usage)

        print("SME is done with microlesson", microlesson["id"])

        return microlesson_output.raw

    def led_generate_microlesson(self, microlesson):
        microlesson_output = (
            LdCrew()
            .crew()
            .kickoff(inputs={
                **self.state.model_dump(),
                **microlesson
            })
        )

        print("LED is done with microlesson", microlesson["id"])

        token_history.append(microlesson_output.token_usage)

        return microlesson_output.raw
    
    def led_generate_microlesson_slides(self, microlesson):
        microlesson_output = (
            SlidesCrew()
            .crew()
            .kickoff(inputs={**self.state.model_dump(), **microlesson})
        )

        print("LED is done with slides for microlesson", microlesson["id"])

        token_history.append(microlesson_output.token_usage)

        return microlesson_output.raw

    def construct_response(self):
        module = {
            "title": self.state.module_title,
            "about": self.state.module_topic,
            "learner_persona": self.state.learner_persona,
            "prerequisites": self.state.prerequisites,
            "tools": self.state.tools,
            "microlessons": self.state.microlessons
        }

        return json.dumps(module)

def kickoff():
    content_generation_flow = ContentGenerationFlow()
    content_generation_flow.kickoff()


def plot():
    content_generation_flow = ContentGenerationFlow()
    content_generation_flow.plot()


if __name__ == "__main__":
    kickoff()
