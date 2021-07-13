from __future__ import annotations

from typing import Any, Dict

from loguru import logger


# pylint:disable=R0201
class State:
    """
    State base class

    Attributes:
        name (str): State name, use to match which state in cache
        machine (Machine): State machine instance
            used to reference back to the machine itself
    """

    name: str = ""
    machine: Machine

    def __init__(self, machine):
        self.machine = machine

    def execute(self, user_id="", payload: Any = None, **kwargs) -> Any:
        """
        Function execute, write your business logic here in subclasses

        Args:
            user_id (str): User ID. Default to ""
            payload (Any, optional): Message payload. Defaults to None.

        Raises:
            Exception: Raised when called directly

        Returns:
            Any: Any data depends on subclass implenation
                Can return status code for further debugging and API responses
        """
        raise Exception("This function should be implemented in subclass!")


class Machine:
    """
    State machine base class

    Attributes:
        name (str): Machine name, use to match which machine in cache
        states (Dict[str, State]): Dictionary pair of state classes
            Use state name as key and State subclass as value
            State subclasses will be initialized to instance in __init__ function
    """

    name: str = ""
    states: Dict[str, State]

    def execute(self, state="", user_id="", payload="", **kwargs) -> Any:
        """
        Execute state function directly

        Args:
            state (str, optional): State name. Defaults to "".
            user_id
            payload (str, optional): Line payload. Defaults to "".

        Returns:
            Any: Any data depends on state implenation
                Can return status code for further debugging and API responses
        """
        # Init state object in runtime
        state: State = self.states[state](self)
        logger.info(
            f"Execute {state.name} payload: {payload} user_id: {user_id} kwargs: {kwargs}"
        )
        return state.execute(user_id=user_id, payload=payload, **kwargs)
