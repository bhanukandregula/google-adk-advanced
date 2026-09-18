from google.adk.agents import Agent, LlmAgent

song_agent = LlmAgent(
    name="SongAgent",
    model="gemini-3-flash-preview",
    instruction="You are a song creation agent. Compose lyrics and melodies based on user input.",
    description="An agent that creates songs.",
)
