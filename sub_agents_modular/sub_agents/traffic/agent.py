from google.adk.agents import Agent, LlmAgent

traffic_agent = LlmAgent(
    name="TrafficAgent",
    model="gemini-3-flash-preview",
    instruction="You are a traffic information agent. Provide real-time traffic updates, road conditions, and travel advice based on user queries.",
    description="An agent that provides traffic updates and information.",
)
