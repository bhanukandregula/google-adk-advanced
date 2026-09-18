import os

import google.auth
from google.adk.agents import Agent
from google.adk.tools import google_search

_, project_id = google.auth.default()
os.environ["GOOGLE_CLOUD_PROJECT"] = project_id # type: ignore
os.environ["GOOGLE_CLOUD_LOCATION"] = "global"
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "True"

root_agent = Agent(
    name="news_agent",
    model="gemini-3-flash-preview",
    instruction="You are a helpful AI assistant designed to provide accurate and useful information.",
    tools=[google_search],
)
