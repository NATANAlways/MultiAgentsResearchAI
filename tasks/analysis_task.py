import textwrap

from crewai import Task
from agents.data_analyst import data_analyst_agent
from tasks.research_task import research_task

analysis_task = Task(
    agent = data_analyst_agent,
    description = textwrap.dedent("""
        Analyze the research findings for the topic: {topic}
        
        your tasks:
        1. Review the research findings from the previous task
        2. Find the relevance data and information of the given topic
        3. Identify patterns, trends, and key insights
        4. Analyse the implications and significance
        5. Provide expert interpretation of the data
        6. Highlight the most important conclusions
    """),
    expected_output = "A detailed analysis report with insights, patterns and conclusions relevant to the topic given",
    context=[research_task],
    output_file="analysis_report.md"
)