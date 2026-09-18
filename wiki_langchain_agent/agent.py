import os

import google.auth
import wikipedia.wikipedia as wikipedia_client
from google.adk import Agent
from google.adk.integrations.langchain import LangchainTool
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

# Wikimedia rejects the wikipedia package's default User-Agent (403/429). The
# package reads USER_AGENT from its inner module, so it must be set there.
wikipedia_client.USER_AGENT ="explore-google-adk/0.1 (wiki_langchain_agent)"

_, project_id = google.auth.default()
os.environ["GOOGLE_CLOUD_PROJECT"] = project_id # type: ignore
os.environ["GOOGLE_CLOUD_LOCATION"] = "global"
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "True"

root_agent = Agent(
    name="wiki_langchain_agent",
    model="gemini-3-flash-preview",
    instruction="You are an agent that can perform Wikipedia searches using the " \
    "LangChain WikipediaQueryRun tool. You can use this tool to search for " \
    "information on Wikipedia and provide relevant results to the user. " \
    "Please ensure that you use the tool responsibly and follow best practices " \
    "when performing searches.",
    description="An agent that can perform Wikipedia searches using the LangChain " \
    "WikipediaQueryRun tool.",
    tools=[
        LangchainTool(
            tool=WikipediaQueryRun(
                api_wrapper=WikipediaAPIWrapper()
            ),
            name="WikipediaQueryRun",
            description="A tool for searching Wikipedia using LangChain's WikipediaQueryRun.",
        )
    ]
)
