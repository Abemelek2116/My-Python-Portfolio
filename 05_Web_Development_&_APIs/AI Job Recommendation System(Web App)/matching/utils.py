def normalize_skills(skills):
    """
    Convert skills to a clean, comparable set
    """
    if not skills:
        return set()

    return {
        skill.lower().strip()
        for skill in skills
        if skill and isinstance(skill, str)
    }
