import os

import google.auth
from google.adk.agents import ParallelAgent
from .sub_agents.brand_story.agent import brand_story_agent
from .sub_agents.hashtag.agent import hashtag_agent

_, project_id = google.auth.default()
os.environ["GOOGLE_CLOUD_PROJECT"] = project_id # type: ignore
os.environ["GOOGLE_CLOUD_LOCATION"] = "global"
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "True"

root_agent = ParallelAgent(
    name="new_summarizer_agent",
    description="An agent that searched for and summarizes news on the given articles.",
    sub_agents=[brand_story_agent, hashtag_agent]
)
