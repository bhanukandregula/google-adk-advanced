import os

import google.auth
from google.adk.agents import SequentialAgent
from .sub_agents.summerizer.agent import summerizer_agent
from .sub_agents.web_searcher.agent import news_reader_agent

_, project_id = google.auth.default()
os.environ["GOOGLE_CLOUD_PROJECT"] = project_id # type: ignore
os.environ["GOOGLE_CLOUD_LOCATION"] = "global"
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "True"

root_agent = SequentialAgent(
    name="new_summarizer_agent",
    description="An agent that searched for and summarizes news on the given articles.",
    sub_agents=[news_reader_agent, summerizer_agent]
)
