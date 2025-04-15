#!/usr/bin/env python
from random import randint

from pydantic import BaseModel

from crewai.flow import Flow, listen, start

from ga_content_generation_flow.crews.outline_crew.outline_crew import OutlineCrew

class ContentState(BaseModel):
    module_title: str = "Introduction to Javascript Arrays"
    module_topic: str = "This JavaScript Arrays module is designed to provide a comprehensive introduction to arrays, a fundamental list datatype in programming. The module concludes with an extended practical exercise where learners will create, modify, and iterate through an array of strings. This content is suitable for beginners who are relatively new to JavaScript programming."
    learner_persona: str = "Little to no prior coding experience; basic computer literacy is assumed. Students are adult learners and aspiring professionals."
    learning_objectives: list[str] = [
        "Define JavaScript arrays and explain how they organize data.\n",
        "Identify the components of an array, including its elements and index positions.\n",
        "Create arrays using JavaScript literal notation in VS Code.\n",
        "Access and modify elements within an array using square brackets.\n",
        "Use basic array methods, such as push() and pop(), to manage array data."
    ]
    tools: str = "Visual Studio Code"
    microlessons: list[str] = []


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

        print("OUTLINE GENERATED!!!", result.raw)
        # self.state. = result.raw

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
