import os
from crewai import Agent, LLM
from crewai_tools import FileWriterTool

# LLM configuration -Agents specific config
model = os.getenv("WRITER_AGENT_LLM")
temperature = float(os.getenv("WRITER_AGENT_TEMPERATURE"))

llm = LLM(
    model=model,
    temperature=temperature
)

content_writer_agent = Agent(
    role = 'Content Writer',
    goal = 'Create Comprehensive, well-stuctured reports and summaries',
    backstory = (
        "You are a professional content writer with expertise in creating"
        "clear, engaging, and well-structured documents. You can transform complex"
        "information into accessible and compelling content"
        "in a very simple english with necessary technical words"
        "with necessary definition of technical words."
    ),
    llm = llm,
    tools = [FileWriterTool()],
    verbose=True,
)