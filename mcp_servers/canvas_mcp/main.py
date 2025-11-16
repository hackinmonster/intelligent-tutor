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

@mcp.tool
def clean_assignments(course_id: int):
    """Return clean assignments for a specific course."""
    return list_clean_assignments(canvas, course_id)

@mcp.tool
def weak_grades(course_id: int):
    """Return weak grades for a specific course."""
    return get_weak_grades(canvas, course_id)

@mcp.tool
def strong_grades(course_id: int):
    """Return strong grades for a specific course."""
    return get_strong_grades(canvas, course_id)

@mcp.tool
def overdue(course_id: int):
    """Return overdue assignments for a specific course."""
    return get_overdue(canvas, course_id)

if __name__ == "__main__":
    mcp.run()
