from crewai import Agent
import os
from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from tool import tool
from crewai.llm import LLM 
llm = LLM(
    model="gemini/gemini-2.5-pro-exp-03-25",  # Explicit provider/model
    api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.5,
    verbose=True
)


researcher=Agent(
    role="Senior Researcher",
    goal="Uncover ground breaking technologies in {topic}",
    llm=llm,
    verbose=True,
    memory=True,
    backstory=(
 "Driven by curiosity, you're at the forefront of"
        "innovation, eager to explore and share knowledge that could change"
        "the world."
    ),
    tools=[tool],
    allow_delegation=True
)


writer=Agent(
    role="Writer",
    goal="Uncover ground breaking technologies in {topic}",
    llm=llm,
    verbose=True,
    memory=True,
    backstory=(
"With a flair for simplifying complex topics, you craft"
    "engaging narratives that captivate and educate, bringing new"
    "discoveries to light in an accessible manner."
    ),
    tools=[tool],
    allow_delegation=False
)
