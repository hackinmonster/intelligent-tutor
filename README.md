### Testing the MCP server

For testing, use MCP inspector: https://modelcontextprotocol.io/docs/tools/inspector

You can install it globally like  this:

```npm install -g @modelcontextprotocol/inspector```

And then run it with

```mcp-inspector```

You can access the tool via browser and use the following settings:

Transport type: STDIO

Command: python

Arguments: -m canvas_mcp.main

Then set environment variables:

PYTHONPATH: (insert path to mcp_servers directory)

CANVAS_BASE_URL: https://uncc.instructure.com

CANVAS_API_TOKEN: (create an access token in Canvas under settings)


