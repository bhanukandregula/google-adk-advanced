import os

import google.auth
from google.adk.agents import LoopAgent
from .sub_agents.writer.agent import writer_agent
from .sub_agents.critic.agent import critic_agent

_, project_id = google.auth.default()
os.environ["GOOGLE_CLOUD_PROJECT"] = project_id # type: ignore
os.environ["GOOGLE_CLOUD_LOCATION"] = "global"
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "True"

root_agent = LoopAgent(
    name="brand_story_loop_agent",
    description="An agent that writes a brand story and refines it with a critic until "
    "the critic approves or the maximum number of iterations is reached.",
    sub_agents=[writer_agent, critic_agent],
    max_iterations=3,
)
