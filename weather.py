from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")

@mcp.tool()

#location parameter is annotated as str
async def get_weather(location:str)-> str:
    '''get the weather at a particular location. we can use any third party API'''
    return "It's 34.4 degree Celcius and 70 percent humid"

if __name__=="__main__":
    mcp.run(transport="streamable-http")