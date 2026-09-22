
import os
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

process_message = Agent(
    name="process_message",
    model="gemini-3-flash-preview",
    instruction=
    """
    Classity user message into either "BUG", "CUSTOMER_SUPPORT" or "LOGISTICS". Return only one of
    these options.
    """,
    output_schema=str
)

@node(name="response_1_bug")
def response_1_bug(node_input: Any):
    return Event(
        output= "Handling bug..."
    )

@node(name="response_3_logistics")
def response_3_logistics(node_input: Any):
    return Event(
        output = "Handling logistics."
    )

customer_support_agent = Agent(
    name="customer_support_agent",
    model="gemini-3-flash-preview",
    instruction=
    """
    Return a 5 line basic customer support help based on technical issues on Laptop and Mobile.
    """,
    output_schema=str
)

@node(rerun_on_resume=True)
async def my_workflow(ctx: Context, node_input: str) -> str:
    return_message = "We are unable to process your request at this moment. Please try again later."

    issue_type = await ctx.run_node(process_message)

    if issue_type == "BUG":
        return_message = await ctx.run_node(response_1_bug, node_input=issue_type)
    elif issue_type == "CUSTOMER_SUPPORT":
        return_message = await ctx.run_node(customer_support_agent, node_input=issue_type)
    elif issue_type == "LOGISTICS":
        return_message = await ctx.run_node(response_3_logistics, node_input=issue_type)

    return return_message

root_agent = Workflow(
    name="root_agent",
    edges = [
        ("START", my_workflow)
    ]
)


