from agent import content_gatherer, content_thinker, content_writer
from tools import tool
from crewai import Task

content_gatherer_task = Task(
    description=(
        "Gather information regarding topic: {topic}. "
        "It should be relevant to age group: {age} for social media: {socialMedia}."
    ),
    expected_output=(
        "A well formatted words regarding topic: {topic}."
    ),
    tools=[tool],
    agent=content_gatherer
)

content_thinker_task = Task(
    description=(
        "Think about the topic: {topic}, for social media: {socialMedia}. "
        "Maintain formality: {formality} and age group: {age}."
    ),
    expected_output=(
        "A well formatted paragraph regarding topic: {topic}."
    ),
    tools=[tool],
    agent=content_thinker
)

content_writer_task = Task(
    description=(
        "Write a content on topic: {topic}. Make it more attractive. "
        "Maintain {formality} for audience of age group: {age} "
        "for social media platform: {socialMedia}."
    ),
    expected_output=(
        "A well structured paragraph(s) on topic: {topic}."
    ),
    tools=[tool],
    agent=content_writer
)
