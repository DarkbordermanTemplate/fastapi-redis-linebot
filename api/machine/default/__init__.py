from ..classes import Machine
from .reply import Reply


class DefaultMachine(Machine):
    name = "default"
    states = {Reply.name: Reply}
