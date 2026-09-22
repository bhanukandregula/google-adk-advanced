
import os
import google.auth

from google.adk import Agent
from google.adk.agents import LlmAgent


_, project_id = google.auth.default()
os.environ["GOOGLE_CLOUD_PROJECT"] = project_id # type: ignore
os.environ["GOOGLE_CLOUD_LOCATION"] = "global"
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "True"

weather_agent = Agent(
    name="weather_agent",
    model="gemini-3-flash-preview",
    instruction=
    """
    Suggest random weather for a given city. Just make the weather. No need to say that you cannnot
    get realtime weather.
    """,
    description="An agent which an provide weather updates for a given city"
)

flight_agent = LlmAgent(
    name="flight_agent",
    model="gemini-3-flash-preview",
    instruction=
    """
    Suggest a random flight details between 2 cities. If city names are not provided, ask for that.

    Crucial: Once you have both cities, provide the flight details directly to the user. Do not
    call or transfer back to 'travel_agent'.
    """,
    description = "An agent whi helps with flight information.",
)

travel_agent = LlmAgent(
    name="travel_agent",
    model="gemini-3-flash-preview",
    instruction=
    """
    You are a coordinator who helps with weather and flight information.
    """,
    sub_agents=[weather_agent, flight_agent],
)

root_agent = travel_agent



