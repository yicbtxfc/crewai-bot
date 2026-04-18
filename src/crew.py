from crewai import Agent, Task, Crew

def run_crew():

    job_finder = Agent(
        role="Cybersecurity Job Finder",
        goal="Find cybersecurity job opportunities",
        backstory="Expert at analyzing job boards and security roles."
    )

    skills_matcher = Agent(
        role="Skills Matcher",
        goal="Match user skills to job requirements",
        backstory="Career advisor specializing in cybersecurity hiring trends."
    )

    portfolio_builder = Agent(
        role="Portfolio Builder",
        goal="Suggest cybersecurity learning projects",
        backstory="Senior cybersecurity engineer mentoring beginners."
    )

    task1 = Task(
        description="Find cybersecurity job opportunities",
        agent=job_finder
    )

    task2 = Task(
        description="Match skills to job requirements",
        agent=skills_matcher
    )

    task3 = Task(
        description="Suggest portfolio projects",
        agent=portfolio_builder
    )

    crew = Crew(
        agents=[job_finder, skills_matcher, portfolio_builder],
        tasks=[task1, task2, task3],
        memory=True  # enables memory if supported in your setup
    )

    return crew.kickoff()
