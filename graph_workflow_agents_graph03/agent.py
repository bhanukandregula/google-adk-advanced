import os
from re import M
import google.auth

from google.adk import Agent
from google.adk import Workflow
from google.adk import Event


_, project_id = google.auth.default()
os.environ["GOOGLE_CLOUD_PROJECT"] = project_id # type: ignore
os.environ["GOOGLE_CLOUD_LOCATION"] = "global"
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "True"

city_name_agent = Agent(
    name="city_name_agent",
    model="gemini-3-flash-preview",
    instruction=""" suggest a random famous city name. Just the name, nothing else. """
)

def welcome_city(node_input: str):
    output_value = f"Welcome to {node_input}"
    return Event(
        output = output_value
    )

def message_city(node_input):
    return Event(
        output = f"Hello, {node_input}. It is a nice place to visit.\n"
    )

root_agent = Workflow(
    name="root_agent",
    edges=[
        ("START", city_name_agent, welcome_city, message_city)
    ]
)
