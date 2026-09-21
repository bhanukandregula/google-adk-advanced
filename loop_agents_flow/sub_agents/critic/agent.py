import os

import google.auth
from google.adk import Agent
from google.adk.tools import exit_loop

_, project_id = google.auth.default()
os.environ["GOOGLE_CLOUD_PROJECT"] = project_id # type: ignore
os.environ["GOOGLE_CLOUD_LOCATION"] = "global"
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "True"

critic_agent = Agent(
    name="critic_agent",
    model="gemini-3-flash-preview",
    description="An agent who reviews a brand story and decides if the loop can stop.",
    instruction="You are a strict reviewer. Check the brand story below against these rules: "
    "exactly 3 lines, at most 10 words per line, and an inspiring tone.\n\n"
    "Brand story:\n{draft}\n\n"
    "If every rule is met, call the exit_loop tool and say nothing else. "
    "Otherwise, reply with a short list of what must be fixed.",
    tools=[exit_loop],
    output_key="feedback",
)
