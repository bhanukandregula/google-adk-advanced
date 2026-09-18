import os
from dotenv import load_dotenv
load_dotenv()

import google.auth
from google.adk.agents import Agent
# from google.adk.tools import google_search

from google.adk.tools.bigquery import BigQueryCredentialsConfig, BigQueryToolset
from google.adk.tools.bigquery.config import BigQueryToolConfig
from google.adk.tools.bigquery.config import WriteMode
from google.genai import types
import google.auth

credentials, project_id = google.auth.default()
os.environ["GOOGLE_CLOUD_PROJECT"] = project_id
os.environ["GOOGLE_CLOUD_LOCATION"] = "global"
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "True"

credentials_config = BigQueryCredentialsConfig(credentials=credentials)

tool_config = BigQueryToolConfig(
    compute_project_id=os.environ.get("GOOGLE_CLOUD_PROJECT"),
    location=os.environ.get("GOOGLE_CLOUD_LOCATION"),
    #  we can use the flag here as ALLOWED or DENIED,
    # but we can also use the flag to allow the agent to choose the write mode
    write_mode=WriteMode.BLOCKED,  # or WriteMode.ALLOWED or WriteMode.DENIED,
)

# Lets initiaite the bigquery tooslet here
bigquery_toolset = BigQueryToolset(
    credentials_config=credentials_config,
    bigquery_tool_config=tool_config,
)


root_agent = Agent(
    name="bq_agent",
    model="gemini-3-flash-preview",
    instruction="You are an agent with access to several " \
    "BigQuery tools. " \

    "Make use of those tools to answer questions and " \
    "perform tasks related to BigQuery. " \

    "You can use the tools to query data, insert data, and " \
    "perform other operations on BigQuery. " \

    "Please ensure that you use the tools responsibly and " \
    "follow best practices when interacting with BigQuery.",
    tools=[bigquery_toolset],
)
