import os
from re import M
import google.auth
from google.adk import Agent
from google.adk import Workflow
from google.adk import Event
from google.adk.events import RequestInput


_, project_id = google.auth.default()
os.environ["GOOGLE_CLOUD_PROJECT"] = project_id # type: ignore
os.environ["GOOGLE_CLOUD_LOCATION"] = "global"
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "True"

city_list_agent = Agent(
    name="city_list_agent",
    model="gemini-3-flash-preview",
    instruction=
    """
        List top 10 nice to visit cities in the world.
        Just list the names.
        Do not provice any further details.
    """
)

def choose_city():
    yield RequestInput(message="Enter your city selection: ", response_schema=None)

def welcome_city(node_input):
    return Event(
        output=f"{node_input}\n is a nice place."
    )

city_details_agent = Agent(
    name="city_details_agent",
    model="gemini-3-flash-preview",
    instruction=
    """

    When a city name provided,
    list down the palces to visit in the city.
    Limit the putput to 10 lines

    """
)

root_agent = Workflow(
    name="root_agent",
    edges=[
        ("START", city_list_agent, choose_city, city_details_agent)
    ]
)
