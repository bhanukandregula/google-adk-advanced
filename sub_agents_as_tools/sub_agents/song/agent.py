from google.adk.agents import Agent, LlmAgent

song_agent = LlmAgent(
    name="SongAgent",
    model="gemini-3-flash-preview",
    instruction="" \
    "You are a song creation agent. Compose lyrics and melodies based on user input. " \
    "Return the results to the root agent along with any relevant context or instructions for the user.",
    description="An agent that creates songs.",
)
