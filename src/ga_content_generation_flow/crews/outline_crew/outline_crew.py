from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from pydantic import BaseModel

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

# Create a text file knowledge source

claude_sonnet = LLM(
    model="claude-3-5-sonnet-20240620",
    max_tokens=8192
)

openai_o3mini = LLM(
    model="o3-mini",
    max_tokens=8192,
)

chatgpt_41 = LLM(
    model="gpt-4.1",
    max_tokens=8192,
)

class MicrolessonModel(BaseModel):
    """Represents a single microlesson within the module."""
    title: str
    slug: str
    id: int
    minutes: int
    learning_objective: str
    outline: list[str]

class ModuleModel(BaseModel):
    overview: str
    tools: list[str]
    learner_persona: str
    prerequisites: list[str]
    microlessons: list[MicrolessonModel]

@CrewBase
class OutlineCrew():
    """OutlineCrew crew"""

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def instructional_architect(self) -> Agent:
        return Agent(
            config=self.agents_config['instructional_architect'],
            verbose=True,
            llm=claude_sonnet,
            cache=False
        )
    
    @agent
    def curriculum_quality_assurance_expert(self) -> Agent:
        return Agent(
            config=self.agents_config['curriculum_quality_assurance_expert'],
            verbose=True,
            llm=openai_o3mini,
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def generate_module_outline_task(self) -> Task:
        return Task(
            config=self.tasks_config['generate_module_outline'],
            output_json=ModuleModel
        )
    
    @task
    def module_outline_qa_task(self) -> Task:
        return Task(
            config=self.tasks_config['module_outline_qa'],
            output_json=ModuleModel
        )

    @crew
    def crew(self) -> Crew:
        """Creates the OutlineCrew crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        outline_crew = Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            output_log_file="./output_logs/outline_crew"
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )

        outline_crew.reset_memories(command_type = 'all')

        return outline_crew
