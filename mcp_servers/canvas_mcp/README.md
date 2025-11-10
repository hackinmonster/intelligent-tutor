# Canvas MCP

FastMCP server for interacting with the Canvas LMS API.

## Overview
This module exposes Canvas data (courses, assignments, grades, etc.) as MCP tools that can be called by LLMs or other MCP clients.  
It wraps the Canvas REST API and provides higher-level abstractions for common student tasks.

## Structure
canvas_mcp/
    - main - FastMCP app entrypoint
    - api/ - Low-level Canvas API wrappers
    - tools/ - Exposed MCP tools (overview, assignments, grades)
    - utils/ - Helpers (auth, formatting)