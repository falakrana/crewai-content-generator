from crewai import Agent

from tools import tool
import os
from langchain_google_genai import ChatGoogleGenerativeAI
# from crewai import LLM

llm = ChatGoogleGenerativeAI(
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    model="gemini-2.0-flash",
    # provider="google",
    # model="gemini-pro",
    max_output_tokens=500,

    verbose=True,
    temperature=0.5,
    # google_api_key="AIzaSyAMEeev0hI4xbL94ujCJn7cfpSu0zuAkso",
)
content_gatherer = Agent(
    role = "Information gatherer",
    goal = "Gather information related to {topic}",
    backstory = "You are an expert in gathering information related to {topic} and send to targeted audience of age: {age}.",
    memory = True,
    verbose = True,
    llm = llm,
    tools=[tool],
    allow_delegation=True,
)

content_thinker = Agent(
    role = "Content thinker",
    goal = "Thinking content on the topic: {topic}.",
    backstory = "You are an expert in thinking on the topic: {topic} for audience of age: {age}. Think content for particular social media platform: {socialMedia} with {formality} manner from the information gathered from content_gatherer.",
    memory = True,
    verbose = True,
    llm = llm,
    tools=[tool],
    allow_delegation=True,    
)

content_writer = Agent(
    role = "Content writer",
    goal = "Writing content on the topic: {topic} which should be eye catchy.",
    backstory = "You are an expert in Writing on the topic: {topic} for audience of age: {age}. Write content from the information got from content_thinker. It should be applicable for audience of age: {age}.",
    memory = True,
    verbose = True,
    llm = llm,
    tools=[tool],
    allow_delegation=True,    
     
)

