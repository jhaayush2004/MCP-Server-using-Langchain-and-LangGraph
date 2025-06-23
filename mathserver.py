from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Maths")

@mcp.tool()
def add(a:int, b:int) -> int:
    return a+b

@mcp.tool()
def multiply(a:int, b:int) -> int:
    return a*b

if __name__ == "__main__":
    mcp.run(transport="stdio")

# When transport="stdio" is used, the communication happens over the standard input (stdin) and standard output (stdout) streams. These streams are inherently tied to the console or command prompt from which the program is launched.
# Or we can simply say outputs can be recieved in console itself.