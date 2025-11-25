from canvas_mcp.tools.dates import is_overdue

def get_assignments(canvas, course_id: int):
    """Return all assignments for a given course."""
    return canvas.get(f"courses/{course_id}/assignments")

def list_clean_assignments(canvas, course_id):
    """Return a list of clean assignments for a given course."""
    raw = canvas.get(f"courses/{course_id}/assignments")  

    cleaned = []
    for a in raw:
        s = a.get("submission", {})
        cleaned.append({
            "id": a["id"],
            "name": a["name"],
            "due_at": a["due_at"],
            "points_possible": a.get("points_possible"),
            "score": s.get("score"),
            "late": s.get("late"),
            "missing": s.get("missing"),
            "percentage": (s["score"] / a["points_possible"] * 100)
                         if s.get("score") is not None and a.get("points_possible")
                         else None,
            "html_url": a.get("html_url"),
        })
    return cleaned

def get_weak_grades(canvas, course_id, threshold=80):
    """Return a list of weak grades for a given course."""
    assignments = list_clean_assignments(canvas, course_id)
    return [
        a for a in assignments
        if a["percentage"] is not None and a["percentage"] < threshold
    ]

def get_strong_grades(canvas, course_id, threshold=80):
    """Return a list of strong grades for a given course."""
    assignments = list_clean_assignments(canvas, course_id)
    return [
        a for a in assignments
        if a["percentage"] is not None and a["percentage"] >= threshold
    ]

def get_overdue(canvas, course_id):
    """Return a list of overdue assignments for a given course."""
    assignments = list_clean_assignments(canvas, course_id)
    return [a for a in assignments if is_overdue(a["due_at"])]
