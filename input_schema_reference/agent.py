
import os
import google.auth

from google.adk import Agent
from google.adk.agents import LlmAgent
from pydantic import BaseModel, Field

_, project_id = google.auth.default()
os.environ["GOOGLE_CLOUD_PROJECT"] = project_id # type: ignore
os.environ["GOOGLE_CLOUD_LOCATION"] = "global"
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "True"

class CountryInput(BaseModel):
    country: str =  Field(description="The country to get information about.")


# {"country": "India"}

root_agent = LlmAgent(
    name="capital_agent",
    model="gemini-3-flash-preview",
    # instruction=
    # """
    # You are an agent which returns the capital of a country when the country name provided in json
    # format {'country':'Canada'}. if the format is not maintained by user suggest to use the
    # json format.
    # """,
    instruction=
    """
    When shared with a country name, answer with the capital of the country.
    """,
    description="An agent that helps with capital of a country",
    input_schema=CountryInput
)





