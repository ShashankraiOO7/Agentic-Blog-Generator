from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, task, crew
from crewai_tools import SerperDevTool, FileWriterTool
from dotenv import load_dotenv

load_dotenv()

#llm = LLM(model="gemini-1.5-pro")
@CrewBase
class BlogCrew():
    '''Blog Crew'''

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    # === AGENTS ===
    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["researcher"],
            tools=[SerperDevTool()],
            verbose=True
        )

    @agent
    def writer(self) -> Agent:
        return Agent(
            config=self.agents_config["writer"],
        
            verbose=True
        )

    @agent
    def fact_checker(self) -> Agent:
        return Agent(
            config=self.agents_config["fact_checker"],
            #llm=llm,
            tools=[SerperDevTool()],
            verbose=True
        )

    @agent
    def seo_expert(self) -> Agent:
        return Agent(
            config=self.agents_config["seo_expert"],
            #llm=llm,
            tools=[SerperDevTool()],
            verbose=True,
            reasoning=True
        )

    @agent
    def file_writer(self) -> Agent:
        return Agent(
            config=self.agents_config["file_writer"],
            #llm=llm,
            tools=[FileWriterTool()],
            verbose=True
        )

    # === TASKS ===
    @task
    def do_research(self, input=None) -> Task:
        return Task(
            config=self.tasks_config["do_research"]
        )

    @task
    def generate_draft(self, input=None) -> Task:
        return Task(
            config=self.tasks_config["generate_draft"]
        )

    @task
    def verify_facts(self, input=None) -> Task:
        return Task(
            config=self.tasks_config["verify_facts"]
        )

    @task
    def optimize_seo(self, input=None) -> Task:
        return Task(
            config=self.tasks_config["optimize_seo"]
        )

    @task
    def file_write_task(self, input=None) -> Task:
        return Task(
            config=self.tasks_config["file_write_task"],
            output_file='Output.md'
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
