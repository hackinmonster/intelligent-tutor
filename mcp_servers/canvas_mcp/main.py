from fastmcp import FastMCP
from .api.client import CanvasClient
from .tools.overview import get_student_overview
from .tools.assignments import (
    get_assignments,
    list_clean_assignments,
    get_weak_grades,
    get_strong_grades,
    get_overdue,
   )
from .tools.courses import (
    list_clean_courses,
    get_course_details,
    get_course_progress,
)

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

@mcp.tool
def courses():
    """List all active courses for the current user."""
    return list_clean_courses(canvas)

@mcp.tool
def course_details(course_id: int):
    """Return detailed info about a specific course."""
    return get_course_details(canvas, course_id)

@mcp.tool
def course_progress(course_id: int):
    """Return progress info for the current user in this course."""
    return get_course_progress(canvas, course_id)

if __name__ == "__main__":
    mcp.run()
