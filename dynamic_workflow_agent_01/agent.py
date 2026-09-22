
import os
from platform import node
from typing import Any
import google.auth

from google.adk import Agent
from google.adk import Workflow
from google.adk import Event
from google.adk.workflow import node
from google.adk import Context


_, project_id = google.auth.default()
os.environ["GOOGLE_CLOUD_PROJECT"] = project_id # type: ignore
os.environ["GOOGLE_CLOUD_LOCATION"] = "global"
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "True"


city_name_agent = Agent(
    name="city_name_agent",
    model="gemini-3-flash-preview",
    instruction=
    """
    Suggest random famous city name. Just the name, nothing else.
    """
)

@node(name="final_message_city_node")
def final_message_city_node(node_input: Any):
    return Event(
        output = f"Hello, {node_input}. It is a nice place to visit.\n"
    )

@node(name="welcome_city_node")
def welcome_city_node(node_input: Any):
    return Event(
        output = f"Welcome to {node_input}"
    )

@node(rerun_on_resume=True)
async def my_workflow(ctx: Context, node_input: str) -> str:
    city_name = await ctx.run_node(city_name_agent)
    welcome_message = await ctx.run_node(welcome_city_node, node_input=city_name)
    final_message = await ctx.run_node(final_message_city_node, node_input=welcome_message)
    return final_message

root_agent = Workflow(
    name="root_agent",
    edges = [
        ("START", my_workflow)
    ]
)


