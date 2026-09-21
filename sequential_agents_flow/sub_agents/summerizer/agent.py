import os

import google.auth
from google.adk.agents import LlmAgent

_, project_id = google.auth.default()
os.environ["GOOGLE_CLOUD_PROJECT"] = project_id # type: ignore
os.environ["GOOGLE_CLOUD_LOCATION"] = "global"
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "True"

summerizer_agent = LlmAgent(
    name="summerizer_agent",
    model="gemini-3-flash-preview",
    description="An agent which is good at summarizing content shared with it.",
    instruction="You are a summarizer agent. You will be given a piece of news content "
    "and you need to create a concise summary of it.\n\n"
    "News content to summarize:\n{news}",
)
