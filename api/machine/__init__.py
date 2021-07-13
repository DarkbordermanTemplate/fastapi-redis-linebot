from typing import Dict

from .classes import Machine
from .default import DefaultMachine
from .quickreply import QuickReplyMachine

MACHINE: Dict[str, Machine] = {
    DefaultMachine.name: DefaultMachine(),
    QuickReplyMachine.name: QuickReplyMachine(),
}
