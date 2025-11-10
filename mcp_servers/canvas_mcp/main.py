from fastmcp import FastMCP
from .api.client import CanvasClient
from .tools.overview import get_student_overview
from .tools.assignments import get_assignments

mcp = FastMCP("canvas-mcp")

canvas = CanvasClient()

@mcp.tool
def overview():
    """Return upcoming assignments across all active courses."""
    return get_student_overview(canvas)

@mcp.tool
def assignments(course_id: int):
    """Return assignments for a specific course."""
    return get_assignments(canvas, course_id)

if __name__ == "__main__":
    mcp.run()
