from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY environment variable not found")

async def main():
    try:
        agent = Agent(
            task="""find the best cars in dubai which 
            i can buy which is under 1 million and have a 
            good market to sell it as well to make sure 
            if im selling it back ill not lose money """,
            llm=ChatOpenAI(
                model="gpt-4o",
                openai_api_key=openai_api_key
            ),
        )
        result = await agent.run()
        print(result)
    except Exception as e:
        print(f"Error occurred: {str(e)}")

asyncio.run(main())