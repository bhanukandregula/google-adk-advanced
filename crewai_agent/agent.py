from google.adk import Agent
from google.adk.tools.crewai_tool import CrewaiTool
from crewai_tools import ScrapeWebsiteTool

import os
import google.auth

_, project_id = google.auth.default()
os.environ["GOOGLE_CLOUD_PROJECT"] = project_id # type: ignore
os.environ["GOOGLE_CLOUD_LOCATION"] = "global"
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "True"

scrape_news_tool = CrewaiTool(
    name="scrape_news",
    description="Scrape news articles from a given website.",
    tool=ScrapeWebsiteTool("https://techartphotography.com"),
)

root_agent = Agent(
    name="root_agent",
    model="gemini-3-flash-preview",
    instruction="You are an agent that can scrape news articles from a given website. " \
    "You can use the provided tools to scrape news articles. " \
    "Please ensure that you use the tools responsibly and follow best practices when scraping news articles.",
    description="Root agent for scraping news articles.",
    tools=[scrape_news_tool],
)
