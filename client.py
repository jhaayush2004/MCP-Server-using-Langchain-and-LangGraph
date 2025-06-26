from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
#
from dotenv import load_dotenv
load_dotenv()

import asyncio

async def main():
    client = MultiServerMCPClient(
        {
            "math" : {
                "command" : "python",
                "args" : ["mathserver.py"],
                "transport" : "stdio"
            },
            "weather": {
                "url": "http://localhost:8000/mcp",  # Ensure server is running here
                "transport": "streamable_http",
            }
        }
    )

    import os
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

    tools = await client.get_tools()
    model = ChatGroq(model = "qwen-qwq-32b")
    agent = create_react_agent(
        model, tools
    )

    math_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "what's (3 + 5) x 12?"}]}
    )
    
    print("Math response:", math_response['messages'][-1].content)
    
    weather_response = await agent.ainvoke(
            {"messages": [{"role": "user", "content": "what is the weather in California?"}]}
        )
    print("Weather response:", weather_response['messages'][-1].content)
    
asyncio.run(main())


"""
(venv) D:\Documents\MLOps\MCP-Server-using-Langchain-and-LangGraph>python client.py 
Math response: The result of (3 + 5) multiplied by 12 is **96**. 

Here's the breakdown:
1. First, calculate the addition: 3 + 5 = 8
2. Then multiply the result by 12: 8 × 12 = 96
Weather response: The current weather in California is **34.4°C** with **70% humidity**. It’s quite warm and humid, so be sure to stay hydrated!

"""
