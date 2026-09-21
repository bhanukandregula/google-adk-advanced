import os

import google.auth
from google.adk import Agent

_, project_id = google.auth.default()
os.environ["GOOGLE_CLOUD_PROJECT"] = project_id # type: ignore
os.environ["GOOGLE_CLOUD_LOCATION"] = "global"
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "True"

brand_story_agent = Agent(
    name="brand_story_agent",
    model="gemini-3-flash-preview",
    description="An agent who creates a brand story on a given topic",
    instruction="You are an agent who specializes in creating brand story. "
    "Please make sure the story is relevant to current generation and it is limited "
    "to 5 lines and crisp in nature",
)
