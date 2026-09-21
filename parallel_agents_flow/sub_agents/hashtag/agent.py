import os

import google.auth
from google.adk import Agent

_, project_id = google.auth.default()
os.environ["GOOGLE_CLOUD_PROJECT"] = project_id # type: ignore
os.environ["GOOGLE_CLOUD_LOCATION"] = "global"
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "True"

hashtag_agent = Agent(
    name="hashtag_agent",
    model="gemini-3-flash-preview",
    description="An agent who generates hashtags for a given topic",
    instruction="You are an agent who specializes in creating social media hashtags. "
    "Given a topic, generate 5 to 8 relevant, trending hashtags for the current "
    "generation. Return only the hashtags, separated by spaces.",
)
