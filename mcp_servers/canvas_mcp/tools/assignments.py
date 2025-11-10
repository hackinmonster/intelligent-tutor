def get_assignments(canvas, course_id: int):
    """Return all assignments for a given course."""
    return canvas.get(f"courses/{course_id}/assignments")
