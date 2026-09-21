import os

import google.auth
from google.adk.agents import Agent
from google.adk.tools import google_search

_, project_id = google.auth.default()
os.environ["GOOGLE_CLOUD_PROJECT"] = project_id # type: ignore
os.environ["GOOGLE_CLOUD_LOCATION"] = "global"
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "True"

news_reader_agent = Agent(
    name="news_reader_agent",
    model="gemini-3-flash-preview",
    description="An agent who checks in internet and gathers the latest news on the " \
    "given topic.",
    instruction="You are a news reader agent. You will be given a topic and you need " \
    "to search the internet for the latest news on that topic. You will then summarize " \
    "the news in a concise manner.",
    tools=[google_search],
    output_key="news",
    )
