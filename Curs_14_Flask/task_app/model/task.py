from dataclasses import dataclass
from enum import Enum


class TaskStatus(Enum):  # Enum - lista cu optiuni
    d = "done"
    t = "todo"
    p = "in progress"


@dataclass
class Task:
    title: str
    todo: str
    status: TaskStatus
