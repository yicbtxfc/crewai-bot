from crewai import Agent, Task, Crew
import yaml

def load_yaml(file_path):
    with open(file_path, "r") as f:
        return yaml.safe_load(f)

def run_crew():

    agents_data = load_yaml("src/config/agents.yaml")
    tasks_data = load_yaml("src/config/tasks.yaml")

    job_finder = Agent(
        role=agents_data["job_finder"]["role"],
        goal=agents_data["job_finder"]["goal"],
        backstory=agents_data["job_finder"]["backstory"]
    )

    skills_matcher = Agent(
        role=agents_data["skills_matcher"]["role"],
        goal=agents_data["skills_matcher"]["goal"],
        backstory=agents_data["skills_matcher"]["backstory"]
    )

    portfolio_builder = Agent(
        role=agents_data["portfolio_builder"]["role"],
        goal=agents_data["portfolio_builder"]["goal"],
        backstory=agents_data["portfolio_builder"]["backstory"]
    )

    task1 = Task(description=tasks_data["find_jobs"]["description"], agent=job_finder)
    task2 = Task(description=tasks_data["match_skills"]["description"], agent=skills_matcher)
    task3 = Task(description=tasks_data["build_portfolio"]["description"], agent=portfolio_builder)

    crew = Crew(
        agents=[job_finder, skills_matcher, portfolio_builder],
        tasks=[task1, task2, task3],
        memory=True
    )

    return crew.kickoff()
