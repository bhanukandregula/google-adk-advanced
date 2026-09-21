import os
import google.auth

from google.adk import Agent
from google.adk import Workflow
from google.adk import Event


_, project_id = google.auth.default()
os.environ["GOOGLE_CLOUD_PROJECT"] = project_id # type: ignore
os.environ["GOOGLE_CLOUD_LOCATION"] = "global"
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "True"

book_review_agent = Agent(
    name="book_review_agent",
    model="gemini-3-flash-preview",
    instruction=""" Return the review of a given book in maximum 200 words """,
    output_schema=str
)

book_review_summarizer_agent = Agent(
    name="book_review_summarizer_agent",
    model="gemini-3-flash-preview",
    instruction=""" For a given book review, summarize it in maximum of 50 words """,
    output_schema=str
)

def upper_case_tool(node_input: str):
    just_upper_case = node_input.upper()
    return Event(
        output = just_upper_case
    )

root_agent = Workflow(
    name="root_agent",
    edges=[
        ("START", book_review_agent, book_review_summarizer_agent, upper_case_tool),
    ]
)
