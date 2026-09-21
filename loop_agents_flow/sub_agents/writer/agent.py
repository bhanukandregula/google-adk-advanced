import os

import google.auth
from google.adk import Agent

_, project_id = google.auth.default()
os.environ["GOOGLE_CLOUD_PROJECT"] = project_id # type: ignore
os.environ["GOOGLE_CLOUD_LOCATION"] = "global"
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "True"

writer_agent = Agent(
    name="writer_agent",
    model="gemini-3-flash-preview",
    description="An agent who writes a short brand story and improves it using feedback.",
    instruction="You are a brand story writer. Write a brand story on the topic given "
    "by the user. It must be exactly 3 lines long, with at most 10 words per line.\n\n"
    "Reviewer feedback from the previous round (if any):\n{feedback?}\n\n"
    "If there is feedback, rewrite the previous draft to fix every point. "
    "Return only the story, nothing else.",
    output_key="draft",
)
