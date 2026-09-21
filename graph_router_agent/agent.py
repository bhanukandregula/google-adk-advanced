import os
import google.auth
from google.adk import Agent
from google.adk import Workflow
from google.adk import Event


_, project_id = google.auth.default()
os.environ["GOOGLE_CLOUD_PROJECT"] = project_id # type: ignore
os.environ["GOOGLE_CLOUD_LOCATION"] = "global"
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "True"

process_message = Agent(
    name="process_message",
    model="gemini-3-flash-preview",
    instruction=
    """
        Classify user message into either "BUG", "CUSTOMER_SUPPORT", or "LOGISTICS".
        If you think a message applied to more than one category,
        reply with a comma seperated list of categories.
    """
)

def router(node_input: str):
    routes = node_input.split(",")
    routes = [route.strip().upper().replace(" ", "_") for route in routes]
    return Event(route=routes) # type: ignore

def response_1_bug():
    return Event(output="Handling bug...")

def response_3_logistics():
    return Event(output="Handling logistics...")

customer_support_agent = Agent(
    name="customer_support_agent",
    model="gemini-3-flash-preview",
    instruction=
    """
        Return a 5 line basic customer support help based on technical
        issues on laptop and mobile.
    """
)

def final_response(node_input: str):
    return Event(output=node_input)

root_agent = Workflow(
    name="routing_workflow",
    edges=[
        ("START", process_message, router),
        (router, {
            "BUG": response_1_bug,
            "CUSTOMER_SUPPORT": customer_support_agent,
            "LOGISTICS": response_3_logistics
        }),
        # A workflow may have only one terminal node, so every branch
        # converges here. It runs once per matched category.
        (response_1_bug, final_response),
        (customer_support_agent, final_response),
        (response_3_logistics, final_response),
    ]
)
