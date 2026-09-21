import os
import google.auth

from google.adk import Agent
from google.adk import Workflow


_, project_id = google.auth.default()
os.environ["GOOGLE_CLOUD_PROJECT"] = project_id # type: ignore
os.environ["GOOGLE_CLOUD_LOCATION"] = "global"
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "True"


city_visit_places_agent = Agent(
    name="city_visit_places_agent",
    model="gemini-3-flash-preview",
    instruction=
    """ When a city name is provided, return the primary places to visit.
    Limit the answer to 10.
    """
)

city_best_time_visit_agent = Agent(
    name="city_best_time_visit_agent",
    model="gemini-3-flash-preview",
    instruction=
    """ The input is a list of places to visit in a city.
    Return the best time of year to visit the city and, for each place, any
    seasonal or time-of-day advice.
    """
)

root_agent = Workflow(
    name="root_agent",
    edges=[
        ("START", city_visit_places_agent, city_best_time_visit_agent),
    ]
)