from typing import List

from cache import CacheUser
from common.enums import EnumResponse
from common.line.classes import Event
from loguru import logger
from machine import MACHINE
from machine.classes import Machine

# pylint: disable=E0611
from pydantic import BaseModel

# pylint: enable=E0611


DOC = {
    200: EnumResponse.OK.value.doc,
    500: EnumResponse.INTERNAL_SERVER_ERROR.value.doc,
}


class Payload(BaseModel):
    destination: str
    events: List[Event]


def post(payload: Payload):

    try:
        for event in payload.events:
            machine: Machine = None
            state: str = ""

            user_id = event.source["userId"]
            if event.type == "message" and event.message["type"] == "text":
                message = event.message["text"]
                # Retrieve from session
                if CacheUser.get(user_id):
                    machine = MACHINE[CacheUser.get(user_id)["machine"]]
                    state = CacheUser.get(user_id)["state"]
                # No session, use pre-defined flow
                if message == "/quickreply":
                    machine = MACHINE["quickreply"]
                    state = "question"
            # Unhandled requests goes to default reply
            if machine is None:
                machine = MACHINE["default"]
                state = "reply"

            machine.execute(state, user_id, event)

        return EnumResponse.OK.value.response
    except Exception as error:
        logger.error(error)
        return EnumResponse.INTERNAL_SERVER_ERROR.value.response
