import asyncio
from dotenv import load_dotenv
load_dotenv()
from browser_use import Agent, ChatGoogle

llm = ChatGoogle(model='gemini-2.5-flash')

async def main():
    agent = Agent(
        task="Find the number of stars of the browser-use repo",
        llm=llm
    )
    await agent.run()

asyncio.run(main())