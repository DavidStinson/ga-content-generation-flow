from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.knowledge.source.text_file_knowledge_source import TextFileKnowledgeSource

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

chatgpt_41 = LLM(
    model="gpt-4.1",
    max_tokens=16384,
)

openai_o3 = LLM(
    model="o3",
    max_tokens=8192,
)

text_sources_learning_experience_designer = TextFileKnowledgeSource(
    file_paths=["creating-clear-exercises.txt",
                "markdown-document-structure.txt", "modular-code.txt",
                "modular-writing.txt", "technical-voice.txt",
                "creating-inclusive-and-globally-relevant-content.txt"
               ]
)

@CrewBase
class LdCrew():
    """LdCrew crew"""

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def learning_experience_designer(self) -> Agent:
        return Agent(
            config=self.agents_config['learning_experience_designer'],
            verbose=True,
            llm=chatgpt_41,
            knowledge_sources=[text_sources_learning_experience_designer],
            cache=False
        )
    
    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def learning_design_task(self) -> Task:
        return Task(
            config=self.tasks_config['learning_design_task'],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the LdCrew crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
