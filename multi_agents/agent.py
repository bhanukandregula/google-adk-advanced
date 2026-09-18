import os
import google.auth
from google.adk.agents import Agent, LlmAgent

_, project_id = google.auth.default()
os.environ["GOOGLE_CLOUD_PROJECT"] = project_id # type: ignore
os.environ["GOOGLE_CLOUD_LOCATION"] = "global"
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "True"

traffic_agent = LlmAgent(
    name="TrafficAgent",
    model="gemini-3-flash-preview",
    instruction="You are a traffic information agent. Provide real-time traffic updates, road conditions, and travel advice based on user queries.",
    description="An agent that provides traffic updates and information.",
)

story_agent = LlmAgent(
    name="StoryAgent",
    model="gemini-3-flash-preview",
    instruction="You are a story generation agent. Create engaging and creative stories based on user prompts.",
    description="An agent that generates stories.",
)

song_agent = LlmAgent(
    name="SongAgent",
    model="gemini-3-flash-preview",
    instruction="You are a song creation agent. Compose lyrics and melodies based on user input.",
    description="An agent that creates songs.",
)

root_agent = LlmAgent(
    name="RootAgent",
    model="gemini-3-flash-preview",
    description="A root agent that coordinates between different specialized agents.",
    instruction="You are the root agent. Your role is to delegate tasks to "
    "specialized agents based on user queries. If a query is related to traffic, "
    "delegate it to the TrafficAgent. If it's about stories, delegate it to the StoryAgent. "
    "If it's about songs, delegate it to the SongAgent. Provide clear instructions "
    "and context when delegating tasks.",
    sub_agents=[traffic_agent, story_agent, song_agent]
)
