from enum import Enum


class RolesEnum(str, Enum):
    """
    Constants for Roles in the tool
    """
    STUDENT = "student"
    OBSERVER = "observer"
    INSTRUCTOR = "instructor"
    ADMIN = "admin"
    TEACHING_ASSISTANT = "teaching_assistant"
    CONTENT_DEVELOPER = "content_developer"
    MENTOR = "mentor"
