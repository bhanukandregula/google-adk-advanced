import os
import google.auth
from google.adk.agents import Agent
from google.adk.tools import google_search

_, project_id = google.auth.default()
os.environ["GOOGLE_CLOUD_PROJECT"] = project_id # type: ignore
os.environ["GOOGLE_CLOUD_LOCATION"] = "global"
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "True"


def add_numbers(a: float, b: float) -> float:
    """Adds two numbers provided by the user."""
    return a + b

def multiply_numbers(a: float, b: float) -> float:
    """Multiplies two numbers provided by the user."""
    return a * b

root_agent = Agent(
    name="math_agent",
    model="gemini-3-flash-preview",
    instruction="You are an agent that can perform basic arithmetic operations " \
    "like addition and multiplication. " \
    "You can use the provided tools to add or multiply two numbers. " \
    "Please ensure that you use the tools responsibly and follow best " \
    "practices when performing arithmetic operations.",
    description="An agent that can perform basic arithmetic operations like " \
    "addition and multiplication.",
    tools=[add_numbers, multiply_numbers]
)
