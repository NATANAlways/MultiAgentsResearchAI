# 🧠 MultiAgentsResearchAI

This is a multi-agent system that automates the end-to-end academic research workflow. It simulates a virtual research team composed of autonomous agents such as a **Research Specialist**, **Data Analyst**, and **Content Writer**, each assigned specific responsibilities in the research pipeline.

Built using Python, the system uses task delegation, memory management, and inter-agent communication to research a topic, analyze data, and generate readable content based on findings.

---

## 🚀 Features

- 🤖 Multiple intelligent agents (Researcher, Analyst, Writer)
- 🔄 Task delegation via a shared `Crew`
- 📑 Automated content generation and summarization
- 📈 Data analysis through agent collaboration
- 📂 Modular architecture for extensibility
- 🛠 CLI interface to input research topics

---

## 🧩 How It Works

1. **Research Specialist**:
   - Searches and extracts relevant online content.
   - Breaks down the research query into sub-tasks.

2. **Data Analyst**:
   - Analyzes datasets or factual input.
   - Extracts patterns, trends, and summaries.

3. **Content Writer**:
   - Transforms insights into coherent paragraphs.
   - Writes final research summaries.

4. **`Crew` Module**:
   - Coordinates agents using the `main.py` entry point.
   - Assigns tasks and consolidates output.

---

## 📁 Project Structure

```
MultiAgentsResearchAI/
├── agents/
│   ├── content_writer.py            # Agent that writes readable content
│   ├── data_analyst.py              # Agent that analyzes structured/unstructured data
│   └── research_specialist.py       # Agent that gathers and breaks down research topics
│
├── tasks/
│   ├── analysis_task.py             # Defines analysis tasks for the data analyst
│   ├── research_task.py             # Defines research tasks for the specialist
│   └── writing_task.py              # Defines writing tasks for the content writer
│
├── app.py                           # Optional Streamlit interface (if applicable)
├── main.py                          # Entry point for the CLI research assistant
├── crew.py                          # Crew management and task assignment logic
├── requirements.txt                 # Python dependencies
├── research_findings.md             # Example research output file
└── README.md                        # Project documentation
```

## 🧠 Technologies Used

- Python 3.x  
- Modular class-based architecture  
- Agent design pattern  
- File-based inter-agent communication  
- Command-line interface (CLI) interaction
