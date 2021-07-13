from common.line.classes import Event, TextMessage
from common.line.utilities import reply_message

from ..classes import State


class Reply(State):
    name = "reply"

    def execute(self, user_id="", payload: Event = None, **kwargs):
        reply_message(payload.replyToken, [TextMessage("Invalid option")])
        return "Invalid option"
