import os
import google.auth
from google.adk.agents import Agent, LlmAgent
from .sub_agents.traffic.agent import traffic_agent
from .sub_agents.story.agent import story_agent
from .sub_agents.song.agent import song_agent
from google.adk.tools.agent_tool import AgentTool

_, project_id = google.auth.default()
os.environ["GOOGLE_CLOUD_PROJECT"] = project_id # type: ignore
os.environ["GOOGLE_CLOUD_LOCATION"] = "global"
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "True"

root_agent = LlmAgent(
    name="RootAgent",
    model="gemini-3-flash-preview",
    description="A root agent that coordinates between different specialized agents.",
    instruction="You are the root agent. Your role is to delegate tasks to "
    "specialized agents based on user queries. If a query is related to traffic, "
    "delegate it to the TrafficAgent. If it's about stories, delegate it to the StoryAgent. "
    "If it's about songs, delegate it to the SongAgent. Provide clear instructions "
    "and context when delegating tasks.",
    tools=[AgentTool(traffic_agent), AgentTool(story_agent), AgentTool(song_agent)]
)
