from google.adk.agents import Agent, LlmAgent

story_agent = LlmAgent(
    name="StoryAgent",
    model="gemini-3-flash-preview",
    instruction="You are a story generation agent. Create engaging and creative stories based on user prompts. " \
    "Return the results to the root agent along with any relevant context or instructions for the user.",
    description="An agent that generates stories.",
)
