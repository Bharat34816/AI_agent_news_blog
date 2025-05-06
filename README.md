AI Agent for Research and Writing
This project implements an AI-powered agent system consisting of two main agents:

Researcher Agent: An AI agent responsible for gathering information and conducting research on specific topics.

Writer Agent: An AI agent that takes the research material and writes content based on the gathered data.

The system is designed to automate content creation, such as blog posts or articles, by utilizing the capabilities of both agents to perform research and then write a structured piece of content.

Installation
To use this project, follow the steps below to set up your environment:

Clone the repository:

bash
Copy
Edit
git clone https://github.com/Bharat34816/AI_agent_news_blog
cd AI_agent_news_blog
Create a virtual environment:

bash
Copy
Edit
python3 -m venv venv
Activate the virtual environment:

bash
Copy
Edit
source venv/bin/activate  # For Linux/MacOS
venv\Scripts\activate  # For Windows
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
How It Works
The AI agents work together in a sequential process:

Researcher Agent:

The Researcher agent is responsible for gathering data related to a specified topic. It can search the internet, analyze content, and organize research materials.

Writer Agent:

Once the research is completed, the Writer agent takes the data and generates well-structured content like blog posts or articles based on the research provided.

Agent Workflow (Flowgraph)
Here’s a flowgraph illustrating how the system works step-by-step:

Step 1: Input Topic
User Input: The user provides a topic they want content on (e.g., "AI in healthcare").

Step 2: Research Phase
Researcher Agent:

The agent initiates a web search or database lookup to gather data related to the topic.

The agent filters and organizes the data into usable research material.

The research data is formatted and ready for the Writer Agent.

Flowgraph for Researcher Agent:

csharp
Copy
Edit
[User Input (Topic)]
       ↓
[Researcher Agent Initiates Search]
       ↓
[Gather Data]
       ↓
[Process & Organize Information]
       ↓
[Research Material Ready for Writing]
Step 3: Writing Phase
Writer Agent:

The Writer agent receives the organized research data.

It uses the research to generate structured, well-written content.

The content is tailored to the topic and presented in a readable format for publication.

Flowgraph for Writer Agent:

csharp
Copy
Edit
[Research Material]
       ↓
[Writer Agent Begins Content Creation]
       ↓
[Generate Structured Content (Blog, Article)]
       ↓
[Content Ready for Output]
Step 4: Output
The final written content is produced and can be displayed to the user or published on a website.

Final Output:

csharp
Copy
Edit
[Final Content (Blog Post / Article)]
Example Workflow
User Input: The user enters the topic "AI in Healthcare".

Researcher Agent: The agent searches the web for articles, papers, and research reports on AI in healthcare. It processes and organizes the data into research material.

Writer Agent: The writer agent takes the research and generates a detailed article about AI's impact on healthcare, focusing on applications, trends, and future directions.

Output: The article is displayed to the user or published as a blog post.
