from ..classes import Machine
from .question import Question


class QuickReplyMachine(Machine):
    name = "quickreply"
    states = {Question.name: Question}
