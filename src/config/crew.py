from crewai import Agent, Task, Crew

def run_crew():

    # -----------------------
    # AGENTS
    # -----------------------

    job_finder = Agent(
        role="Cybersecurity Job Finder",
        goal="Find relevant cybersecurity job opportunities",
        backstory="Expert at analyzing job listings and identifying relevant roles."
    )

    skills_matcher = Agent(
        role="Skills Matcher",
        goal="Match user skills to cybersecurity job requirements",
        backstory="Career advisor specializing in cybersecurity hiring trends."
    )

    portfolio_builder = Agent(
        role="Portfolio Builder",
        goal="Suggest cybersecurity learning projects",
        backstory="Senior cybersecurity engineer guiding learners into the industry."
    )

    # -----------------------
    # TASKS
    # -----------------------

    task1 = Task(
        description="Find cybersecurity job opportunities",
        agent=job_finder
    )

    task2 = Task(
        description="Match user skills to job requirements",
        agent=skills_matcher
    )

    task3 = Task(
        description="Suggest cybersecurity portfolio projects",
        agent=portfolio_builder
    )

    # -----------------------
    # CREW
    # -----------------------

    crew = Crew(
        agents=[job_finder, skills_matcher, portfolio_builder],
        tasks=[task1, task2, task3],
        memory=True  # enables memory if supported
    )

    return crew.kickoff()
